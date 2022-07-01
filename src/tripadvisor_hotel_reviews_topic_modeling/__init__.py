"""tripadvisor_hotel_reviews_topic_modeling Python package."""

from importlib.metadata import version
from typing import List

__version__ = version(__package__)

# Add imported functions in this list to prevent flake8 F401 issues. See
# https://stackoverflow.com/a/59438802 for further details
__all__: List[str] = []
