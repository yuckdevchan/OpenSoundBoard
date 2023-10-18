import subprocess
import random
from pynput.mouse import Listener

sounds = [
    "bruh",
    "obamna",
    "sus",
    "wah",
    "fazbear",
    "bababooey"
]

sound_queue = sounds.copy()
random.shuffle(sound_queue)
current_sound_process = None

def play_random_sound():
    global current_sound_process
    if current_sound_process:
        current_sound_process.kill()

    if sound_queue:
        sound = sound_queue.pop(0)
        print(f"Playing: {sound}.mp3")
        current_sound_process = subprocess.Popen(["mplayer", f"{sound}.mp3"])
    else:
        random.shuffle(sounds)
        sound_queue.extend(sounds)

def on_click(x, y, button, pressed):
    print("Mouse Click Detected...")
    if pressed:
        play_random_sound()

def main():
    with Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()
