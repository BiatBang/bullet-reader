import time
from tts import playaudio

def read_bullets(url, bullets, duration):
    cur_time = 0
    # every second, start all the bullets
    while cur_time <= duration:
        if str(cur_time) in bullets:
            for bul in bullets[str(cur_time)]:
                playaudio(bul)
        time.sleep(1)
        cur_time += 1