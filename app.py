import argparse
import logging
import os.path

import cv2

from src.converter.converter import Converter
from src.loader.loader import DatasetLoader
from src.visualization.visualization import Visualization
from src.video_capture.capture import VideoCapture


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_dir', type=str, nargs='?',
                        help='A required path to configuration file')

    args = parser.parse_args()
    dataset_path = args.dataset_dir or 'src/datasets/gait3d'

    loader = DatasetLoader(dataset_path)
    converter = Converter(loader)
    converter.convert_dataset_to_images()
    visualizer = Visualization(loader)
    visualizer.to_file("./results/", "./results.json")



if __name__ == "__main__":
    main()
