import pytest
from unittest.mock import patch

from reasoning_engines import GPTModel
from resource_manager.built_in_resources import CurrencyResource


def make_response(text="ok"):
    class Resp:
        def raise_for_status(self):
            pass

        def json(self):
            return {"choices": [{"message": {"content": text}}]}
    return Resp()


@patch("reasoning_engines.OpenRouterModel.requests.post")
def test_spend_after_api_call(mock_post):
    events = []

    def post_side_effect(*args, **kwargs):
        events.append("api")
        return make_response("hi")

    mock_post.side_effect = post_side_effect

    currency = CurrencyResource(budget=1.0)
    model = GPTModel()

    with patch.object(currency, "spend", wraps=currency.spend) as spy_spend, \
         patch.object(GPTModel, "measure_tokens", return_value=(1, 0.1)):
        reply = model.generate([{"role": "user", "content": "hello"}], currency)
        events.append("spend")
        spy_spend.assert_called_once()

    assert reply == "hi"
    assert events[0] == "api"
    assert events[1] == "spend"
    assert currency.budget == pytest.approx(0.8)

