# from typing import List

import os
from dotenv import load_dotenv
# from .insta_posts import Reel

load_dotenv()

# from InstagramReelDownloader import ReelDownload
# import chromedriver_autoinstaller


# chromedriver_autoinstaller.install()

INSTAGRAM_SESSION_ID = os.getenv('INSTAGRAM_SESSION_ID')

# def download_links(links: List[str]) -> bool:
#     for link in links:
#         if not download(link):
#             return False
        
#     return True
# def download(link: str) -> bool:
    
#     sample_reel = Reel('https://www.instagram.com/reel/CKWDdesgv2l')
#     sample_reel.scrape(
#         headers={
#             "user-agent": "Mozilla/5.0 (Linux; Android 6.0;",
#             "cookie":f'sessionid={INSTAGRAM_SESSION_ID};'
#         }
#     )
#     # reeldir = os.getcwd()
#     sample_reel.download(fp=f"reels\\reel.mp4")
#     # print(dir)
#     # print(f"This reel has {sample_reel.video_view_count:,} views.")

# if __name__ == "__main__":
#     from . import get_links

#     download(get_links(dict()))


import time
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from functional import seq

import requests
import os

def ensure_folder_exists(folder_path):
    """Ensure the folder exists, if not, create it."""
    os.makedirs(folder_path, exist_ok=True)

def download_file(url):
    """Download the content from a URL and return the bytes if successful."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download the file. Status code: {response.status_code}")

def save_file(content, file_path):
    """Save the downloaded content to a file."""
    with open(file_path, 'wb') as file:
        file.write(content)

def download_mp4(url, save_folder, filename):
    """Main function to download an MP4 and save it to a specified folder."""
    ensure_folder_exists(save_folder)
    file_path = os.path.join(save_folder, filename)
    content = download_file(url)
    save_file(content, file_path)
    print(f"File saved successfully at: {file_path}")

# Example usage

options = Options()

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

# options = {"desired_capabilities": caps}
# options.set_capability('desired_capabilities', caps)
driver = webdriver.Chrome(
    executable_path="C:\\chromedriver\\chromedriver.exe",
    desired_capabilities=caps
)#options=options)
driver.get('https://www.instagram.com/reel/Cccgd2MFCs4/')
driver.add_cookie({
    # "https://www.instagram.com": {
        "name": "sessionid",
        "value": INSTAGRAM_SESSION_ID
    # }
})
driver.get('https://www.instagram.com/reel/Cccgd2MFCs4/')
time.sleep(0.25)


def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response

browser_log = driver.get_log('performance') 
urls = (
    seq(browser_log)
        .map(process_browser_log_entry)
        .filter(lambda event: 'Network.requestWillBeSent' in event['method'])
        .map(lambda event: event["params"])
        .filter(lambda event: "request" in event)
        .map(lambda event: event["request"])
        .map(lambda event: event["url"])
        .filter(lambda url: ".mp4" in url)
        .map(lambda url: url[:min(url.index("bytestart"), url.index("byteend"))-1])
        .set()
)

print(urls)

for url in urls:
    save_folder = "reels"
    filename = f"{hash(url)}.mp4"
    download_mp4(url, save_folder, filename)
# url