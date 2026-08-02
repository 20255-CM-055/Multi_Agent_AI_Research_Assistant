import logging
from pathlib import Path

# Create logs directory if it doesn't exist
log_directory = Path("logs")
log_directory.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(log_directory / "app.log"),
        logging.StreamHandler()
    ],
)

logger = logging.getLogger("research_assistant")