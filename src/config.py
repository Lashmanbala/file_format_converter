import os
from dotenv import load_dotenv
from logger import logger

def load_config():
    try:
        load_dotenv()

        src_dir = os.environ.get("SRC_BASE_DIR")
        tgt_dir = os.environ.get("TGT_BASE_DIR")

        if not src_dir:
            raise ValueError("SRC_BASE_DIR is not set in environment variables.")
        
        if not tgt_dir:
            raise ValueError("TGT_BASE_DIR is not set in environment variables.")
        
        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")
        
        if not os.path.exists(tgt_dir):
            os.makedirs(tgt_dir, exist_ok=True)
        
        logger.info(f"Environment configuration loaded successfully.")
        return src_dir, tgt_dir
        
    except Exception as e:
        logger.warning(f"Error loading configuration: {e}")
        raise
    
load_config()