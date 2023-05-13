import logging
import os

log_level = os.getenv('LOG_LEVEL','INFO')

level = logging.getLevelNamesMapping()[log_level]

logging.basicConfig(
    level=level,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger(__name__)