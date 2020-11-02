import time
import _thread
from tts import playaudio

stop = False

def read_bullets(bullets, start_time, duration):
    cur_time = int(start_time)
    global stop
    stop = False
    # every second, start all the bullets
    while cur_time <= duration:
        if stop:
            stop = False
            return
        if str(cur_time) in bullets:
            for bul in bullets[str(cur_time)]:
                try:
                    _thread.start_new_thread(playaudio, (bul, ))
                except ValueError:
                    print(ValueError)
        time.sleep(1)
        cur_time += 1

def stop_reading():
    global stop
    stop = True