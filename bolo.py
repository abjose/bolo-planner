

class ResourceType(object):
    def __init__(self):
        self.name = blah
        self.lifespan = blah

        self.unit = "units"  # TODO: units, kgs, etc.
        self.integer = True


class Resource(object):
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def expires(self):
        pass


class Need(object):
    def __init__(self, resource_type, quantity, consume=True):
        self.resource_type = resource_type
        self.quantity = quantity

        # Whether the agent will consume these resources or not. Useful for
        # scheduling production, like a carrot garden scheduling a "need" to
        # have 1 kg of carrots harvested.
        self.will_consume = consume


class ResourcePool(object):
    def __init__(self):
        # resource -> amount
        self.resources = {}

    def add(resource, number):
        if resource not in self.resources:
            self.resources[resource] = 0
        self.resources[resource] += number
        assert self.resources[resource] >= 0
    def use(resource, number):
        self.add(resource, -1 * number)


class Agent(object):
    def __init__(self, name, consumes, produces, needs, is_person=False):
        self.name = name

        # Resources consumed and produced per 'use'.
        self.consumes_dict = consumes
        self.produces_dict = produces

        # For persons, will try harder to minimize labor.
        self.is_person = is_person

        # Won't work more than this. Should be reset each step. Must remember to deduct by `sork`-ing.
        self.max_uses = 8 if is_person else None
        self.remaining_uses = self.max_uses

        # Needs mapped to frequency.
        self.needs = needs

    def work(self, uses):
        if self.max_uses:
            self.remaining_uses -= uses
            assert self.remaining_uses >= 0
    def reset(self):
        self.remaining_uses = self.max_uses

    def consumes(self, r):
        return self.consumes_dict.get(r, 0)
    def produces(self, r):
        return self.produces_dict.get(r, 0)
    def net(self, r):
        return self.produces(r) - self.consumes(r)

    def all_resources(self):
        return set(self.consumes_dict.keys()) | set(self.produces_dict.keys())

# ok, now how to represent schedule of needs?
# could just ask each agent? or maybe ResourcePool records needs from agents? or NeedCalendar?
# also, things like needing to use 1 unit of labor to harvest carrots from garden?
# carrot garden could be a "conditional" agent - only available to use at certain times and only if "planted"
# and otherwise like an agent that only consumes labor
# so like - for the first however many steps it occasionally consumes labor and some other resources
# and finally it is "harvested" by consuming labor and creating carrots over a period of time
# so it's just adding regular needs like any other agent
# but also have to know to ask for carrots to actually send someone to harvest them...
# ...
# how do needs translate into "operations" on agents?
# like if carrot garden wants 1 unit of labor to poop out 1kg of carrots
# can create a need for 1 unit of labor, but how does the garden use it?
# I guess the simple thing would be to include carrots in the need?
# so need is both 1 unit of labor and 1kg carrots
# or... need could simply be 1kg carrots... but it doesn't consume them!
# have both input and output needs?
# on the other hand, "needs" don't necessarily mean the thing is consumed, I guess?
# could create a need for 1kg carrots and then not consume it
# just a flag on the need itself? consume

# ok, so bolo has list of agents
# every step, asks agents for needs
# agents generate needs - for any period of time
# bolo remembers needs and agents don't need to re-report them


class Bolo(object):
    def __init__(self):
        pass

    def step(self):
        # collect current day's needs and plan, deduct resources (or fail)
        # step through future needs and attempt to fulfill - if can't do in full, try partial too
        # can planner tell you what variable didn't work? could just remove those ones
        # I think so! it even tells you what resources are lacking!
        # make sure to subtract agent labor from their remaining labor
        pass
