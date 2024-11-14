from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .device_model import City
from .explosive_model import Mission
from .location_model import Target
from .terrorist_model import TargetType
from .hostage_model import Country
