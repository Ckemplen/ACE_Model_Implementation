import os
import inspect

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

    def create_capability_class(self, name, description):
        """
        Dynamically create a new capability class.

        Args:
            name (str): The name of the new capability class.
            description (str): The description of the new capability class.

        Returns:
            type: The new capability class.
        """
        return type(name, (Capability,), {
            "__init__": lambda self: Capability.__init__(self, name, description)
        })

    def create_and_save_capability_class(self, name, description, required_imports=None):
        """
        Dynamically create a new capability class and save it to a Python file in the 'dynamically_created_capabilities' module.

        Args:
            name (str): The name of the new capability class.
            description (str): The description of the new capability class.
            required_imports (str): The required import statements for the new capability class.
        """
        # Create the new capability class
        new_class = self.create_capability_class(name, description)
        new_class.is_built_in = False  # Add a property to indicate that this is not a built-in class

        # Generate the Python code for the new class
        class_code = inspect.getsource(new_class)

        # Define the necessary import statements
        import_code = (required_imports + "\n"
                                          "from capability_manager.Capability import Capability\n")

        # Combine the import statements and the class code
        code = import_code + class_code

        # Define the module directory
        module = "capability_manager/dynamically_created_capabilities"

        # Create the module directory if it does not exist
        if not os.path.exists(module):
            os.makedirs(module)

        # Determine a unique file name
        filename = os.path.join(module, f"{name}Capability.py")
        i = 1
        while os.path.exists(filename):
            filename = os.path.join(module, f"{name}V{i}Capability.py")
            i += 1

        # Write the code to the file
        with open(filename, "w") as file:
            file.write(code)
