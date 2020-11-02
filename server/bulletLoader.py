from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests, json, re

def getHtml(url):
    # header for bilibili
    html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}).content.decode('utf-8')
    return html

def getContent(url):
    html = getHtml(url)
    soup = BeautifulSoup(html, "html.parser")
    return soup

# the raw html contains the duration of the video and cid
def find_cid_duration(url):
    # trash and brute solution
    html = getHtml(url)
    # cid in 'cid=*******'
    cid = re.findall(r'cid=(\d+)&', html)[0]
    # duration in "duration":****
    duration = int(re.findall(r'\"duration\":(\d+),', html)[0])
    return cid, duration

def load_bullet_duration_from_url(url, bullets):
    cid, duration = find_cid_duration(url)
    # bilibili uses a xml to store all comments
    comment_url = "https://comment.bilibili.com/" + cid + ".xml"
    page_content = getContent(comment_url)
    bullet_blocks = page_content.findAll('d')
    for b_b in bullet_blocks:
        time = b_b['p'].split(',')[0].split(".")[0]
        text = b_b.text
        if time not in bullets:
            bullets[time] = []
        bullets[time].append(text)
    return duration