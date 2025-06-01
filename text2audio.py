import os
from dotenv import load_dotenv
from openai import OpenAI
import elevenlabs

# Generate audio via OpenAI text to audio
def audiogen_openai(OPENAI_API_KEY, input_file, content):
    client = OpenAI(api_key=OPENAI_API_KEY)  # Requires API key
    with client.audio.speech.with_streaming_response.create(
        model="tts-1", 
        # Available voices:
        # - alloy: A balanced, neutral voice
        # - echo: A warm, friendly voice
        # - fable: A clear, professional voice
        # - onyx: A deep, authoritative voice
        # - nova: A bright, energetic voice
        # - shimmer: A soft, gentle voice
        voice="echo",  # You can change this to any of the voices listed above
        input=content,
        speed=0.9  # Slower speed (0.25 to 4.0, where 1.0 is default)
    ) as response:
        response.stream_to_file(f'data/audio/{input_file}.mp3')

# Generate audio via ElevenLabs text to audio
def audiogen_elevenlabs(ELEVENLABS_API_KEY, input_file, content):
    elevenlabs.set_api_key(ELEVENLABS_API_KEY)
    # Generate audio using ElevenLabs
    audio = elevenlabs.generate(
        text=content,
        voice="ERB",
        model="eleven_monolingual_v1"
    )
    # Save the audio
    with open("data/audio/elevenlabs.mp3", "wb") as f:
        f.write(audio)

def main():
    # load .env file to environment
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    input_file = "Post1-AI_ML_DL_LLMs" # Provide name of the input text file without the .txt extension
    with open(f'data/text/{input_file}.txt', "r") as file:
        content = file.read()
    audiogen_openai(OPENAI_API_KEY, input_file, content)
    # audiogen_elevenlabs(ELEVENLABS_API_KEY, content)

if __name__ == "__main__":
    main()

