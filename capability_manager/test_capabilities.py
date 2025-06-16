import importlib
import os

from capability_manager import CapabilityManager, Capability


def test_dynamic_capability_creation_and_import():
    manager = CapabilityManager(creator="tester")
    name = "TempCap"
    description = "temporary capability"

    path = manager.create_and_save_capability_class(name, description, required_imports="")

    assert os.path.exists(path)

    module_name = "capability_manager.dynamically_created_capabilities." + os.path.splitext(os.path.basename(path))[0]
    mod = importlib.import_module(module_name)
    cls = getattr(mod, name)
    instance = cls()
    assert isinstance(instance, Capability)

    os.remove(path)
