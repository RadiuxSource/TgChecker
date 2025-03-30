import logging
import os

# Configure logging format
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a logger instance
logger = logging.getLogger("TgChecker")

# Log file setup (optional)
LOG_FILE = os.getenv("LOG_FILE", "bot.log")
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

logger.info("Logger initialized successfully!")

# Example function logs
def aditya_logging():
    logger.info("Aditya's function was executed successfully!")

def aman_logging():
    logger.warning("Aman's function encountered a minor issue!")

def chhotu_logging():
    logger.error("Chhotu's function encountered a critical error!")

# Science Study Room
