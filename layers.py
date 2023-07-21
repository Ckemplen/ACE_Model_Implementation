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
    def __init__(self, name):
        self.name = name

        self.up_queue = queue.Queue()
        self.down_queue = queue.Queue()

    def pass_up(self, data):
        self.up_queue.put(data)

    def pass_down(self, data):
        self.down_queue.put(data)

    def receive_from_above(self):
        if not self.up_queue.empty():
            return self.up_queue.get()
        return None

    def receive_from_below(self):
        if not self.down_queue.empty():
            return self.down_queue.get()
        return None

    def _validate_and_update(self, config_dict):
        # Validate the config_dict to ensure it contains valid keys
        for key in config_dict:
            if not hasattr(self, key):
                raise ValueError(f"_validate_and_update: '{key}' is not a valid property of {self.__class__.__name__}.")

        # Set the class attributes dynamically based on the keys in config_dict
        for key, value in config_dict.items():
            setattr(self, key, value)

    def amend_state(self, config_dict):
        # method to amend state at execution time by passing in a dictionary with new values
        if not isinstance(config_dict, dict):
            raise ValueError("amend_state: config_dict should be a dictionary.")

        self._validate_and_update(config_dict)

    def set_up_callback(self, callback):
        self.up_callback = callback

    def set_down_callback(self, callback):
        self.down_callback = callback

    def pass_up(self, data):
        if hasattr(self, 'up_callback') and callable(self.up_callback):
            self.up_callback(data)

    def pass_down(self, data):
        if hasattr(self, 'down_callback') and callable(self.down_callback):
            self.down_callback(data)

    def process_input(self, input_data):
        raise NotImplementedError("Subclasses must implement process_input method.")

    def execute(self):
        raise NotImplementedError("Subclasses must implement execute method.")





class AspirationalLayer(CognitiveLayer):
    def __init__(self):
        super().__init__(name="Aspirational Layer")

        config = configparser.ConfigParser()
        config.read('config.ini')
        layer_config = config['AspirationalLayer']

        self.mission: str = layer_config.get('mission')
        self.values: list = layer_config.get('values').split(', ')


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
        super().__init__(name="Global Strategy Layer")

        config = configparser.ConfigParser()
        config.read('config.ini')
        layer_config = config['GlobalStrategyLayer']

        self.long_term_goals: list = layer_config.get('long_term_goals').split(', ')
        self.context: list = layer_config.get('context').split(', ')

    def process_input(self, input_data):

        pass

    def execute(self):

        pass



class AgentModelLayer(CognitiveLayer):
    def __init__(self):
        super().__init__(name="Agent Model Layer")

        config = configparser.ConfigParser()
        config.read('config.ini')
        layer_config = config['AgentModelLayer']

        self.capabilities: list = layer_config.get('capabilities').split(', ')
        self.learning_methods: list = layer_config.get('learning_methods').split(', ')

    def process_input(self, input_data):

        pass

    def execute(self):

        pass



class ExecutiveFunctionLayer(CognitiveLayer):
    def __init__(self):
        super().__init__(name="Executive Function Layer")

        config = configparser.ConfigParser()
        config.read('config.ini')
        layer_config = config['ExecutiveFunctionLayer']

        self.planning_data: list = layer_config.get('planning_data').split(', ')
        self.forecasting_models: list = layer_config.get('forecasting_models').split(', ')

    def process_input(self, input_data):

        pass

    def execute(self):

        pass



class CognitiveControlLayer(CognitiveLayer):

    def __init__(self):
        super().__init__(name="Cognitive Control Layer")

        config = configparser.ConfigParser()
        config.read('config.ini')
        layer_config = config['CognitiveControlLayer']

        self.long_term_goals: list = layer_config.get('task_switching_mechanisms').split(', ')
        self.context: int = layer_config.get('frustration_threshold')

    def process_input(self, input_data):

        pass

    def execute(self):

        pass



class TaskProsecutionLayer(CognitiveLayer):
    def __init__(self):
        super().__init__(name="Task Prosecution Layer")

        config = configparser.ConfigParser()
        config.read('config.ini')
        layer_config = config['TaskProsecutionLayer']

        self.current_task: str = layer_config.get('current_task')
        self.success_detection: list = layer_config.get('success_detection').split(', ')

    def process_input(self, input_data):

        pass

    def execute(self):

        pass

