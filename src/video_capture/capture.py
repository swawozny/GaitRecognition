import os

import cv2


class VideoCapture:

    @staticmethod
    def from_file(path):
        captures = []
        for file in os.listdir(path):
            if not file.startswith('.'):
                captures.append(cv2.VideoCapture(os.path.join(path, file)))
        return captures
