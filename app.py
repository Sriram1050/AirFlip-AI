import cv2
import time
import threading
from gesture.hand_detector import HandDetector
from voice.voice_controller import VoiceController
from utils.page_manager import open_page
from utils.pdf_manager import open_pdf_page
from bot.bot import AssistantBot
hand_detector = HandDetector()
voice_controller = VoiceController()
bot = AssistantBot()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Webcam not found")
    exit()
last_page = 0
last_time = 0
cooldown = 2
running = True
def voice_system():
    global running
    while running:
        page = voice_controller.listen()
        if page:
            success = open_pdf_page(page)
            if success:
                bot.speak(f"Opening page {page}")
            else:
                bot.speak("Page not found")
voice_thread = threading.Thread(target=voice_system)
voice_thread.daemon = True
voice_thread.start()
bot.speak("Gesture voice navigator started")
while True:
    success, frame = cap.read()
    if not success:
        break
    frame = cv2.flip(frame, 1)
    frame, fingers = hand_detector.detect_fingers(frame)
    cv2.putText(
        frame,
        f"Fingers: {fingers}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    current_time = time.time()
    if fingers > 0:
        if fingers != last_page and current_time - last_time > cooldown:
            success = open_pdf_page(fingers)
            if success:
                bot.speak(f"Opening page {fingers}")
                last_page = fingers
                last_time = current_time
    cv2.imshow("Gesture Voice Navigator", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
running = False
cap.release()
cv2.destroyAllWindows()