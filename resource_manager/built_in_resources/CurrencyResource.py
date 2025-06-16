from resource_manager import Resource


class CurrencyResource(Resource):
    """Currency resource tracking API budget."""

    def __init__(self, budget: float = 0.0):
        super().__init__(
            name="CurrencyResource",
            description="Resource to represent available real-word currency for spend on LLM API calls",
            budget=budget,
        )

    def spend(self, amount: float) -> None:
        """Deduct amount from budget and log the spend."""
        if amount < 0:
            raise ValueError("Spend amount must be positive")
        if self.budget - amount < 0:
            raise ValueError("Insufficient currency budget")
        self.budget -= amount
        self.logger.debug(f"CurrencyResource spent ${amount:.4f}, remaining ${self.budget:.4f}")
