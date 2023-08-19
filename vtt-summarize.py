import openai
import json
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# set API key
openai.api_key = os.getenv("OPENAI_API_KEY")
print("API Key:", os.getenv("OPENAI_API_KEY"))

# read VTT file
def read_clean_file(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        # Read the contents of the file into a string
        file_contents = file.read()
        
    # Split the string into lines
    lines = file_contents.split('\n')

    # Check if the first line is "WEBVTT" and remove it if so
    if lines[0].strip() == "WEBVTT":
        lines = lines[1:]

    # Join the remaining lines back into a string
    cleaned_contents = '\n'.join(lines)
    
    # Remove the timestamps using regular expression
    cleaned_contents = re.sub(r'\d{2}:\d{2}:\d{2}\.\d{3}\s-->\s\d{2}:\d{2}:\d{2}\.\d{3}\n', '', cleaned_contents)
    
    # Define the regular expression pattern for the hashes
    pattern = r'\b[a-f0-9]{8}(?:-[a-f0-9]{4}){3}-[a-f0-9]{12}-\d\b'

    # Remove the hashes from the content using the sub() method
    cleaned_contents = re.sub(pattern, '', cleaned_contents)
    
    # Split the string into paragraphs using double newline
    paragraphs = cleaned_contents.split('\n\n')

    # For each paragraph, split by newlines, strip, and join
    processed_paragraphs = [' '.join([line.strip() for line in paragraph.split('\n') if line.strip()]) for paragraph in paragraphs]

    # Join the processed paragraphs using a single newline
    cleaned_contents = '\n'.join(processed_paragraphs)

    return cleaned_contents

# Will batch the calls into a single API call
def summarize_vtt(vtt_string):
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="%s - Given the following VTT file, give a bulleted list summarization of the conversation"%vtt_string
    ) 
    
    return response['choices'][0]['text']

# Specify the file path
file_path = 'samples/algoConvo.vtt'

# Call the function to read the file into a string
file_string = read_clean_file(file_path)

summarization = summarize_vtt(file_string)

print(summarization)