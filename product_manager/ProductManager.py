import os
import inspect

from .Product import Product


class ProductManager:
    """
    Class to manage products.
    """

    def __init__(self, creator):
        """
        Initialize the ProductManager.
        """
        self.products = {}  # Dictionary to store the products
        self.creator = creator

    def add_product(self, name, product: Product):
        """
        Add a new product.

        Args:
            name (str): The name of the product.
            product (Product): The product object.
        """
        self.products[name] = product

    def remove_product(self, name):
        """
        Remove a product.

        Args:
            name (str): The name of the product.
        """
        if name in self.products:
            del self.products[name]

    def get_product(self, name):
        """
        Get a product.

        Args:
            name (str): The name of the product.

        Returns:
            Product: The product object, or None if it doesn't exist.
        """
        return self.products.get(name, None)

    def execute_product(self, name):
        """
        Execute a product.

        Args:
            name (str): The name of the product.

        Returns:
            The output of the product execution, or None if the product doesn't exist or if required resources/capabilities are not available.
        """
        product = self.get_product(name)
        if product is None:
            return None

        # Check if required resources and capabilities are available
        # If they are, execute the product and return the output
        # If they are not, return None or raise an exception

        return product.execute()

    def create_product_class(self, name, description, required_resources=None, required_capabilities=None):
        """
        Dynamically create a new product class.

        Args:
            name (str): The name of the new product class.
            required_resources (list): The resources required for the new product class.
            required_capabilities (list): The capabilities required for the new product class.

        Returns:
            type: The new product class.
        """
        # Create a new product subclass with the given name, required resources, and required capabilities
        # The new class should inherit from the Product base class and override its methods as needed
        # The new class is returned, and can then be instantiated and used like any other class
        return type(name, (Product,), {
            "__init__": lambda self: Product.__init__(self, name, description, required_resources, required_capabilities)
        })

    def create_and_save_product_class(self, name, description, required_resources=None, required_capabilities=None,
                                      required_imports=None):
        """
        Dynamically create a new product class and save it to a Python file in the 'dynamically_created_products' module.

        Args:
            name (str): The name of the new product class.
            required_resources (list): The resources required for the new product class.
            required_capabilities (list): The capabilities required for the new product class.
        """
        # Create the new product class
        new_class = self.create_product_class(name, description, required_resources, required_capabilities)
        new_class.is_built_in = False  # Add a property to indicate that this is not a built-in class

        # Generate the Python code for the new class
        class_code = inspect.getsource(new_class)

        # Define the necessary import statements
        import_code = (required_imports + "\n"
                                          "from product_manager.Product import Product\n"
                                          "from resource_manager.Resource import Resource\n"
                                          "from capability_manager.Capability import Capability\n")

        # Combine the import statements and the class code
        code = import_code + class_code

        # Define the module directory
        module = "product_manager/dynamically_created_products"

        # Create the module directory if it does not exist
        if not os.path.exists(module):
            os.makedirs(module)

        # Determine a unique file name
        filename = os.path.join(module, f"{name}Product.py")
        i = 1
        while os.path.exists(filename):
            filename = os.path.join(module, f"{name}V{i}Product.py")
            i += 1

        # Write the code to the file
        with open(filename, "w") as file:
            file.write(code)
