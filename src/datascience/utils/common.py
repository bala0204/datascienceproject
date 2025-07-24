import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.expectations import BoxValueError
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        valueError: If the file does not exist or is empty.
        e: empty file
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file read successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:

        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.

    Returns:
        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to save.

    Returns:
        None
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"Data saved to JSON file at {path}")

@ensure_annotations
def load_json(path: Path) -> dict:
    """
    Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        dict: Data loaded from the JSON file.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"Data loaded from JSON file at {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Path to the binary file.

    Returns:
        None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved to binary file at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(filename=path)
    logger.info(f"Data loaded from binary file at {path}")
    return data


