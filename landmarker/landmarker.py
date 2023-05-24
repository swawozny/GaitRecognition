import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
BG_COLOR = (192, 192, 192)


class PoseLandMarker:
    def __init__(self):
        self.model = mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5)

    def process_img(self, image):
        image_height, image_width, _ = image.shape
        results = self.model.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        return self.group_by_landmarks(results, image_width, image_height)

    def group_by_landmarks(self, results, img_width, img_height):
        grouped_landmarks = {}
        idx = 0
        for pose_landmark in mp.solutions.pose.PoseLandmark:
            if pose_landmark not in grouped_landmarks:
                grouped_landmarks[pose_landmark] = []
            idx += 1
            if not results.pose_landmarks:
                continue
            landmark = results.pose_landmarks.landmark[pose_landmark]

            x = landmark.x * img_width
            y = landmark.y * img_height

            grouped_landmarks[pose_landmark].append((x, y))

        return grouped_landmarks
