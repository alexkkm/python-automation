import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Check API key BEFORE initializing client
api_key = os.getenv("openrouter_api_key")   # please ensure you create the .env file and add your OpenRouter API key as openrouter_api_key="YOUR_API_KEY"

# Check if API key is found
if not api_key:
    print("Error: API key not found in environment variables.")
    sys.exit(1)

# Initialize OpenRouter client with verified key
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

# Function to call OpenRouter to correct grammar in a text file
def correct_grammar(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if not text.strip():
        print("File is empty.")
        return
    # Call OpenRouter API to correct grammar, provide the instructions to the model so that it knows what to do with the text
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": "You are a grammar correction assistant. Improve grammar and correct the misspelled words while preserving meaning. Return ONLY corrected text."},
            {"role": "user", "content": text}
        ],
        temperature=0.3,
    )
            
    corrected = response.choices[0].message.content
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(corrected)
            
    print(f"Saved corrected text to: {output_path}")
            
# Main function
if __name__ == "__main__":

    # Define input and output file paths
    input_file = "./input.txt"
    output_file = "./output.txt"

    if os.path.isfile(input_file):
        correct_grammar(input_file, output_file)
    else:
        print(f"File not found: {input_file}")