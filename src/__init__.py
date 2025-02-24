import logging
import sys, os

logger_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "Logs"
log_filepath = os.join.path(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
                    level=logging.INFO, 
                    format=logger_str, 
                    handlers=[
                        logging.FileHandler(logger_str),
                        logging.StreamHandler(sys.stdout)
                    ]
)
logger = logging.getLogger('src')
