import logging

logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

model = "GPT"
input_tokens = 850
output_tokens = 120

logger.info("LLM request started")
logger.info(f"Model: {model}")
logger.info(f"Input tokens: {input_tokens}")
logger.info(f"Output tokens: {output_tokens}")

if output_tokens > 100:
    logger.warning("Output tokens exceed 100, consider optimizing the request.")    

try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    logger.error("An error occurred during processing")