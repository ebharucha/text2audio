1. Execute "**pip install -r requirements.txt**" from a command shell.
2. Create a "**.env**" file in the current directory as the text2audio.py script and set the
   "**OPENAI_API_KEY**" variable to your OpenAI API key
   "**ELEVENLABS_API_KEY**" variable to your ElevenLabs API key
3. Uncomment either the "**audiogen_openai**" or "**audiogen_elevenlabs**" function under main depending on your preference.
4. Modify the voice parameter under the "**audiogen_openai**" or "**audiogen_elevenlabs**" functions as appropriate.
5. Store the text file to covert to audio under the "**data/text/**" directory.
6. Set the "**input_file**" variable to the "**text file name**" <ins>without</ins> the .txt extension.
7. The associated mp3 audio file will be generated and stored under the "**data/audio/**" directory.

Ed Bharucha
@ebharucha
