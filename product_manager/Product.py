import logging
import pathlib

project_root = pathlib.Path(__file__).parent.parent.resolve()
from utils.logging import setup_logger

class Product:
    """
    Base class for all products.
    """

    def __init__(self, name, description, required_resources=None, required_capabilities=None):
        """
        Initialize the Product.

        Args:
            name (str): The name of the product.
            required_resources (list): The resources required to create the product.
            required_capabilities (list): The capabilities required to create the product.
        """
        self.name = name
        self.description = description
        self.required_resources = required_resources if required_resources else []
        self.required_capabilities = required_capabilities if required_capabilities else []

        # storage allocated for the product class to make it
        # easier to organise and track data stored by and for products.
        self.storage_root = f"{project_root}/storage/products/{self.name}"

        # Set up logging
        self.logger = setup_logger(name)

    def draft(self):
        """
        Draft the product.
        This method should be overridden by subclasses to provide the specific drafting logic.

        Higher layers of the model unlikely to be involved in drafting.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def review(self):
        """
        Review the product.
        This method should be overridden by subclasses to provide the specific review logic.


        """
        raise NotImplementedError("Subclasses should implement this method.")

    def complete(self):
        """
        Complete the product.
        This method should be overridden by subclasses to provide the specific completion logic.

        Perhaps each layer could have their own approach to each method.

        Potentially reserve complete function for higher layers of the layer hierarchy.

        Lower levels of the model unlikely to be involved in sign-off / completion.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def export(self):
        """
        Export the product.
        This method should be overridden by subclasses to provide the specific export logic.
        """
        raise NotImplementedError("Subclasses should implement this method.")
