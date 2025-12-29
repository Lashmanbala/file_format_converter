import logging
import os
from dotenv import load_dotenv

def setup_logger():
    try:    
        load_dotenv()

        log_file_path = os.environ.get('LOG_FILE_PATH')

        if not log_file_path:
            raise ValueError("log_file_path is not set in environment variables.")

        logger = logging.getLogger(__name__)

        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file_path, mode='a')

        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger
    except Exception as e:
        print(f"Error setting up logger: {e}")

logger = setup_logger()

logger.info("Logging initialized successfully.")