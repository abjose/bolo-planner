from typing import List
from utils import Timespan


# Something that can be consumed by Agents or ResourceTransformers.
class Resource(object):
    def __init__(self, name: str):
        self.name = name
        self.creation_time = None
        self.usage_window = None  # Timespan
        self.require_whole_units = False  # whether can be divided into partial units

    # Name must be unique.
    def __hash__(self):
        return hash(self.name)


# Optionally time-bounded request for a particular Resource.
class ResourceRequest(object):
    def __init__(self):
        self.creation_time = None
        self.fulfillment_window = None  # Timespan


# Collection of available Resources.
class ResourcePool(object):
    def __init__(self):
        self.current_resources = {}

    def deduct_existing_resources(self, resource_dict):
        pass


# An "edge" in the resource graph - consumes input resources and produces output resources.
class ResourceTransformer(object):
    def __init__(self):
        self.name = ""

        # TODO: need to specify quantities.
        self.input_resources = dict()
        self.output_resources = dict()

        # Time delay between input and output.
        self.delay = 0

    # Produce an appropriate amount of output resources.
    # Should it take/put directly into ResourcePool?
    def transform(self):
        pass


# TODO: move resources to a config / seed file
def make_resources(names: List[str]):
    return [Resource(name) for name in names]

# 1 unit of labor meant to represent 1 hour of labor

resources = make_resources([
    "water",
    "time", "labor",  # ???
    "tree", "wood",
    "carrot", "potato",
    "chair",
])
