

"""
Consists of
- a ResourcePool (potentially pre-populated)
- a collection of ResourceTransformers
- a collection of Agents

Generates a production graph from the ResourceTransformers, and a calendar of Requirements from the Agents.
Attempts to schedule resource utilization to meet requirements.
"""
class System(object):
    def __init__(self):
        self.transformers = TransformerDB([])

    # def construct_resource_graph(self):
    #     pass
    # def query_resource_graph(self):
    #     pass

    def find_transform_sequence(self, resource, amount):
        # Find all possible sequences, or just shortest? shortest may not be best
        # maybe could have costs on graph edges? like market price?
        # need transformer database
        # first check if sufficient resource in rp, taking into account pending requests
        # find all transformers that output resource
        # trace backwards to resources we have
        # want to construct explicit graph or not? edges between every transformer that produce/consume same thing

        # hmm, in some ways - can "collapse" transfomer graph
        # so have all these pathways but really they're just "actions"
        # to turn some collection of resources into another
        # basically just caching pathways
        # but maybe doesn't sufficiently take into account things like using multiple at once
        pass

    # How long would it take to make amount of resource?
    def steps_to_fulfill(self, resource, amount):
        # find all nodes that can produce resource
        # ... basically recursive? call this on each sub-resource?
        pass

    def determine_current_needs(self):
        needs = []
        # for agent in self.agents:
        # OK, need to get needs from all agents
        # also need to ask Transformers for needs for making those needs
        # how to deal with timing? just be greedy for now? do everything you have time for?
        # or try to start X steps before the resource is due, where X is the number of steps needed to do it
        # that would be another useful query
        
        needed = self.rp.deduct_existing_resources(needed)
    
    def step(self):
        # - use ResourceRequests and ResourcePool to figure out resource needs
        # - query resource graphs to see what needs to be made
        # - step constituents

        self.rp.prune_resources()

        for node in self.nodes:
            node.make_sources()
        for work in self.current_work:
            work.node.do_work()
        for node in self.nodes:
            node.consume_sources()
        

# or just work?
class WorkRequest(object):
    def __init__(self):
        pass
