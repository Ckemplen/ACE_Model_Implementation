from .CognitiveLayer import CognitiveLayer
from resource_manager.built_in_resources import CurrencyResource


class TaskProsecutionLayer(CognitiveLayer):
    """
    While the above cognitive control layer is responsible for choosing and switching between tasks,
    the task prosecution layer is responsible for performing one task at time. This could be robotic commands,
    such as moving from one place to another, or it could also be performing coding problems, such as writing or
    testing code and sending API calls. This layer is responsible for detecting whether or not an individual task was
    successful or not.

    Key Responsibilities:
    - One task at a time
    - Detect failure or success
    """

    def __init__(self):
        super().__init__(name="TaskProsecutionLayer")
        self.resources.add_resource(name="CurrencyResource", resource=CurrencyResource(budget=1.5))
        # The heavy GoogleSearchScrapeResearchCapability is omitted in test environments

    def process_input(self, input_data):
        # Some other action specific to this layer
        processed_data = self.GPTModel.process(input_data)
        return processed_data

    def execute(self):

        try:
            self.process_input("something")

            self.initiate_task("something")

            self.monitor_tasks("something")

            currency = self.resources.get_resource("CurrencyResource")
            if currency and currency.budget > 0:
                messages = [{"role": "user", "content": "something"}]
                result = self.GPTModel.generate(messages, currency)
            else:
                self.logger.warning("Insufficient funds for model call")
                result = None

            return result
        except Exception as e:
            self.pass_up(f"Error: {str(e)}")

    def initiate_task(self, task):
        # Initiate a new task
        pass  # Placeholder

    def monitor_tasks(self):
        # Monitor the progress of ongoing tasks
        return {}  # Placeholder

    def pass_up_status(self):
        status = self.get_status()
        self.pass_up(status)

    def receive_request_from_above(self):
        request = self.receive_from_above()
        if request:
            print(f"Received request from above: {request}")
            # Execute the requested action and send a response
            response = self.execute(request)
            self.pass_up(response)

    def handle_failure(self):
        pass

    def handle_success(self):
        pass
