model = {
    "name": "GPT",
    "provider": "OpenAI",
    "context_window": 128000,
    "supports_tools": True,
    "cost_per_1k_tokens": 0.01
}

print(model)
print(model["name"])
print(model["provider"])
print(model["context_window"])
print(model["cost_per_1k_tokens"])

print("================================================================\n")
print("More Examples of Python Dictionaries\n")

llm_response = {
    "model": {
        "name": "GPT",
        "provider": "OpenAI",
    },
    "usage": {
        "input_tokens": 850,
        "output_tokens": 120,
    },
    "result": {
        "success": True,
        "answer": "Revenue increased by 12%.",
    },
}

print(llm_response["model"]["name"])
print(llm_response["usage"]["input_tokens"])
print(llm_response["usage"]["output_tokens"])
print(llm_response["result"]["answer"])


print("================================================================\n")
print("More Examples of Python Dictionaries and Lists\n")

models = [
    {"name": "GPT", "provider": "OpenAI", "context_window": 128000},
    {"name": "Claude", "provider": "Anthropic", "context_window": 200000},
    {"name": "Gemini", "provider": "Google", "context_window": 1000000},
]

for model in models:
    print(model["name"], "-", model["provider"], "-", model["context_window"])



print("================================================================\n")
print("More Examples of Python Dictionaries ,Lists, conditional logic\n")



models = [
    {"name": "GPT", "provider": "OpenAI", "context_window": 128000},
    {"name": "Claude", "provider": "Anthropic", "context_window": 200000},
    {"name": "Gemini", "provider": "Google", "context_window": 1000000},
]

for model in models:
    if model["context_window"] > 500000:
        print(f'{model["name"]} - Massive context window, suitable for very large documents')
    elif model["context_window"] >= 100000:
        print(f'{model["name"]} - Suitable for large documents')
    else:
        print(f'{model["name"]} - Suitable for smaller documents')