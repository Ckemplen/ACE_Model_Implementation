import logging

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

        # Set up logging
        self.logger = logging.getLogger(name)  # Create a logger for this layer
        self.logger.setLevel(logging.DEBUG)  # Set the logging level

        # Create a console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create a file handler
        fh = logging.FileHandler('application.log')
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
