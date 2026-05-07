import cv2
import mediapipe as mp
import os


class HandDetector:

    def __init__(self):

        model_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "hand_landmarker.task"
        )

        BaseOptions = mp.tasks.BaseOptions
        HandLandmarker = mp.tasks.vision.HandLandmarker
        HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode

        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.IMAGE,
            num_hands=1
        )

        self.detector = HandLandmarker.create_from_options(options)

    def detect_fingers(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = self.detector.detect(mp_image)

        finger_count = 0

        if result.hand_landmarks:

            hand = result.hand_landmarks[0]

            tips = [4, 8, 12, 16, 20]

            fingers = []

            # Thumb
            if hand[tips[0]].x < hand[tips[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers
            for i in range(1, 5):

                if hand[tips[i]].y < hand[tips[i] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            finger_count = fingers.count(1)

        return frame, finger_count