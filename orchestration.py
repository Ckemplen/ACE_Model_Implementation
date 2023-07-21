"""
Brings together the various layers to act in concert.

Layers:

- 1 Aspirational Layer: Mission, values, purpose, ethics, vision, morals
- 2 Global Strategy: Long term thinking, context, like a CEO
- 3 Agent Model: (Self) Capabilities, configuration, learning
- 4 Executive Function: Planning, forecasting, directives, resources
- 5 Cognitive Control: Task switching & selection, frustration, damping
- 6 Task Prosecution: One task at a time, detect success & failure

"""

from enum import Enum

from layers import (AspirationalLayer, GlobalStrategyLayer, AgentModelLayer, ExecutiveFunctionLayer,
                    CognitiveControlLayer, TaskProsecutionLayer)


class LayerHierarchy(Enum):
    ASPIRATIONAL = 1
    GLOBAL_STRATEGY = 2
    AGENT_MODEL = 3
    EXECUTIVE_FUNCTION = 4
    COGNITIVE_CONTROL = 5
    TASK_PROSECUTION = 6


class CognitiveArchitecture:
    def __init__(self):
        # Instantiate layers
        self.aspirational_layer = AspirationalLayer()
        self.global_strategy_layer = GlobalStrategyLayer()
        self.agent_model_layer = AgentModelLayer()
        self.executive_function_layer = ExecutiveFunctionLayer()
        self.cognitive_control_layer = CognitiveControlLayer()
        self.task_prosecution_layer = TaskProsecutionLayer()

        # Set up callbacks or input/output queues between layers
        for layer in [self.aspirational_layer, self.global_strategy_layer, self.agent_model_layer,
                      self.executive_function_layer, self.cognitive_control_layer, self.task_prosecution_layer]:
            layer.set_down_callback(self.global_strategy_layer.process_input)

    def process_input(self, input_data):
        # Implement how the input data flows through the layers
        # e.g., layer_output = self.aspirational_layer.process_input(input_data)
        pass

    def execute(self):
        # Implement how execution happens across the layers
        # e.g., self.global_strategy_layer.execute()
        pass

    def pass_up(self, layer_hierarchy: LayerHierarchy, data):
        layer = self.get_layer_by_hierarchy(layer_hierarchy)
        layer.pass_up(data)

    def pass_down(self, layer_hierarchy: LayerHierarchy, data):
        layer = self.get_layer_by_hierarchy(layer_hierarchy)
        layer.pass_down(data)

    def get_layer_by_hierarchy(self, hierarchy: LayerHierarchy):
        if hierarchy == LayerHierarchy.ASPIRATIONAL:
            return self.aspirational_layer
        elif hierarchy == LayerHierarchy.GLOBAL_STRATEGY:
            return self.global_strategy_layer
        elif hierarchy == LayerHierarchy.AGENT_MODEL:
            return self.agent_model_layer
        elif hierarchy == LayerHierarchy.EXECUTIVE_FUNCTION:
            return self.executive_function_layer
        elif hierarchy == LayerHierarchy.COGNITIVE_CONTROL:
            return self.cognitive_control_layer
        elif hierarchy == LayerHierarchy.TASK_PROSECUTION:
            return self.task_prosecution_layer
        else:
            raise ValueError("Invalid Layer Hierarchy.")
