from planner import solve_problem
from bolo import Agent, Resource

# print("woof")

# person = Agent(
#     "person1",
#     # No per-use production or consumption
#     {}, {},
#     # Needs
#     {},
#     is_person=True
# )

# bolo = Bolo()
# # system.add_agents([Person("a"), Person("b")])
# # system.resource_pool.add_resources("wood", 10)

# system.step(10)
# system.show()

# what about resource type hierarchy
# like if just need certain amount of food... nice to not explicitly enumerate


res = {
    "wood": Resource("wood"),
    "cement": Resource("cement"),
    "soil": Resource("cement"),
    "nail": Resource("nail"),
    
    "table": Resource("table"),
    "garden": Resource("garden"),
    "bed": Resource("bed"),
    "house": Resource("house"),

    "food": Resource("food"),
}


# ok.. what about making a house?
# is a house an agent or resource?
# it cetaintly has upkeep "needs"
# for gardens - you wanted them to be agents
# just need to be able to create Agents, I guess - which seems pretty reasonable
# are agents a subclass of Resource?

make_house = Agent(
    "make_house",
    {: 2},
    {"B": 1},
    {}
)
N = Agent("N", {"B": 2}, {"C": 1}, {})

A1 = Agent("Agent1", {}, {}, {}, is_person=True)
# O = Machine("O", {"A": 2}, {"C": 1})
# init_problem({"A": 8, "B": 2}, {"C": 4}, [M, N], model)

solve_problem({"A": 8, "B": 2}, {"C": 4}, [M, N])


