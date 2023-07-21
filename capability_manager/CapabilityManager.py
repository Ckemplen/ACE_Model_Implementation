from .Capability import Capability

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
