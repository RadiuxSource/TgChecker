import logging

# Configure package-level logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logging.info("TgChecker package initialized.")
logging.debug("Debugging information for TgChecker package.")
logging.warning("Warning: Potential issue in TgChecker package.")