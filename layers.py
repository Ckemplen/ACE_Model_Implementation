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
from GPTModels import GPTModel

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

        self.GPTModel = GPTModel()

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
    Responsible for the mission, values, purpose, ethics, vision, and morals of the system.
    """
    def __init__(self):
        """
        Initialize the AspirationalLayer.
        """
        super().__init__(name="AspirationalLayer")
        self.mission = None
        self.values = None

    def process_input(self, input_data):
        # Some other action specific to this layer
        processed_data = self.GPTModel.process(input_data)
        return processed_data


    def execute(self):
        # Based on the processed data, execute relevant actions
        # For example, you might communicate the mission and values to other parts of the system

        try:
            self.process_input("something")

            self.evaluate_action("something")

            # Execute an action using the GPT model
            result = self.GPTModel.execute("something")

            return result

        except Exception as e:
            self.pass_up(f"Error: {str(e)}")


    def evaluate_action(self, action):
        # Evaluate a proposed action against the system's mission and values
        return True  # Placeholder

    def pass_down_request(self, request):
        self.pass_down(request)

    def receive_response_from_below(self):
        response = self.receive_from_below()
        if response:
            print(f"Received response from below: {response}")
            # Handle the response





class GlobalStrategyLayer(CognitiveLayer):
    """
    The Global Strategy Layer in the cognitive architecture model.
    Responsible for long term thinking and wider context for the system.
    Acts like a CEO.
    """
    def __init__(self):
        super().__init__(name="GlobalStrategyLayer")
        self.strategy = None
        self.goals = None

    def process_input(self, input_data):
        # Some other action specific to this layer
        processed_data = self.GPTModel.process(input_data)
        return processed_data

    def execute(self):
        self.process_input("something")

        self.update_strategy("something")

        self.generate_plan("something")

        # Execute an action using the GPT model
        result = self.GPTModel.execute("something")

        return result

    def update_strategy(self, feedback):
        # Update the strategy based on feedback
        pass  # Placeholder

    def generate_plan(self):
        # Generate a high-level strategic plan
        return {}  # Placeholder

    def pass_up_strategy(self):
        strategy = self.get_strategy()
        self.pass_up(strategy)

    def receive_feedback_from_above(self):
        feedback = self.receive_from_above()
        if feedback:
            print(f"Received feedback from above: {feedback}")
            # Update strategy based on feedback

    def pass_down_request(self, request):
        self.pass_down(request)

    def receive_response_from_below(self):
        response = self.receive_from_below()
        if response:
            print(f"Received response from below: {response}")
            # Handle the response


class AgentModelLayer(CognitiveLayer):
    """
    The Agent Model Layer in the cognitive architecture model.
    Responsible for understanding self capabilities, managing configuration and learning.
    Acts like the ego of the system.
    """
    def __init__(self):
        super().__init__(name="AgentModelLayer")
        self.beliefs = {}  # A dictionary to hold the system's beliefs about other agents



    def process_input(self, input_data):
        # Some other action specific to this layer
        processed_data = self.GPTModel.process(input_data)
        return processed_data

    def execute(self):
        self.process_input("something")

        self.update_beliefs("something")

        self.predict_action("something")

        # Execute an action using the GPT model
        result = self.GPTModel.execute("something")

        return result

    def update_beliefs(self, new_information):
        # Update the beliefs based on new information
        pass  # Placeholder

    def predict_action(self, agent):
        # Predict the action of another agent
        return None  # Placeholder

    def pass_up_beliefs(self):
        beliefs = self.get_beliefs()
        self.pass_up(beliefs)

    def receive_feedback_from_above(self):
        feedback = self.receive_from_above()
        if feedback:
            print(f"Received feedback from above: {feedback}")
            # Update beliefs based on feedback

    def pass_down_request(self, request):
        self.pass_down(request)

    def receive_response_from_below(self):
        response = self.receive_from_below()
        if response:
            print(f"Received response from below: {response}")
            # Handle the response



class ExecutiveFunctionLayer(CognitiveLayer):
    """
    The Executive Function Layer in the cognitive architecture model.
    Responsible for managing planning, forecasting, directives and resources.
    Acts like a Project Manager.
    """
    def __init__(self):
        super().__init__(name="ExecutiveFunctionLayer")
        self.resources = None  # A representation of available resources
        self.actions = []  # A list of ongoing actions


    def process_input(self, input_data):
        # Some other action specific to this layer
        processed_data = self.GPTModel.process(input_data)
        return processed_data

    def execute(self):
        self.process_input("something")

        self.initiate_action("something")

        self.monitor_progress("something")

        # Execute an action using the GPT model
        result = self.GPTModel.execute("something")

        return result

    def initiate_action(self, action):
        # Initiate a new action
        pass  # Placeholder

    def monitor_progress(self):
        # Monitor the progress of ongoing actions
        return {}  # Placeholder

    def pass_up_status(self):
        status = self.get_status()
        self.pass_up(status)

    def receive_feedback_from_above(self):
        feedback = self.receive_from_above()
        if feedback:
            print(f"Received feedback from above: {feedback}")
            # Update status based on feedback

    def pass_down_request(self, request):
        self.pass_down(request)

    def receive_response_from_below(self):
        response = self.receive_from_below()
        if response:
            print(f"Received response from below: {response}")
            # Handle the response



class CognitiveControlLayer(CognitiveLayer):
    """
    The Cognitive Control Layer in the cognitive architecture model.
    Responsible for task switching & selection, frustration, and damping.
    Acts like a team leader for a small operational team.
    """

    def __init__(self):
        super().__init__(name="CognitiveControlLayer")
        self.control_flow_state = None  # The current control flow state

    def process_input(self, input_data):
        # Some other action specific to this layer
        processed_data = self.GPTModel.process(input_data)
        return processed_data

    def execute(self):
        self.process_input("something")

        self.make_decision("something")

        self.update_control_flow("something")

        # Execute an action using the GPT model
        result = self.GPTModel.execute("something")

        return result

    def make_decision(self, input_data):
        # Make a decision based on input data
        return None  # Placeholder

    def update_control_flow(self, decision):
        # Update the control flow state based on a decision
        pass  # Placeholder

    def pass_up_decision(self, decision):
        self.pass_up(decision)

    def receive_feedback_from_above(self):
        feedback = self.receive_from_above()
        if feedback:
            print(f"Received feedback from above: {feedback}")
            # Update decision-making parameters based on feedback

    def pass_down_request(self, request):
        self.pass_down(request)

    def receive_response_from_below(self):
        response = self.receive_from_below()
        if response:
            print(f"Received response from below: {response}")
            # Handle the response


class TaskProsecutionLayer(CognitiveLayer):
    """
    The Task Prosecution Layer in the cognitive architecture model.
    Responsible for taking one task at a time, detecting success & failure.
    Acts as an individual team contributor.
    """
    def __init__(self):
        super().__init__(name="TaskProsecutionLayer")


    def process_input(self, input_data):
        # Some other action specific to this layer
        processed_data = self.GPTModel.process(input_data)
        return processed_data

    def execute(self):

        try:
            self.process_input("something")

            self.initiate_task("something")

            self.monitor_tasks("something")

            # Execute an action using the GPT model
            result = self.GPTModel.execute("something")

            return result
        except Exception as e:
            self.pass_up(f"Error: {str(e)}")


    def initiate_task(self, task):
        # Initiate a new task
        pass  # Placeholder

    def monitor_tasks(self):
        # Monitor the progress of ongoing tasks
        return {}  # Placeholder

    class TaskProsecutionLayer(CognitiveLayer):
        # Existing code...

        def pass_up_status(self):
            status = self.get_status()
            self.pass_up(status)

        def receive_request_from_above(self):
            request = self.receive_from_above()
            if request:
                print(f"Received request from above: {request}")
                # Execute the requested action and send a response
                response = self.execute(request)
                self.pass_up(response)