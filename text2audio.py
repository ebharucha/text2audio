###########################
# ebharucha, 6/4/2025
###########################

import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
import elevenlabs

def split_text_into_chunks(text, max_chars=4000):
    """Split text into chunks of maximum size."""
    chunks = []
    current_chunk = ""
    
    # Split by sentences (roughly)
    sentences = text.replace('\n', '. ').split('. ')
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_chars:
            current_chunk += sentence + '. '
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + '. '
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

# Generate audio via OpenAI text to audio
def audiogen_openai(OPENAI_API_KEY, input_file, AUDIO_OUTPUT_DIR, content):
    client = OpenAI(api_key=OPENAI_API_KEY)  # Requires API key
    
    # Split content into chunks
    chunks = split_text_into_chunks(content)
    
    # Process each chunk
    for i, chunk in enumerate(chunks):
        with client.audio.speech.with_streaming_response.create(
            model="tts-1", 
            # Available voices:
            # - alloy: A balanced, neutral voice
            # - echo: A warm, friendly voice
            # - fable: A clear, professional voice
            # - onyx: A deep, authoritative voice
            # - nova: A bright, energetic voice
            # - shimmer: A soft, gentle voice
            voice="nova",  # You can change this to any of the voices listed above
            input=chunk,
            speed=0.9  # Slower speed (0.25 to 4.0, where 1.0 is default)
        ) as response:
            # Save each chunk with a number suffix
            chunk_file = f'{AUDIO_OUTPUT_DIR}/{input_file}_part{i+1}.mp3'
            response.stream_to_file(chunk_file)
            print(f"Generated audio for chunk {i+1}/{len(chunks)}")

# Generate audio via ElevenLabs text to audio
def audiogen_elevenlabs(ELEVENLABS_API_KEY, input_file, AUDIO_OUTPUT_DIR, content):
    elevenlabs.set_api_key(ELEVENLABS_API_KEY)
    # Generate audio using ElevenLabs
    audio = elevenlabs.generate(
        text=content,
        voice="ERB",
        model="eleven_monolingual_v1"
    )
    # Save the audio
    with open(f"{AUDIO_OUTPUT_DIR}/{input_file}.mp3", "wb") as f:
        f.write(audio)

def main():
    # load .env file to environment
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process a text file')
    parser.add_argument('--textfile', required=True, 
                       help='Path to the input text file', metavar='FILE')
    # Parse arguments
    args = parser.parse_args()
    
    # Check if file has .txt extension
    if not args.textfile.lower().endswith('.txt'):
        print("Error: Input file must be a text file with a .txt extension")
        exit(1)
    
    # Extract base filename without extension
    input_filename = os.path.splitext(os.path.basename(args.textfile))[0]
        
    # Process the file
    try:
        with open(args.textfile, 'r') as file:
            content = file.read()
            print(f"Successfully read file: {args.textfile}")
    except FileNotFoundError:
        print(f"Error: File '{args.textfile}' not found")
        exit(1)
    except PermissionError:
        print(f"Error: No permission to read '{args.textfile}'")
        exit(1)
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        exit(1)

    AUDIO_OUTPUT_DIR = "data/audio"
    os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)  # Ensure dir exists
    
    audiogen_openai(OPENAI_API_KEY, input_filename, AUDIO_OUTPUT_DIR, content)
    # audiogen_elevenlabs(ELEVENLABS_API_KEY, input_filename, AUDIO_OUTPUT_DIR, content)

if __name__ == "__main__":
    main()

