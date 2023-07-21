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

import threading
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
    """
    Represents the entire cognitive architecture model.
    Contains all layers of the model and manages data flow and execution across layers.
    """
    def __init__(self):
        """
        Initialize the CognitiveArchitecture.
        """
        # Instantiate layers
        self.aspirational_layer = AspirationalLayer()
        self.global_strategy_layer = GlobalStrategyLayer()
        self.agent_model_layer = AgentModelLayer()
        self.executive_function_layer = ExecutiveFunctionLayer()
        self.cognitive_control_layer = CognitiveControlLayer()
        self.task_prosecution_layer = TaskProsecutionLayer()

        # Set up input/output queues between layers
        self.aspirational_layer.down_queue = self.global_strategy_layer.up_queue
        self.global_strategy_layer.up_queue = self.aspirational_layer.down_queue
        self.global_strategy_layer.down_queue = self.agent_model_layer.up_queue
        self.agent_model_layer.up_queue = self.global_strategy_layer.down_queue
        self.agent_model_layer.down_queue = self.executive_function_layer.up_queue
        self.executive_function_layer.up_queue = self.agent_model_layer.down_queue
        self.executive_function_layer.down_queue = self.cognitive_control_layer.up_queue
        self.cognitive_control_layer.up_queue = self.executive_function_layer.down_queue
        self.cognitive_control_layer.down_queue = self.task_prosecution_layer.up_queue
        self.task_prosecution_layer.up_queue = self.cognitive_control_layer.down_queue

        self.threads = {}

    def _check_thread_status(self):
        """
        Check the status of all threads.
        """
        # Method to aid debug by checking on status of all threads
        for key, thread in self.threads:
            print(f'{key}: running={thread.running()}, done={thread.done()}')

    def start_execution(self):
        """
        Start the execution of all layers in separate threads.
        """
        # Create a thread for each layer
        aspirational_thread = threading.Thread(target=self.aspirational_layer.main_loop)
        self.threads[LayerHierarchy.ASPIRATIONAL] = aspirational_thread

        global_strategy_thread = threading.Thread(target=self.global_strategy_layer.main_loop)
        self.threads[LayerHierarchy.GLOBAL_STRATEGY] = global_strategy_thread

        agent_model_thread = threading.Thread(target=self.agent_model_layer.main_loop)
        self.threads[LayerHierarchy.AGENT_MODEL] = agent_model_thread

        executive_function_thread = threading.Thread(target=self.executive_function_layer.main_loop)
        self.threads[LayerHierarchy.EXECUTIVE_FUNCTION] = executive_function_thread

        cognitive_control_thread = threading.Thread(target=self.cognitive_control_layer.main_loop)
        self.threads[LayerHierarchy.COGNITIVE_CONTROL] = cognitive_control_thread

        task_prosecution_thread = threading.Thread(target=self.task_prosecution_layer.main_loop)
        self.threads[LayerHierarchy.TASK_PROSECUTION] = task_prosecution_thread


        # Start all threads
        aspirational_thread.start()
        global_strategy_thread.start()
        agent_model_thread.start()
        executive_function_thread.start()
        cognitive_control_thread.start()
        task_prosecution_thread.start()

        # Wait for all threads to finish
        aspirational_thread.join()
        global_strategy_thread.join()
        agent_model_thread.join()
        executive_function_thread.join()
        cognitive_control_thread.join()
        task_prosecution_thread.join()


    def process_input(self, input_data):
        """
        Process input data at a specific layer.

        Args:
            layer_hierarchy (LayerHierarchy): The hierarchy of the layer to process the input data.
            input_data: The input data to be processed.
        """
        # Implement how the input data flows through the layers
        # e.g.,
        pass

    def execute(self):
        """
        Execute actions at a specific layer.

        Args:
            layer_hierarchy (LayerHierarchy): The hierarchy of the layer to execute actions.
        """
        # Implement how execution happens across the layers
        # e.g.,
        pass

    def pass_up(self, layer_hierarchy: LayerHierarchy, data):
        """
        Pass data up to a specific layer.

        Args:
            layer_hierarchy (LayerHierarchy): The hierarchy of the layer to pass data up to.
            data: The data to pass up.
        """
        layer = self.get_layer_by_hierarchy(layer_hierarchy)
        layer.pass_up(data)

    def pass_down(self, layer_hierarchy: LayerHierarchy, data):
        """
        Pass data down to a specific layer.

        Args:
            layer_hierarchy (LayerHierarchy): The hierarchy of the layer to pass data down to.
            data: The data to pass down.
        """
        layer = self.get_layer_by_hierarchy(layer_hierarchy)
        layer.pass_down(data)

    def get_layer_by_hierarchy(self, hierarchy: LayerHierarchy):
        """
        Get a layer by its hierarchy.

        Args:
            layer_hierarchy (LayerHierarchy): The hierarchy of the layer to get.

        Returns:
            The layer with the specified hierarchy.
        """
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
