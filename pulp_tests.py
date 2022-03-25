from pulp import LpMinimize, LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpConstraint, LpConstraintGE

# # Create the model
# model = LpProblem(name="small-problem", sense=LpMaximize)

# # Initialize the decision variables
# x = LpVariable(name="x", lowBound=0)
# y = LpVariable(name="y", lowBound=0)

# # Add the constraints to the model
# model += (2 * x + y <= 20, "red_constraint")
# model += (4 * x - 5 * y >= -10, "blue_constraint")
# model += (-x + 2 * y >= -2, "yellow_constraint")
# model += (-x + 5 * y == 15, "green_constraint")

# # Add the objective function to the model
# model += x + 2 * y

class Machine(object):
    def __init__(self, name, consumes, produces):
        self.name = name
        self.consumes_dict = consumes
        self.produces_dict = produces

    def consumes(self, r):
        return self.consumes_dict.get(r, 0)
    def produces(self, r):
        return self.produces_dict.get(r, 0)
    def net(self, r):
        return self.produces(r) - self.consumes(r)

    def all_resources(self):
        return set(self.consumes_dict.keys()) | set(self.produces_dict.keys())


# start and goal are dicts of resource quantities
def init_problem(start, goal, machines, model):
    m_vars = dict()
    all_resources = set()
    for machine in machines:
        m_vars[machine.name] = LpVariable(name=f"uses_{machine.name}", lowBound=0, cat="Integer")
        all_resources |= machine.all_resources()
        
    for res in all_resources:
        exp = []
        for machine in machines:
            net = machine.net(res)
            if net != 0:
                exp.append(net * m_vars[machine.name])

        if res in start:
            exp.append(start[res])
        if res in goal:
            exp.append(-goal[res])

        model += LpConstraint(e=lpSum(exp), sense=LpConstraintGE, rhs=0, name=f"res_{res}")

    # Set objective.
    model += lpSum(m_vars.values())


# Problem:
# M uses 2 units of A to make 1 unit of B
# N uses 2 units of B to make 1 unit of C
# have 8 units of A and 0 of B and C, want 2 units of C
# solution should be to use M 4x to make 4 units of B, then use N twice to make 2 units of C

# Create the model
model = LpProblem(name="small-problem", sense=LpMinimize)

M = Machine("M", {"A": 2}, {"B": 1})
N = Machine("N", {"B": 2}, {"C": 1})
# O = Machine("O", {"A": 2}, {"C": 1})
init_problem({"A": 8, "B": 2}, {"C": 4}, [M, N], model)

status = model.solve()

# probably better objective is to have the most resources left over?
# but then might do weird stuff like making unnecessary resources
# have a labor-minimizing objective? could make people count as "machines" that output 1 unit of labor each time they're activated

print(model)
print(model.solver)

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for var in model.variables():
    print(f"{var.name}: {var.value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

