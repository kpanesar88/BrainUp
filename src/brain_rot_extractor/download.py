from typing import List

import os
from dotenv import load_dotenv
from instascrape import Reel

load_dotenv()

INSTAGRAM_SESSION_ID = os.getenv('INSTAGRAM_SESSION_ID')

def download_links(links: List[str]) -> bool:
    for link in links:
        if not download(link):
            return False
        
    return True
def download(link: str) -> bool:
    sample_reel = Reel('https://www.instagram.com/reel/Cccgd2MFCs4/')
    sample_reel.scrape(
        headers={
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0;",
            "cookie":f'sessionid={INSTAGRAM_SESSION_ID};'
        }
    )
    # reeldir = os.getcwd()
    sample_reel.download(fp=f"reels\\reel.mp4")
    print(dir)
    print(f"This reel has {sample_reel.video_view_count:,} views.")

if __name__ == "__main__":
    from . import get_links

    download(get_links(dict()))
