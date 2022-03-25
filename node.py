class Work(object):
    def __init__(self):
        pass


class ResourceTransform(object):
    def __init__(self, from_resource, from_units, to_resource, to_units):
        self.from_resource = from_resource  # resource name
        self.from_quantity = from_units     # resource quantity
        self.to_resource = to_resource
        self.to_quantity = to_units


class BoloNode(object):
    def __init__(self, system):
        self.system = system
        self.inputs_per_step = {}
        self.outputs_per_step = {}
        self.transforms = []
        # ideally only a single transform per node
        # though maybe transformers could have multiple

    def make_resources(self):
        pass

    def consume_resources(self):
        pass

    def do_work(self):
        pass


# Collection of BoloNodes that can be queried in various ways.
class NodeDB(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.update_datastructures()

    def update_datastructures(self):
        # graph or no?
        # could just be a dict from resource name to list of transformers that can produce it
        # really want to do a graph search with a "basket" of resources and find the "best" path
        # but what about if certain nodes are committed to doing work?
        # like what if you decide to schedule work for 5 days from now but it turns out you were already going to do stuff then?
        # need to store current schedule of work and "apply" resource changes to see what would actually be like
        # what if have 5 units of labor, node requires 1 unit of labor but can only be used once per step?
        # guess should store that too
        # or have some other way of storing time use
        # is that a kind of labor?
        # like the 3d printer has 10 units of labor available per step
        # maybe call it work-time
        # so that means agents don't need to be their own thing at all!
        # and don't even need to call it anything special! just put "work" units into the resource pool
        # so in that case just need to roll-forward on work schedule to get a future version of resource pool, and use that for search?

        # should you also have work priority? could treat it as "profit", and use a scheduling algorithm that maximizes profit like https://stackoverflow.com/questions/54339470/python-scheduling-algorithm

        # what about multiple-day projects?

        # simpler to convert graph to just single "machines" somehow, and use a typical scheduling algorithm?
        # will you lose important info? could "compress" at each step...
        # simple scheduling like shortest job first: https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf
        # so formulate WorkRequests as Jobs?
        pass

    def add_node(self, node):
        self.nodes.append(node)
        self.update_datastructures()
