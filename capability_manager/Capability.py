import logging
import pathlib

project_root = pathlib.Path(__file__).parent.parent.resolve()
from utils.logging import setup_logger
class Capability:
    """
    Base class for all capabilities.
    """

    def __init__(self, name, description):
        """
        Initialize the Capability.

        Args:
            name (str): The name of the capability.
        """
        self.name = name
        self.description = description

        # storage allocated for the capabilities class to make it
        # easier to organise and track data stored by and for capabilities.
        self.storage_root = f"{project_root}/storage/capabilities/{self.name}"

        # Set up logging
        self.logger = setup_logger(name)

    def execute(self):
        """
        Execute the capability.
        This method should be overridden by subclasses to provide the specific execution logic.
        """
        raise NotImplementedError("Subclasses should implement this method.")