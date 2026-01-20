"""
gpapis - GlobalPlatform API Manager

A simple tool to help JavaCard developers access GlobalPlatform API specifications.
"""

__version__ = "1.0.0"

from .api import get_api_resource, list_api_versions, get_all_resources

__all__ = [
    "get_api_resource",
    "list_api_versions",
    "get_all_resources"
]