"""
API module for gpapis.
Provides functions to access GlobalPlatform API specifications.
"""

import os
from pathlib import Path

# Environment variable name for API root
API_ROOT_ENV = "GLOBALPLATFORM_API_ROOT"

# API types supported
API_TYPES = ["broker", "contactless", "core", "open", "scpp", "upgrade"]

def get_api_root() -> str:
    """
    Get the API root path from environment variable.
    
    Returns:
        str: API root path if set, empty string otherwise
    """
    return os.environ.get(API_ROOT_ENV, "")

def set_api_root(path: str) -> bool:
    """
    Set the API root path in environment variable.
    
    Args:
        path: Path to API root directory
        
    Returns:
        bool: True if path is valid and set successfully
    """
    try:
        api_path = Path(path)
        if not api_path.exists() or not api_path.is_dir():
            return False
        
        os.environ[API_ROOT_ENV] = str(api_path)
        return True
    except Exception:
        return False

def get_api_resource(api_type: str, version: str, filename: str) -> str:
    """
    Get a specific API resource file.
    
    Args:
        api_type (str): The API type (broker, contactless, core, open, scpp, upgrade)
        version (str): The version (e.g., '1.0', '1.8')
        filename (str): The filename to retrieve
    
    Returns:
        str: Path to the resource file if it exists, empty string otherwise
    """
    api_root = get_api_root()
    if not api_root:
        return ""
    
    if api_type.lower() not in API_TYPES:
        return ""
    
    # Construct the expected path
    api_path = Path(api_root) / api_type.lower() / version / filename
    
    if api_path.exists() and api_path.is_file():
        return str(api_path)
    
    return ""

def list_api_versions(api_type: str) -> list:
    """
    List all available versions for a specific API type.
    
    Args:
        api_type (str): The API type (broker, contactless, core, open, scpp, upgrade)
    
    Returns:
        list: List of available versions
    """
    api_root = get_api_root()
    if not api_root:
        return []
    
    if api_type.lower() not in API_TYPES:
        return []
    
    api_path = Path(api_root) / api_type.lower()
    if not api_path.exists() or not api_path.is_dir():
        return []
    
    try:
        # Get all directories in the API type directory
        return [item.name for item in api_path.iterdir() if item.is_dir()]
    except Exception:
        return []

def get_all_resources() -> dict:
    """
    Get all available API resources.
    
    Returns:
        dict: Dictionary with API types as keys and their versions as values
    """
    apis = {}
    
    for api_type in API_TYPES:
        versions = list_api_versions(api_type)
        if versions:
            apis[api_type] = versions
    
    return apis