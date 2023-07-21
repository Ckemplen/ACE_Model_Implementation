class Resource:
    """
    Base class for all resources.
    """

    def __init__(self, name, capacity):
        """
        Initialize the Resource.

        Args:
            name (str): The name of the resource.
            capacity (int): The total capacity of the resource.
        """
        self.name = name
        self.capacity = capacity
        self.used = 0

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
