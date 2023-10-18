import subprocess
import random
from pynput.mouse import Listener

sounds = [
    "bruh", 
    "obamna", 
    "sus", 
    "wah", 
    "fazbear"
]

sound_queue = sounds.copy()
random.shuffle(sound_queue)

def play_random_sound():
    if sound_queue:
        sound = sound_queue.pop(0)
        subprocess.run(["echo", f"Playing: {sound}.mp3"])
        subprocess.run(["mplayer", f"{sound}.mp3"])
    else:
        random.shuffle(sounds)
        sound_queue.extend(sounds)

def on_click(x, y, button, pressed):
    if pressed:
        play_random_sound()

def main():
    with Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()
