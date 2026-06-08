from loguru import logger
import os

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

logger.add(
    f"{LOG_DIR}/framework.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO"
)

def get_logger():
    return logger