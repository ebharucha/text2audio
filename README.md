1. Execute "**pip install -r requirements.txt**" from a command shell.
2. Create a "**.env**" file in the current directory as the text2audio.py script and set the<br>
   "**OPENAI_API_KEY**" variable to your OpenAI API key<br>
   "**ELEVENLABS_API_KEY**" variable to your ElevenLabs API key
3. Uncomment either the "**audiogen_openai**" or "**audiogen_elevenlabs**" function under main depending on your preference.
4. Modify the voice parameter under the "**audiogen_openai**" or "**audiogen_elevenlabs**" functions as appropriate.
5. Script usage "usage: text2audio.py [-h] --textfile FILE"
7. The associated mp3 audio file will be generated and stored under the "**data/audio/**" directory.

Ed Bharucha<br>
@ebharucha
