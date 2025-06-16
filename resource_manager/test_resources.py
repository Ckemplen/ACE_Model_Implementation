import importlib
import os

from resource_manager import ResourceManager, Resource


def test_dynamic_resource_creation_and_import():
    manager = ResourceManager(creator="tester")
    name = "TempRes"
    description = "temporary resource"

    path = manager.create_and_save_resource_class(name, description, capacity=1, used=0, budget=0, required_imports="")

    assert os.path.exists(path)

    module_name = "resource_manager.dynamically_created_resources." + os.path.splitext(os.path.basename(path))[0]
    mod = importlib.import_module(module_name)
    cls = getattr(mod, name)
    instance = cls()
    assert isinstance(instance, Resource)

    os.remove(path)
