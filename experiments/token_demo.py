from utils.token_utils import calculate_token_cost

input_tokens = 5
output_tokens = 10

cost = calculate_token_cost(input_tokens, output_tokens)
print(cost)
