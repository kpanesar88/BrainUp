from typing import Callable, List

from functional import seq

from .async_model import model_loop

from .key_frame import load_model as kf_load
from .transcript import load_model as t_load
from .embedding import load_model as e_load
from .frame_caption import load_model as fc_load
from .text_generation import load_model as tg_load

from .cluster import cluster



def create_pipeline() -> Callable[[List[str]], str]:
    # load all models
    print("Initializing workers")
    kf_in, kf_out, kf_p = model_loop(kf_load)()
    t_in, t_out, t_p = model_loop(t_load)()
    fc_in, fc_out, fc_p = model_loop(fc_load)()
    e_in, e_out, e_p = model_loop(e_load)()
    tg_in, tg_out, tg_p = model_loop(tg_load)()

    def data_batch(videos: List[str]) -> str:
        print(videos)
        print(len(videos))
        embeddings = []
        sent_videos = 0
        required_embeddings = 0

        while sent_videos < len(videos) or required_embeddings > 0:
            if sent_videos != len(videos):
                video_name = videos[sent_videos]
                kf_in.send(video_name)
                t_in.send(f"reels\\{video_name}")

            if kf_out.poll():
                key_frames = kf_out.recv()[1]
                print("sending kf->fc")
                print(key_frames)
                # required_embeddings+= len(key_frames)
                for key_frame in key_frames:
                    fc_in.send(f"key_frames\\{key_frame}")
            
            if fc_out.poll():
                frame_caption = fc_out.recv()[1]
                print("sending fc->e")
                required_embeddings+=1

                e_in.send(frame_caption)
            
            if t_out.poll():
                transcript = t_out.recv()[1]
                print("sending t->e")
                required_embeddings+=1

                e_in.send(transcript)
            

            if e_out.poll():
                print('recv e')
                required_embeddings-=1
                embedding = e_out.recv()[1]
                embeddings.append(embedding)

        print("Cluster time")
        print(embeddings)
        clusters = (seq(cluster(embeddings))
            .sorted(key=len, reverse=True)
            .list()
        )

        tg_in.send(clusters[0])
        return tg_out.recv()[1]
    
    return data_batch

# Example usage
if __name__ == "__main__":
    pipeline = create_pipeline()

    print(
        pipeline([
            "-2970637211523601252.mp4",
            "1834060973874743625.mp4",
            "2764143693230200070.mp4",
            "3879014472440780437.mp4",
            "4018179579686853922.mp4",
            "4491087730200877142.mp4",
            "8512321618049096555.mp4",
        ])
    )