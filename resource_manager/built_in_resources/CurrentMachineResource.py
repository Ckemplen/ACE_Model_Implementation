from resource_manager.Resource import Resource
import psutil
import platform
from datetime import datetime
import yaml
import os
import glob


class CurrentMachineResource(Resource):
    """
    Q: What does this resource provide?
    A: A list of world news result objects, each result has a title, summary, source, link and publish date.

    Q: What is this resource for?
    A: This resource enables layers to get a quick high level overview of the current world state from the
    perspective of several popular RSS feeds.

    Q: How might this resource be extended?
    A: A more diverse set of RSS news sources could be added, it could be made easier to query by date etc.
    Currently, it is a snapshot in time. The resource could be paired with longer term memory if that fits the use case.
    """
    def __init__(self):
        super().__init__(name="CurrentMachineResource", description="")
        self.system_info = {}
        self.cpu_info = {}
        self.memory_info = {}

        # Automatically clean up folder if yaml files exceeds 30
        self.max_files_to_keep = 30

    def execute(self):
        self.get_system_info()
        self.get_cpu_info()
        self.get_memory_info()
        self.save_as_yaml()
        self.clean_up()

    def get_size(self, bytes, suffix="B"):
        # Scale bytes to its proper format
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def get_system_info(self):
        uname = platform.uname()
        self.system_info = {
            "System": uname.system,
            "Node Name": uname.node,
            "Release": uname.release,
            "Version": uname.version,
            "Machine": uname.machine,
            "Processor": uname.processor,
            "Boot Time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y/%m/%d %H:%M:%S")
        }

    def get_cpu_info(self):
        cpufreq = psutil.cpu_freq()
        self.cpu_info = {
            "Physical cores": psutil.cpu_count(logical=False),
            "Total cores": psutil.cpu_count(logical=True),
            "Max Frequency": cpufreq.max,
            "Min Frequency": cpufreq.min,
            "Current Frequency": cpufreq.current,
            "Total CPU Usage": psutil.cpu_percent()
        }

    def get_memory_info(self):
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        self.memory_info = {
            "Total": self.get_size(svmem.total),
            "Available": self.get_size(svmem.available),
            "Used": self.get_size(svmem.used),
            "Percentage": svmem.percent,
            "SWAP": {
                "Total": self.get_size(swap.total),
                "Free": self.get_size(swap.free),
                "Used": self.get_size(swap.used),
                "Percentage": swap.percent
            }
        }

    def save_as_yaml(self):
        data = {
            "System Info": self.system_info,
            "CPU Info": self.cpu_info,
            "Memory Info": self.memory_info
        }

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{self.storage_root}/data/{timestamp}_system_info.yaml"

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as file:
            yaml.dump(data, file)

    def clean_up(self):
        files = glob.glob(f"{self.storage_root}/data/*.yaml")
        if len(files) > self.max_files_to_keep:
            self.logger.debug(f"Trimming older system info files as limit of {self.max_files_to_keep} exceeded.")
            files.sort(key=os.path.getmtime)
            for file in files[:-self.max_files_to_keep]:  # keeping the latest 50 files
                os.remove(file)


if __name__ == "__main__":
    CMR = CurrentMachineResource()
    CMR.execute()
