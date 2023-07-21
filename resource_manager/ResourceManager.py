from .Resource import Resource

class ResourceManager:
    """
    Class to manage resources.
    """

    def __init__(self):
        """
        Initialize the ResourceManager.
        """
        self.resources = {}  # Dictionary to store the resources

    def add_resource(self, name, resource):
        """
        Add a new resource.

        Args:
            name (str): The name of the resource.
            resource (object): The resource object.
        """
        self.resources[name] = resource

    def remove_resource(self, name):
        """
        Remove a resource.

        Args:
            name (str): The name of the resource.
        """
        if name in self.resources:
            del self.resources[name]

    def get_resource(self, name):
        """
        Get a resource.

        Args:
            name (str): The name of the resource.

        Returns:
            The resource object, or None if it doesn't exist.
        """
        return self.resources.get(name, None)
