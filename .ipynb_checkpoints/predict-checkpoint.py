from cog import BasePredictor, Input, Path
import os
from utils import download_online_model, download_gdrive_model, generate_ai_cover, move_model

class Predictor(BasePredictor):
    def predict(
        self,
        voice_model:str = Input(
            description="Voice model.",
            choices=["custom"
                    ,"ariana-grande"
                    ,"the-weeknd"
                    ,"villager"
                    ,"trump"
                    ,"taylor-swift" 
                    ,"tate"
                    ,"squidward"
                    ,"spongebob-squarepants"
                    ,"siri"
                    ,"britney-spears"
                    ,"pikachu"
                    ,"obama"
                    ,"mrbeast"
                    ,"mj-raspy"
                    ,"megatron"
                    ,"kanye"
                    ,"eminem"
                    ,"elon-musk" 
                    ,"drake"
                    ,"darthvader"
                    ,"billie-eilish"
                    ,"biden"],
            default='taylor-swift',),
        audio: str = Input(
            description="Youtube link.",
            default= None,
        ),
        custom_voice_model_link:str = Input(
            description="Custom voice model link.",
            default=None
        )
    ) -> Path:
        if voice_model == "custom":
            download_online_model(custom_voice_model_link)
            generate_ai_cover(audio,"custom")
            return Path("song_output/output.mp3")

        generate_ai_cover(audio,voice_model)
        return Path("song_output/output.mp3")
