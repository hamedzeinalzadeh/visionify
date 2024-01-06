import os

import cv2
from loguru import logger

from src.data import DATA_DIR
from src.utils.io import parse_calibration_settings_file
# from src.utils.io import automated_camera_path_detector

# Open camera stream and save frames on a specific path
def save_single_camera_frames():
    '''
    Open camera stream and save frames by pressing 's' on keyboard.
    Images ares savd in src/data/images/single_camera path created by the function automatically.
    '''

    calibration_setting_dict = parse_calibration_settings_file()
    camera_id = calibration_setting_dict['single_camera_path']

    # Another option for detecting camera's address automatically
    # camera_address_list = automated_camera_path_detector(category='by-id')
    # camera_id = camera_address_list[0]

    # Vidoe capture
    cap = cv2.VideoCapture()
    cap.open(camera_id)

    # Set camera resolution
    width = calibration_setting_dict['frame_width']
    height = calibration_setting_dict['frame_height']
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

    # Format camera frames indexing
    counter = 0

    # Check if the "images/sin" directory exists
    images_dir = os.path.join(str(DATA_DIR), 'images/single_camera')

    if not os.path.exists(images_dir):
        # Create the "images/single_camera" directory
        os.makedirs(images_dir)

    while cap.isOpened():

        ret, frame = cap.read()

        k = cv2.waitKey(10)

        # Exit if ESC pressed
        if (k & 0xff) == 27:
            break

        elif k == ord('s'):  # Wait for 's' key to save frames from both cameras

            cv2.imwrite(str(DATA_DIR/'images/single_camera/img') +
                        f'{counter:02d}' + '.png', frame)
            logger.info(f'img_{counter:02d}.png saved.')

            counter += 1

        cv2.imshow('single camera', frame)

    cap.release()
    cv2.destroyAllWindows()


# Open both cameras and make synched frames in a special path
def save_stereo_synched_frames():
    '''
    Open both cameras and make synched frames by pressing 's' on keyboard
    Images ares savd in src/data/images/synched path created by the function automatically.
    '''

    calibration_setting_dict = parse_calibration_settings_file()
    camera_0_id = calibration_setting_dict['camera0_path']
    camera_1_id = calibration_setting_dict['camera1_path']

    # Another option for detecting cameras' addresses automatically
    # camera_address_list = automated_camera_path_detector(category='by-id')
    # camera_0_id = camera_address_list[0]
    # camera_1_id = camera_address_list[1]

    # First Camera
    cap1 = cv2.VideoCapture()
    cap1.open(camera_0_id)

    # Second Camera
    cap2 = cv2.VideoCapture()
    cap2.open(camera_1_id)

    # Set camera resolution
    width = calibration_setting_dict['frame_width']
    height = calibration_setting_dict['frame_height']
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap2.set(cv2.CAP_PROP_FRAME_WIDTH, width)

    # To format camera frames indexing
    counter = 0

    # Check if the "images/synched" directory exists
    synched_images_dir = os.path.join(str(DATA_DIR), 'images/synched')

    if not os.path.exists(synched_images_dir):
        # Create the "images/synched" directory
        os.makedirs(synched_images_dir)

    while (cap1.isOpened() and cap2.isOpened()):

        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        k = cv2.waitKey(10)

        # Exit if ESC pressed
        if (k & 0xff) == 27:

            break

        elif k == ord('s'):  # Wait for 's' key to save frames from both cameras

            cv2.imwrite(str(DATA_DIR/'images/synched/img_cam0_') +
                        f'{counter:02d}' + '.png', frame1)
            cv2.imwrite(str(DATA_DIR/'images/synched/img_cam1_') +
                        f'{counter:02d}' + '.png', frame2)
            logger.info(
                f'img_cam0_{counter:02d}.png and img_cam1_{counter:02d}.png saved.')

            counter += 1

        cv2.imshow('camera 0', frame1)
        cv2.imshow('camera 1', frame2)

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # save_single_camera_frames()
    # save_stereo_synched_frames()
    pass
