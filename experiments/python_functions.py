def classify_model(context_window):
    if context_window >= 500000:
        return "Massive context"
    elif context_window >= 200000:
        return "Very large context"
    elif context_window >= 100000:
        return "Large context"
    else:
        return "Smaller context"

print(classify_model(600000))  # Output: Massive context


# def classify_model(context_window: int) -> str:

#Here, we define a function called classify_model that takes an integer parameter context_window and returns a string. 
#The funcion uses conditional statements to classify the context window size into different categories based on its value.``

# def retrieve_documents(query: str, top_k: int) -> list[str]:

#Here, we define a function called retrieve_documents that takes a string parameter query and an integer parameter top_k. 
#The function is expected to return a list of strings, which represent the top_k documents relevant to the given query. 
#The function signature indicates that it returns a list of strings, but the implementation is not provided in the snippet.


# Write a function to calculate the cost of processing using input and output tokens, given the cost per 1k tokens.
# Assume Input:  $0.01 per 1,000 tokens and Output: $0.03 per 1,000 tokens

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


cost = calculate_token_cost(
    input_tokens=2000,
    output_tokens=1000,
)

print(cost)


#calcualte token usage

def calculate_token_usage(input_tokens: int, output_tokens: int) -> tuple[int, int, int]:
    """Calculate the total token usage for an LLM request."""
    total_tokens = input_tokens + output_tokens
    return input_tokens, output_tokens, total_tokens

total_usage = calculate_token_usage(2000, 1000)
print(total_usage)