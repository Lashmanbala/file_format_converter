import os
from dotenv import load_dotenv
from logger import logger

def load_config():
    try:
        load_dotenv()

        src_dir = os.environ.get("SRC_BASE_DIR ")
        tgt_dir = os.environ.get("TGT_BASE_DIR ")

        if not src_dir:
            raise ValueError("SRC_BASE_DIR is not set in environment variables.")
        
        if not tgt_dir:
            raise ValueError("TGT_BASE_DIR is not set in environment variables.")
        
        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")
        
        if not src_dir.os.path.isdir():
            raise NotADirectoryError(f"Source path '{src_dir}' is not a directory.")
        
        if not os.makedirs(tgt_dir, exist_ok=True):
            raise OSError(f"Could not create target directory '{tgt_dir}': {e}")
        
        return src_dir, tgt_dir
        
    except Exception as e:
        logger.warning(f"Error loading configuration: {e}")
        raise
