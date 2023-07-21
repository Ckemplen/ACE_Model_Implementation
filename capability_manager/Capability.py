class Capability:
    """
    Base class for all capabilities.
    """

    def __init__(self, name):
        """
        Initialize the Capability.

        Args:
            name (str): The name of the capability.
        """
        self.name = name

    def execute(self):
        """
        Execute the capability.
        This method should be overridden by subclasses to provide the specific execution logic.
        """
        raise NotImplementedError("Subclasses should implement this method.")