import json
import cv2
import os

from src.loader.loader import DatasetLoader
from src.video_capture.capture import VideoCapture

VIDEO_DIR_SUFFIX = "Images"
class Visualization:

    def __init__(self, loader: DatasetLoader):
        self.loader = loader
        self.dataset = self.loader.get_dataset()


    def to_file(self, to_save_path, json_path):
        f = open(json_path)
        data = json.load(f)

        for person in self.dataset.persons:
            for sequence in person.sequences:
                seq_key = "p{}s{}".format(person.id, sequence.seq_id)
                sequence_full_path = os.path.join(sequence.path, VIDEO_DIR_SUFFIX)
                captures = VideoCapture.from_file(sequence_full_path)

                seq_data = data[seq_key].items()
                # 4 kamery -135 klatek - 33 keypointy
                for camera_data, capture in zip(seq_data, captures):
                    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
                    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
                    out = cv2.VideoWriter(to_save_path + seq_key +str(camera_data[0]) + ".avi",
                                          cv2.VideoWriter_fourcc(*"MJPG"), 30, (width, height))

                    frames_data = camera_data[1]
                    while capture.isOpened():
                        success, frame = capture.read()
                        if success:
                            res = frame
                            for point in frames_data[0].items():
                                if len(point[1]) == 0:
                                    continue
                                res = cv2.circle(res, (int(point[1][0][0]), int(point[1][0][1])), 10,  color=(0, 0, 255), thickness=-1)
                            frames_data.pop(0)
                            cv2.imshow("a",res)
                            out.write(frame)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                        else:
                            break

                    cv2.destroyAllWindows()
                    capture.release()



        f.close()

