from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .device_model import Device
from .explosive_model import Explosive
from .location_model import Location
from .terrorist_model import Terrorist
from .hostage_model import Hostage
