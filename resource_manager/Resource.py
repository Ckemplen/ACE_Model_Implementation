import logging
class Resource:
    """
    Base class for all resources.
    """

    def __init__(self, name, description, capacity=0, used=0, budget=0):
        """
        Initialize the Resource.

        Args:
            name (str): The name of the resource.
            capacity (int): The total capacity of the resource.
        """
        self.name = name
        self.description: str = description # mandatory brief description, should be set when child class is created
        self.capacity = capacity # optional as may well not apply to many resources, default to 0
        self.used = used # optional as may or may not be relevant, defaults to 0
        self.budget: float = budget # refers to currency so is optional as may not apply to all resources, default to 0

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

    def use(self, amount):
        """
        Use a certain amount of the resource.

        Args:
            amount (int): The amount of the resource to use.
        """
        if self.used + amount > self.capacity:
            raise ValueError("Not enough capacity to use the requested amount.")
        self.used += amount

    def release(self, amount):
        """
        Release a certain amount of the resource.

        Args:
            amount (int): The amount of the resource to release.
        """
        if self.used - amount < 0:
            raise ValueError("Cannot release more than the used amount.")
        self.used -= amount

    def get_remaining(self):
        """
        Get the remaining amount of the resource.

        Returns:
            int: The remaining amount of the resource.
        """
        return self.capacity - self.used

