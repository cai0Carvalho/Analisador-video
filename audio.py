import sys
from pytubefix import YouTube
import ffmpeg
import openai
import os 

openai.api_key=os.getenv("OPENAI_API_KEY")

def resumirVideo():

    # Baixar áudio
    url = sys.argv[1]
    filename = "audio.wav"

    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    stream_url = audio_stream.url
    ffmpeg.input(stream_url).output(filename, format='wav', loglevel="error").run()

    # Transcrever audio
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe(model="whisper-1", file = audio_file)

    # Revisão
    completion = openai.ChatCompletion.create(
        model ="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": """
                    Você é um profissional que resume vídeos detalhadamente e de forma sucinta. 
                    Responda com formatação Markdown 
             """},
             {"role": "user", "content": f"Descreva o seguinte vídeo {transcript['text']}"}
        ]
    )
    with open("resumo.md", "w+", encoding="utf-8") as md:
        md.write(completion["choices"][0]["message"]["content"])

if __name__ == "__main__":
    resumirVideo()