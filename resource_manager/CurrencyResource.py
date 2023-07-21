from . import Resource


class CurrencyResource(Resource):
    """
    Budget of USD $0.00 by default, depletes by spend on reasoning engines.
    """

    def __init__(self):
        super().__init__(name="CurrencyResource",
                         description="Resource to represent available real-word currency for spend on LLM API calls")

