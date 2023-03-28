import os
import openai

# Function to save the content to a file
def save_file (filepath, content):
  with open (filepath,'w', encoding='utf-8') as outfile:
    outfile.write (content)
# Set the OpenAI API key from a file
openai.api_key = os.getenv("OPENAI_API_KEY")
# Open the audio file that needs to be transcribed
audio_file = open ("../data/gptAmj5vo.mp3", "rb")
# Define your prompt text
prompt_text = "GPT-4 and Midjourney V5 are the models used"
# Transcribe the audio file using the OpenAl Whisper API with the provided prompt
transcript = openai.Audio.transcribe("whisper-1", audio_file, prompt=prompt_text)
# Save the transcription to a text file
save_file ("../data/gpt4mj5.txt" , transcript.text)