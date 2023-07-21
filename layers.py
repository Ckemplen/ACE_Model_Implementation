"""
Sets out classes for each layer of the ACE model.

Layers:

- 1 Aspirational Layer: Mission, values, purpose, ethics, vision, morals
- 2 Global Strategy: Long term thinking, context, like a CEO
- 3 Agent Model: (Self) Capabilities, configuration, learning
- 4 Executive Function: Planning, forecasting, directives, resources
- 5 Cognitive Control: Task switching & selection, frustration, damping
- 6 Task Prosecution: One task at a time, detect success & failure

"""

import configparser
import queue


class CognitiveLayer:
    """
    Base class for all layers in the cognitive architecture model.
    """
    def __init__(self, name):
        """
        Initialize the CognitiveLayer.

        Args:
            name (str): The name of the layer.
        """
        self.name = name

        self.up_queue = queue.Queue()
        self.down_queue = queue.Queue()

        # Read the config file
        config = configparser.ConfigParser()
        config.read('config.ini')
        layer_config = config[self.name]

        # Set the layer-specific attributes dynamically based on the keys in the config section
        for key, value in layer_config.items():
            # Split on ', ' if the value is a list
            if ', ' in value:
                value = value.split(', ')
            setattr(self, key, value)

    def pass_up(self, data):
        """
        Pass data up to the layer above.

        Args:
            data: The data to pass up.
        """
        self.up_queue.put(data)

    def pass_down(self, data):
        """
        Pass data down to the layer below.

        Args:
            data: The data to pass down.
        """
        self.down_queue.put(data)

    def receive_from_above(self):
        """
        Receive data from the layer above.

        Returns:
            The data from the layer above, or None if the up_queue is empty.
        """
        if not self.up_queue.empty():
            return self.up_queue.get()
        return None

    def receive_from_below(self):
        """
        Receive data from the layer below.

        Returns:
            The data from the layer below, or None if the down_queue is empty.
        """
        if not self.down_queue.empty():
            return self.down_queue.get()
        return None

    def _validate_and_update(self, config_dict):
        """
        Validate and update the state changes.

        Args:
            config_dict (dict): A dictionary containing the state changes.
        """
        # Validate the config_dict to ensure it contains valid keys
        for key in config_dict:
            if not hasattr(self, key):
                raise ValueError(f"_validate_and_update: '{key}' is not a valid property of {self.__class__.__name__}.")

        # Set the class attributes dynamically based on the keys in config_dict
        for key, value in config_dict.items():
            setattr(self, key, value)

    def amend_state(self, config_dict):
        """
        Amend the state of the layer.

        Args:
            new_state (dict): A dictionary containing the new state of the layer.
        """
        # method to amend state at execution time by passing in a dictionary with new values
        if not isinstance(config_dict, dict):
            raise ValueError("amend_state: config_dict should be a dictionary.")

        self._validate_and_update(config_dict)

    def process_input(self, input_data):
        """
        Process the input data for the layer. This method should be implemented in each subclass.
        """
        raise NotImplementedError("Subclasses must implement process_input method.")

    def execute(self):
        """
        Execute actions for the layer. This method should be implemented in each subclass.
        """
        raise NotImplementedError("Subclasses must implement execute method.")





class AspirationalLayer(CognitiveLayer):
    """
    The Aspirational Layer in the cognitive architecture model.
    Represents the mission, values, purpose, ethics, vision, and morals of the system.
    """
    def __init__(self):
        """
        Initialize the AspirationalLayer.
        """
        super().__init__(name="AspirationalLayer")


    def process_input(self, input_data):
        # Processes information coming up or down the layers
        # Implement processing logic using the input data
        # For example, you might perform some analysis or decision-making here
        pass


    def execute(self):
        # Based on the processed data, execute relevant actions
        # For example, you might communicate the mission and values to other parts of the system
        print(f"Executing {self.name} - Mission: {self.mission}, Values: {self.values}")





class GlobalStrategyLayer(CognitiveLayer):
    def __init__(self):
        super().__init__(name="GlobalStrategyLayer")


    def process_input(self, input_data):

        pass

    def execute(self):

        pass



class AgentModelLayer(CognitiveLayer):
    def __init__(self):
        super().__init__(name="AgentModelLayer")


    def process_input(self, input_data):

        pass

    def execute(self):

        pass



class ExecutiveFunctionLayer(CognitiveLayer):
    def __init__(self):
        super().__init__(name="ExecutiveFunctionLayer")


    def process_input(self, input_data):

        pass

    def execute(self):

        pass



class CognitiveControlLayer(CognitiveLayer):

    def __init__(self):
        super().__init__(name="CognitiveControlLayer")


    def process_input(self, input_data):

        pass

    def execute(self):

        pass



class TaskProsecutionLayer(CognitiveLayer):
    def __init__(self):
        super().__init__(name="TaskProsecutionLayer")


    def process_input(self, input_data):

        pass

    def execute(self):

        pass

