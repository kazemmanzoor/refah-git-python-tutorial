import threading
import time
import dlib
import cv2
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class AlarmApp(App):
    def build(self):
        # Create the GUI layout
        layout = BoxLayout(orientation="vertical")

        # Create the time input field
        self.time_input = TextInput(hint_text="Enter alarm time (HH:MM)")

        # Create the start alarm button
        start_alarm_button = Button(text="Start Alarm")
        start_alarm_button.bind(on_press=self.start_alarm)

        # Create the stop alarm button
        self.stop_alarm_button = Button(text="Stop Alarm", disabled=True)
        self.stop_alarm_button.bind(on_press=self.stop_alarm)

        # Create the remaining time label
        self.remaining_time_label = Label(text="", font_size="50sp")

        # Create the blink count label
        self.blink_count_label = Label(text="", font_size="50sp")

        # Add the GUI widgets to the layout
        layout.add_widget(self.time_input)
        layout.add_widget(start_alarm_button)
        layout.add_widget(self.stop_alarm_button)
        layout.add_widget(self.remaining_time_label)
        layout.add_widget(self.blink_count_label)

        return layout

    def start_alarm(self, instance):
        # Parse the alarm time from the input field
        alarm_time_str = self.time_input.text.strip()
        try:
            alarm_time = time.strptime(alarm_time_str, "%H:%M")
        except ValueError:
            self.remaining_time_label.text = "Invalid time format"
            return

        # Calculate the remaining time until the alarm
        now = time.localtime()
        remaining_time = (time.mktime(alarm_time) - time.mktime(now))

        if remaining_time <= 0:
            self.remaining_time_label.text = "Invalid time"
            return

        # Update the remaining time label
        self.remaining_time_label.text = time.strftime("%M:%S", time.gmtime(remaining_time))

        # Disable the start alarm button and enable the stop alarm button
        instance.disabled = True
        self.stop_alarm_button.disabled = False

        # Start the alarm thread
        self.alarm_thread = threading.Thread(target=self.alarm, args=(remaining_time,))
        self.alarm_thread.start()

    def stop_alarm(self, instance):
        # Stop the alarm if it's currently playing
        if self.alarm_thread.is_alive():
            self.alarm_thread.do_run = False
            self.alarm_thread.join()

            # Reset the GUI widgets
            self.remaining_time_label.text = ""
            self.blink_count_label.text = ""
            self.time_input.text = ""
            self.stop_alarm_button.disabled = True
            instance.disabled = False

    def alarm(self, remaining_time):
        # Wait until the alarm time is up
        time.sleep(remaining_time)

        # Load the alarm sound file
        pygame.mixer.init()
        pygame.mixer.music.load("alarm_sound.mp3") # Replace "alarm_sound.mp3" with the path to your alarm sound file

        # Open the video camera
        cap = cv2.VideoCapture(0)

        # Initialize the blink detector
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        left_eye_start, left_eye_end = 36, 41
        right_eye_start, right_eye_end = 42, 47
        blink_count = 0

        # Start playing the alarm sound
        pygame.mixer.music.play()

        # Loop until the alarm is stopped or the user blinks more than 20 times
        while pygame.mixer.music.get_busy() and blink_count < 20:
            # Read a frame from the camera
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = detector(gray, 0)

            # Loop over the faces and detect blinks
            for face in faces:
                landmarks = predictor(gray, face)
                left_eye = landmarks.part(left_eye_start:left_eye_end+1)
                right_eye = landmarks.part(right_eye_start:right_eye_end+1)
                left_eye_ratio = eye_aspect_ratio(left_eye)
                right_eye_ratio = eye_aspect_ratio(right_eye)
                eye_ratio = (left_eye_ratio + right_eye_ratio) / 2
                if eye_ratio < 0.25:
                    blink_count += 1

            # Update the blink count label
            self.blink_count_label.text = f"Blink count: {blink_count}"

        # Stop the alarm sound and clean up the mixer and camera
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        cap.release()

        # If the user blinked more than 20 times, stop the alarm automatically
        if blink_count >= 20:
            self.stop_alarm(self.stop_alarm_button)

def eye_aspect_ratio(eye):
    x = np.mean([p.x for p in eye])
    y = np.mean([p.y for p in eye])
    v1 = np.array([eye[1].x - eye[5].x, eye[1].y - eye[5].y])
    v2 = np.array([eye[2].x - eye[4].x, eye[2].y - eye[4].y])
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    if norm == 0:
        return 0
    else:
        return np.dot(v1, v2) / norm

if __name__ == "__main__":
    AlarmApp().run()