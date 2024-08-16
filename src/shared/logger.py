import logging
import os
from datetime import datetime
from pathlib import Path

ROOT_DIR = str(os.path.dirname(Path(__file__).parent))

# Configure the logging
FILE_LOG = os.path.join(ROOT_DIR, "logs", "{:%Y-%m-%d}.log".format(datetime.now()))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(FILE_LOG),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
