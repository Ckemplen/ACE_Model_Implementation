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


class CapabilityManager:
    """
    Class to manage capabilities.
    """

    def __init__(self):
        """
        Initialize the CapabilityManager.
        """
        self.capabilities = {}  # Dictionary to store the capabilities

    def add_capability(self, name, capability: Capability):
        """
        Add a new capability.

        Args:
            name (str): The name of the capability.
            capability (object): The capability object.
        """
        self.capabilities[name] = capability

    def remove_capability(self, name):
        """
        Remove a capability.

        Args:
            name (str): The name of the capability.
        """
        if name in self.capabilities:
            del self.capabilities[name]

    def get_capability(self, name):
        """
        Get a capability.

        Args:
            name (str): The name of the capability.

        Returns:
            The capability object, or None if it doesn't exist.
        """
        return self.capabilities.get(name, None)
