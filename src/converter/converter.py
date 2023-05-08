import os

import cv2

from src.landmarker.landmarker import PoseLandMarker
from src.loader.loader import DatasetLoader
from src.saver.result_saver import ResultSaver
from src.video_capture.capture import VideoCapture

VIDEO_DIR_SUFFIX = "Images"


class Converter:
    def __init__(self, loader: DatasetLoader):
        self.loader = loader
        self.dataset = self.loader.get_dataset()

    def convert_dataset_to_images(self):
        result = dict()
        landmarker = PoseLandMarker()
        for person in self.dataset.persons:
            for sequence in person.sequences:
                seq_key = "p{}s{}".format(person.id, sequence.seq_id)
                result[seq_key] = {}
                sequence_full_path = os.path.join(sequence.path, VIDEO_DIR_SUFFIX)
                captures = VideoCapture.from_file(sequence_full_path)
                for idx, capture in enumerate(captures):
                    frames_coordinates = list()
                    count = 0
                    while capture.isOpened():
                        success, image = capture.read()
                        if success:
                            grouped_landmarks = landmarker.process_img(image)
                            count += 1
                            frames_coordinates.append(grouped_landmarks)
                        else:
                            break
                    result[seq_key][f"camera_{idx}"] = frames_coordinates
                    cv2.destroyAllWindows()
                    capture.release()
        ResultSaver.save_results_to_file('results', result)
