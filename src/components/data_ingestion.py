import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from logger import logging

from exception import CustomException


try:
    pass
except Exception as e:
    raise CustomException(e,sys)
