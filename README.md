# AI-Cover
An autonomous pipeline to create covers with any RVC v2 trained AI voice from YouTube videos or a local audio file. For developers who may want to add a singing functionality into their AI assistant/chatbot/vtuber, or for people who want to hear their favourite characters sing their favourite song.
# Usage
* Download voice models
```
python download_models.py

```
* You can run predictions:
```
cog predict -i audio=@https://www.youtube.com/watch?v=YVkUvmDQ3HY

```
* Output :

  song_output/output.mp3
# Input Parameters
* 'voice_model' : custom, 
2pac, 
adele, 
alvin, 
ariana-grande, 
baby, 
biden, 
billie-eilish, 
britney-spears, 
craig-tucker, 
darthvader, 
drake, 
elon-musk, 
eminem, 
freddie-mercury, 
justin-beiber, 
kanye, 
kurt-cobain, 
lisa-simpsons, 
megatron, 
miley-cyrus, 
mj-raspy, 
mrbeast, 
mrkrabs, 
mrohare, 
obama, 
pikachu, 
plankton, 
rihanna, 
selena-gomez,
siri, 
spongebob-squarepants, 
squidward, 
stewie-griffin, 
tate, 
taylor-swift, 
the-weeknd, 
travis-scott, 
trump, 
villager, 
xxxtentacion.
* 'audio' : Youtube link.
* 'custom_voice_model_link':Custom voice model link.
