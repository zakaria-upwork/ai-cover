from cog import BasePredictor, Input, Path
import os
from utils import download_online_model, generate_ai_cover, get_video_length

class Predictor(BasePredictor):
    def predict(
        self,
        voice_model:str = Input(
            description="Voice model.",
            choices=["custom",
                    "2pac",
                    "adele",
                    "alvin",
                    "ariana-grande",
                    "baby",
                    "biden",
                    "billie-eilish",
                    "britney-spears",
                    "craig-tucker",
                    "darthvader",
                    "drake",
                    "elon-musk",
                    "eminem",
                    "freddie-mercury",
                    "justin-beiber",
                    "kanye",
                    "kurt-cobain",
                    "lisa-simpsons",
                    "megatron",
                    "miley-cyrus",
                    "mj-raspy",
                    "mrbeast",
                    "mrkrabs",
                    "mrohare",
                    "obama",
                    "pikachu",
                    "plankton",
                    "rihanna",
                    "selena-gomez",
                    "siri",
                    "spongebob-squarepants",
                    "squidward",
                    "stewie-griffin",
                    "tate",
                    "taylor-swift",
                    "the-weeknd",
                    "travis-scott",
                    "trump",
                    "villager",
                    "xxxtentacion"],
            default='taylor-swift',),
        audio: Path = Input(
            description="song_input",
            default= None,
        ),
        youtube_link: str = Input(
            description="Youtube link.",
            default= None,
        ),
        custom_voice_model_link:str = Input(
            description="Custom voice model link.",
            default=None
        )
    ) -> Path:
        if audio and youtube_link:
            raise(Exception("Choose audio or youtube link."))
        if youtube_link:
            audio=youtube_link
            if get_video_length(youtube_link)>300:
                raise Exception("Video length should be 5 minutes or less.")
        if voice_model == "custom":
            download_online_model(custom_voice_model_link)
            generate_ai_cover(audio,"custom")
            return Path("song_output/output.mp3")

        generate_ai_cover(audio,voice_model)
        return Path("song_output/output.mp3")
