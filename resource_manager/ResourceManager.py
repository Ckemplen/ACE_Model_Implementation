import os
import inspect

from .Resource import Resource

class ResourceManager:
    """
    Class to manage resources.
    """

    def __init__(self, creator):
        """
        Initialize the ResourceManager.
        """
        self.resources = {}  # Dictionary to store the resources
        self.creator = creator

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

    def create_resource_class(self, name, description, capacity=0, used=0, budget=0):
        """
        Dynamically create a new resource class.

        Args:
            name (str): The name of the new resource class.
            description (str): The description of the new resource class.
            capacity (int): The total capacity of the new resource class.
            used (int): The amount of the new resource class currently in use.
            budget (float): The budget of the new resource class.

        Returns:
            type: The new resource class.
        """
        return type(name, (Resource,), {
            "__init__": lambda self: Resource.__init__(self, name, description, capacity, used, budget)
        })

    def create_and_save_resource_class(self, name, description, capacity=0, used=0, budget=0, required_imports=None):
        """
        Dynamically create a new resource class and save it to a Python file in the 'dynamically_created_resources' module.

        Args:
            name (str): The name of the new resource class.
            description (str): The description of the new resource class.
            capacity (int): The total capacity of the new resource class.
            used (int): The amount of the new resource class currently in use.
            budget (float): The budget of the new resource class.
            required_imports (str): The required import statements for the new resource class.
        """
        # Create the new resource class
        new_class = self.create_resource_class(name, description, capacity, used, budget)
        new_class.is_built_in = False  # Add a property to indicate that this is not a built-in class

        # Generate the Python code for the new class
        class_code = inspect.getsource(new_class)

        # Define the necessary import statements
        import_code = (required_imports + "\n"
                                          "from resource_manager.Resource import Resource\n")

        # Combine the import statements and the class code
        code = import_code + class_code

        # Define the module directory
        module = "resource_manager/dynamically_created_resources"

        # Create the module directory if it does not exist
        if not os.path.exists(module):
            os.makedirs(module)

        # Determine a unique file name
        filename = os.path.join(module, f"{name}Resource.py")
        i = 1
        while os.path.exists(filename):
            filename = os.path.join(module, f"{name}V{i}Resource.py")
            i += 1
