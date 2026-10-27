def calculate_token_cost(
    input_tokens: int,
    output_tokens: int,
    input_price: float = 0.01,
    output_price: float = 0.03,
) -> float:
    """Calculate the estimated cost of an LLM request."""

    input_cost = (input_tokens / 1000) * input_price
    output_cost = (output_tokens / 1000) * output_price

    return input_cost + output_cost