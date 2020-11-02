from bulletLoader import load_bullet_duration_from_url
from bulletReader import read_bullets
from tts import playaudio
import _thread

def test_load():
    url = 'https://www.bilibili.com/video/BV1eV411y7fa?spm_id_from=333.851.b_7265706f7274466972737431.7'
    load_bullet_duration_from_url(url, dict())

def test_threads():
    for i in range(10):
        try:
            _thread.start_new_thread(playaudio, ("我是" + str(i), ))
        except Exception as e:
            print(e)
            raise

def test_read():
    bullets = dict()
    bullets['1'] = ["哈哈哈", "我死了", "嘿嘿嘿", "前1000"]
    bullets['4'] = ["你是煞笔", "火钳刘明", "前方高能"]
    bullets['5'] = ["我是你爹"]
    duration = 8
    read_bullets(bullets, duration)

if __name__ == '__main__':
    test_read()
    # playaudio("仌")