# Load imports 
import os
from dotenv import load_dotenv
from openai import OpenAI   # So we can use the open api whisper model to capture my speach.
from pathlib import Path    # Then us this to save the audit to a file and return the path
import gradio as gr

# Get the open API key
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# connect to open AI
openai_client = OpenAI(api_key=OPENAI_KEY)

# Create the function to convert my recorded audio to text. 
def transcribe_audio(audio):
    audio_file = Path(audio)  # Save the audio to a file
    # Create the transcriber and convert the audio to text
    transcriber = openai_client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    # and return to the caller
    transcription = transcriber.text
    return transcription

# This function is in the format expected by the Gradio submit_button.click per below 
#   submit_button.click(fn = notes_from_audio, inputs=[audio_input], outputs=[transcription]) code below. 
# It is passed the audio I previously recorded. The function transcribes it then converts it to notes. 
def notes_from_audio(audio=None):
    transcription = transcribe_audio(audio)

    SYSTEM_PROMPT_MESSAGE = "You are an expert notetaker, use the following transcription from my audio to generate "
    SYSTEM_PROMPT_MESSAGE += "notes based on it. Make sure to keep these brief using bullet points."
    prompt = SYSTEM_PROMPT_MESSAGE + "/nTranscription/n" + transcription
    message = [{'role':'user','content':prompt}]

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",    # Use the mini version as it is more cost effective
        messages=message,       # the audio
        max_tokens=100,         # the max length of the response
        temperature=0.7         # the higher the temp the more creative the response. the lower the temp the more precise the response 
                                # which means your are more likely to get the same response for the same prompt
    )
    # It looks like this. 
    # ChatCompletion(id='chatcmpl-CR6SEm8gzlKrpBUx7pdLGP2FKMzAR', 
    #       choices=[Choice(finish_reason='stop', index=0, logprobs=None, 
    #           message=ChatCompletionMessage(content='- Testing audio recording for text conversion\n- Objective: Summarize recording into . . .)))
    # So unpick as follows: -
    notes = response.choices[0].message.content
    return notes, transcription


# Break the application into blocks.
with gr.Blocks() as demo:
  # will create 3 rows in the block. The first captures the audio. 
  with gr.Row():
    audio_input = gr.Audio(sources=["upload","microphone"], type="filepath", label="Audio Transcriber")
  
  # The second is two text boxes to hold the notes and transcriptions. The text box objects are saved to the variables
  # transcription and notes so they can be referenced by the submit button. 
  with gr.Row(height=500):
    transcription = gr.Textbox(label="Transcription", lines=10)
    notes = gr.Textbox(label="Notes", lines=10)

  # The thrid is a submit button that takes the audio above, converts it to text and summarizes that text into notes.
  # It then saves the text into the notes and transcription fields above. The outputs references the text box by its label
  with gr.Row():
    submit_button = gr.Button("Start")
    submit_button.click(fn = notes_from_audio, inputs=[audio_input], outputs=[notes, transcription])

demo.launch()