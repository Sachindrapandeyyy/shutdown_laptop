import os
import speech_recognition as sr
import time

def listen_for_command():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise. Please wait...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for the command...")

            audio_data = recognizer.listen(source)
            print("Recognizing...")

            command = recognizer.recognize_google(audio_data).lower()
            print(f"Command received: {command}")

            if "shutdown laptop" in command:
                print("Shutting down the laptop...")
                os.system("shutdown /s /t 1")  

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Voice-activated shutdown script is running. Say 'Edith shutdown laptop' to shut down your laptop.")
    while True:
        listen_for_command()
        time.sleep(0.5)  
