import argparse
import logging
import os.path
import sys
import pathlib

import cv2

from src.converter.converter import Converter
from src.loader.loader import DatasetLoader
from src.visualization.visualization import Visualization
from src.video_capture.capture import VideoCapture
from src.gui.VideoWindow import VideoWindow
from PyQt5.QtWidgets import QApplication


def main():
    result_path = str(pathlib.Path(__file__).parent.resolve()) + '/results'
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_dir', type=str, nargs='?',
                        help='A required path to configuration file')
    parser.add_argument('action', type=str, nargs='?',
                        help='A type of operation that the program will execute')

    args = parser.parse_args()
    dataset_path = args.dataset_dir or '../PreparedSeq'
    action = args.action or 'all'

    loader = DatasetLoader(dataset_path)

    if(action=="find" or action=="all"):
        converter = Converter(loader)
        converter.convert_dataset_to_images()
    if(action=="visualize" or action=="all"):
        visualizer = Visualization(loader)
        visualizer.to_file("./results/", "./results.json")
    print(result_path)
    if(action=="show" or action=="all"):
        app = QApplication([])
        player = VideoWindow(result_path)
        player.showMaximized()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()

