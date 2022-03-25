from resource import ResourceRequest

# Has "needs" (represented by ResourceRequests) and can optionally produce Labor.
class Agent(object):
    def __init__(self, system):
        self.system = system
        self.daily_labor = 8
        self.create_needs()

    def create_needs(self):
        self.needs = []

    def consume_daily_needs(self):
        # are these resources consumed directly from the resource pool, or via an associated ResourceRequest?
        # maybe simpler to do directly
        # but are all resources the result of ResourceRequests? like is the system making food no matter what?
        # probably not
        # so... do things just schedule resource requests for the next 30 steps or something?
        pass

    def contibute_daily_resources(self):
        pass

    def schedule_future_needs(self):
        pass

    def add_resources(self):
        pass
    
    def step(self):
        self.system.resource_pool.add("labor", self.daily_labor)
        
