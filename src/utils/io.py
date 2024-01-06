import os
import subprocess
from pathlib import Path

import yaml
from loguru import logger

from src.data import DATA_DIR


# Parse calibration_setting yaml file and return a dict(because the calibration_setting.yaml stores a dictionary)
def parse_calibration_settings_file(file_path=DATA_DIR / 'calibration_setting.yaml') -> dict:
    """Open and load the calibration_settings.yaml file.

    Args:
        file_address (str): Absolute path of the calibration.setting.yaml. Defaults to str(src/data/calibration_setting.yaml).

    Returns:
        dict: Contents of the given calibration yaml file. 
    """


    # TODO: This has to be an error handler not and logger!
    if not Path.exists(file_path):
        logger.debug(f'File does not exist: {file_path}')
        quit()

    with open(file_path) as f:
        calibration_settings = yaml.load(f, yaml.SafeLoader)

    return calibration_settings

    # try:
    #     Path.exists(file_path)

# Find usb-camera devices connected to system and return a list including addresses
def auto_camera_path_detector(category='by-path') -> tuple:
    """Detect the exact addresses for usb-camera devices connected to a linux baxed system

    Args:
        category (str): The way of addressing the cameras. Defaults to 'by-path'.

    Raises:
        TypeError: 
        ValueError: _description_

    Returns:
        tuple: _description_
    """
    '''
    \'category\' argument indicates the way of addressing the cameras.
    the default value is \'by-path\'. \'by-id\' is another option due to the linux file system.
    '''

    if category == 'by-path':
        # The path of by-path directory in v4l directory
        dir_path = '/dev/v4l/by-path/'
        result = subprocess.run(
            f'ls {dir_path} | grep index0', shell=True, stdout=subprocess.PIPE, text=True)
        camera_paths = tuple(result.stdout.strip().split('\n'))
        return camera_paths

    elif category == 'by-id':
        # TODO: Add the way of addrressing camera by-id
        pass

    elif type(category) is not str:
        raise TypeError(f'Must be str')

    else:
        raise ValueError(
            f'Input argument expected to be \'by-id\' or \'by-path\'')

# TODO:Auto detection of camera parameters
def auto_camera_params_retireval():
    """Automate the capability of rewritting the calibration_setting.yaml
    """
    pass




if __name__ == '__main__':
    parse_calibration_settings_file(123)
    # auto_camera_path_detector()
    pass
