from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable, LpConstraint, LpConstraintGE


def labor_value(agent):
    # Could have this be proportional to existing labor done to spread things out.
    return 10 if agent.is_person else 1


# start and goal are dicts of resource quantities
def init_problem(start, goal, agents, model):
    m_vars = dict()
    all_resources = set()
    for agent in agents:
        m_vars[agent.name] = LpVariable(name=f"uses_{agent.name}", lowBound=0, cat="Integer")
        all_resources |= agent.all_resources()

    # Apply resource requirement constraints.
    for res in all_resources:
        exp = []
        for agent in agents:
            net = agent.net(res)
            if net != 0:
                exp.append(net * m_vars[agent.name])

        if res in start:
            exp.append(start[res])
        if res in goal:
            exp.append(-goal[res])

        model += LpConstraint(e=lpSum(exp), sense=LpConstraintGE, rhs=0, name=f"res_{res}")

    # Apply max-labor constraints.
    for agent in agents:
        if agent.is_person:
            model += (m_vars[agent.name] <= agent.remaining_uses, f"{agent.name}_labor_constraint")

    # Set objective.
    # TODO: probably not the best objective.
    model += lpSum([m_vars[a.name] * labor_value(a)  for a in agents])


def solve_problem(start, goal, agents, verbose=True):
    # Create the model
    model = LpProblem(name="bolo-problem", sense=LpMinimize)
    init_problem(start, goal, agents, model)
    status = model.solve()

    if verbose:
        print(model)
        print(model.solver)

        print(f"status: {model.status}, {LpStatus[model.status]}")
        print(f"objective: {model.objective.value()}")
        for var in model.variables():
            print(f"{var.name}: {var.value()}")
        for name, constraint in model.constraints.items():
            print(f"{name}: {constraint.value()}")

    return model.status, model.variables(), model.constraints.items()
