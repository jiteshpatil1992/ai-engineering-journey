from ai_engineering_journey.token.calculator import calculate_token_cost


def test_calculate_token_cost():
    result = calculate_token_cost(
        input_tokens=2000,
        output_tokens=1000,
    )

    assert result == 0.05


def test_zero_tokens():
    result = calculate_token_cost(
        input_tokens=0,
        output_tokens=0,
    )

    assert result == 0.0


def test_large_token_usage():
    result = calculate_token_cost(
        input_tokens=10000,
        output_tokens=5000,
    )

    assert result == 0.25