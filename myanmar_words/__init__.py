# myanmar_words/__init__.py

# Import important modules and classes
from .main import get, find, brake, count

# Define package-level variables
__version__ = "1.0.0"
__author__ = "Lin Htut Kyaw"

# Specify what gets imported when using 'from myanmar-words import *'
__all__ = ["get","find", "brake", "count"]
