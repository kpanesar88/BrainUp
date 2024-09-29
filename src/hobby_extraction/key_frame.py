from typing import List
from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter
import os

def load_model():
    def _tmp(video_name) -> List[str]:
        return extract_frames(
            video_name
        )
    return _tmp

def extract_frames(video_name: str, frame_count: int = 12) -> List[str]:
    vd = Video()

    disk_writer = KeyFrameDiskWriter(location="key_frames")

    video_file_path = f"reels\\{video_name}"

    vd.extract_video_keyframes(
        no_of_frames=frame_count,
        file_path=video_file_path,
        writer=disk_writer
    )

    files = [
        f"{video_name[:-4]}_{i}.jpeg" for i in range(frame_count) 
    ]

    return files

if __name__ == "__main__":
    # Get key frames
    print(extract_frames("4018179579686853922.mp4"))