"""
Sets out classes for each layer of the Autonomous Cognitive Entity (ACE) model.

The ACE model is inspired by the OSI model to present layers of abstraction by which you can think about artificial
cognitive architectures. The primary purpose of the ACE model is to provide a framework for thinking about
autonomous, agentic systems.

Layers:

- 1 Aspirational Layer: Mission, values, purpose, ethics, vision, morals
- 2 Global Strategy: Long term thinking, context, like a CEO
- 3 Agent Model: (Self) Capabilities, configuration, learning
- 4 Executive Function: Planning, forecasting, directives, resources
- 5 Cognitive Control: Task switching & selection, frustration, damping
- 6 Task Prosecution: One task at a time, detect success & failure

ACE model is a creation of Dave Shapiro: https://github.com/daveshap/Benevolent_AGI
This implementation is authored by Chris Kemplen: https://github.com/Ckemplen/ACE_Model_Implementation/
"""

import configparser
import logging
import queue
import pathlib

from reasoning_engines.GPTModels import GPTModel
from capability_manager import CapabilityManager
from resource_manager import ResourceManager
from product_manager import ProductManager

project_root = pathlib.Path(__file__).parent.parent.resolve()

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

        self.capabilities = CapabilityManager(creator=self.name)  # store the capabilities of the layer
        self.resources = ResourceManager(creator=self.name)  # store the resources available to the layer
        self.products = ProductManager(creator=self.name) # store the products of the layer

        self.total_tokens: int = 0
        self.total_cost: float = 0

        # Set up logging
        self.logger = logging.getLogger(name)  # Create a logger for this layer
        self.logger.setLevel(logging.DEBUG)  # Set the logging level

        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create a file handler
        fh = logging.FileHandler(f'{project_root}/application.log')
        fh.setLevel(logging.DEBUG)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Add the formatter to the console handler
        ch.setFormatter(formatter)

        # Add the formatter to the file handler
        fh.setFormatter(formatter)

        # Add the console handler to the logger
        self.logger.addHandler(ch)

        # Add the file handler to the logger
        self.logger.addHandler(fh)

    def pass_up(self, data):
        """
        Pass data up to the layer above.

        Args:
            data: The data to pass up.
        """
        self.logger.debug(f"Passed up data: {data}")
        self.up_queue.put(data)

    def pass_down(self, data):
        """
        Pass data down to the layer below.

        Args:
            data: The data to pass down.
        """
        self.logger.debug(f"Passed down data: {data}")
        self.down_queue.put(data)

    def receive_from_above(self):
        """
        Receive data from the layer above.

        Returns:
            The data from the layer above, or None if the up_queue is empty.
        """
        if not self.up_queue.empty():
            self.logger.debug(f"Received from above: {self.up_queue.get}")
            return self.up_queue.get()
        return None

    def receive_from_below(self):
        """
        Receive data from the layer below.

        Returns:
            The data from the layer below, or None if the down_queue is empty.
        """
        if not self.down_queue.empty():
            self.logger.debug(f"Received from below: {self.down_queue.get}")
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
                self.logger.error(f"Invaid config data passed in: {config_dict}")
                raise ValueError(f"_validate_and_update: '{key}' is not a valid property of {self.__class__.__name__}.")

        # Set the class attributes dynamically based on the keys in config_dict
        for key, value in config_dict.items():
            self.logger.debug(f"Attribute added/updated: {key}: {value}")
            setattr(self, key, value)

    def amend_state(self, config_dict):
        """
        Amend the state of the layer.

        Args:
            new_state (dict): A dictionary containing the new state of the layer.
        """
        # method to amend state at execution time by passing in a dictionary with new values
        if not isinstance(config_dict, dict):
            self.logger.error(f"Invalid object passed to amend state: {config_dict}")
            raise ValueError("amend_state: config_dict should be a dictionary.")

        self._validate_and_update(config_dict)

    def process_input(self, input_data):
        """
        Process the input data for the layer. This method should be implemented in each subclass.
        Run all the various workflow chains etc. and prepare everything necessary for self.execute() to come next
        Part of highest level common interface, encapsulates all processing logic that is bespoke to each layer.
        """
        raise NotImplementedError("Subclasses must implement process_input method.")

    def execute(self):
        """
        Execute actions for the layer. This method should be implemented in each subclass.
        Does something with the work processed and prepared via process input.
        Part of highest level common interface, encapsulates all execution logic that is bespoke to each layer.
        """
        raise NotImplementedError("Subclasses must implement execute method.")


    def review_resouces(self):
        """
        Review the resources the layer has access to and judge if any other resources required for current mission.
        """

        raise NotImplementedError("Subclasses must implement review_resources method.")

    def review_capabilities(self):
        """
        Review the capabilities the layer has access to and judge if any other capabilities required for current mission.
        """

        raise NotImplementedError("Subclasses must implement review_capabilities method.")

    def review_products(self):
        """
        Review the products the layer is working on / has produced / is passed by other layers.
        """

        raise NotImplementedError("Subclasses must implement review_products method.")

    def request_resources(self):
        """
        Requests any resources needed for the task at  hand.
        """

        raise NotImplementedError("Subclasses must implement request_resources method.")

    def request_capabilities(self):
        """
        Requests any capabilities needed for the task at hand.
        """

        raise NotImplementedError("Subclasses must implement request_capabilities method.")

    def request_products(self):
        """
        Request the products required to move forward with the mission.
        """

        raise NotImplementedError("Subclasses must implement request_products method.")

    def create_resource(self):
        """
        Creates a new or expanded resource.
        """

        raise NotImplementedError("Subclasses must implement create_resource method.")

    def create_capability(self):
        """
        Creates a new or expanded capability.
        """

        raise NotImplementedError("Subclasses must implement create_capability method.")

    def create_product(self):
        """
        Creates a new or expanded product.
        """

        raise NotImplementedError("Subclasses must implement create_product method.")

