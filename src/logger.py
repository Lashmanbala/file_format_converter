import logging
import os
from dotenv import load_dotenv

def setup_logger():
    try:    
        load_dotenv()

        log_file_path = os.environ.get('LOG_FILE_PATH')
        log_file = os.environ.get('LOG_FILE')

        if not log_file_path:
            raise ValueError("log_file_path is not set in environment variables.")
        
        if not log_file:
            raise ValueError("log_file is not set in environment variables.")

        if not os.path.exists(log_file_path):
            os.makedirs(log_file_path, exist_ok=True)

        logger = logging.getLogger(__name__)

        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file, mode='a')

        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger
    except Exception as e:
        print(f"Error setting up logger: {e}")

logger = setup_logger()

logger.info("Logging initialized successfully.")