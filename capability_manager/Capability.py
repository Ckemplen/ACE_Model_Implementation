import logging
import pathlib

project_root = pathlib.Path(__file__).parent.parent.resolve()
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
        self.logger = logging.getLogger(name)  # Create a logger for this layer
        self.logger.setLevel(logging.DEBUG)  # Set the logging level

        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create a file handler
        fh = logging.FileHandler(f'{project_root}application.log')
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

    def execute(self):
        """
        Execute the capability.
        This method should be overridden by subclasses to provide the specific execution logic.
        """
        raise NotImplementedError("Subclasses should implement this method.")