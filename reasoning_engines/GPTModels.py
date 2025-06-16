# GPTModels.py
import tiktoken
from .OpenRouterModel import OpenRouterModel


class GPTModel:

    def __init__(self, model: str = 'gpt-3.5-turbo'):
        self.model = model
        self.messages = []
        self.client = OpenRouterModel()

    def choose_model(self, budget: float) -> str:
        """Select an OpenRouter model based on remaining budget."""
        if budget > 1:
            return 'openai/gpt-4'
        return 'openai/gpt-3.5-turbo'

    def generate(self, messages, currency_resource=None):
        """Generate a response using OpenRouter and deduct cost."""
        if currency_resource:
            model = self.choose_model(currency_resource.budget)
        else:
            model = self.model
        input_tokens, input_cost = self.measure_tokens(messages, model, 'input')
        if currency_resource and currency_resource.budget < input_cost:
            raise ValueError('Insufficient funds')
        reply = self.client.generate(model=model, messages=messages)
        output_tokens, output_cost = self.measure_tokens([
            {"role": "assistant", "content": reply}
        ], model, 'output')
        total_cost = input_cost + output_cost
        if currency_resource:
            currency_resource.spend(total_cost)
        return reply

    def execute(self, args):
        pass

    def process(self, args):
        pass

    def add_system_message(self, args):
        pass

    def add_user_message(self, args):
        pass

    def measure_tokens(self, messages, model, direction):
        """Counts tokens in a message using tiktoken, calculates cost based on current OpenAI pricing."""

        def _num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
            """Return the number of tokens used by a list of messages."""
            try:
                encoding = tiktoken.encoding_for_model(model)
            except KeyError:
                print("Warning: model not found. Using cl100k_base encoding.")
                encoding = tiktoken.get_encoding("cl100k_base")
            if model in {"gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k-0613", "gpt-4-0314", "gpt-4-32k-0314", "gpt-4-0613",
                "gpt-4-32k-0613", }:
                tokens_per_message = 3
                tokens_per_name = 1
            elif model == "gpt-3.5-turbo-0301":
                tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
                tokens_per_name = -1  # if there's a name, the role is omitted
            elif "gpt-3.5-turbo" in model:
                print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
                return _num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
            elif "gpt-4" in model:
                print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
                return _num_tokens_from_messages(messages, model="gpt-4-0613")
            else:
                raise NotImplementedError(
                    f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
            num_tokens = 0
            for message in messages:
                num_tokens += tokens_per_message
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":
                        num_tokens += tokens_per_name
            num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
            return num_tokens

        token_count = _num_tokens_from_messages(messages, model)

        pricing_lookup = {"input": {'gpt-3.5-turbo-0613': 0.0015, 'gpt-3.5-turbo-16k-0613': 0.003, 'gpt-4-0314': 0.03,
                                    'gpt-4-32k-0314': 0.06, 'gpt-4-0613': 0.03, 'gpt-4-32k-0613': 0.06},
                          "output": {'gpt-3.5-turbo-0613': 0.002, 'gpt-3.5-turbo-16k-0613': 0.004, 'gpt-4-0314': 0.06,
                                     'gpt-4-32k-0314': 0.12, 'gpt-4-0613': 0.06, 'gpt-4-32k-0613': 0.12}}

        cost = (token_count * pricing_lookup[direction][model]) / 1000

        return token_count, cost
