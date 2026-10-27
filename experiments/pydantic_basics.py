from pydantic import BaseModel


class LLMresponse(BaseModel):
    answer: str
    confidence : float
    input_tokens : int
    output_tokens : int
    success      : bool


model = LLMresponse(
    answer="Revenue increased by 12%",
    confidence= 0.92,
    input_tokens= 850,
    output_tokens= 120,
    success= True
)

print(model)
print(model.answer)
print(model.confidence)
print(model.input_tokens)
print(model.output_tokens)
print(model.success)