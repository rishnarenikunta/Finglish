import time
import PyPDF2
import re
import requests
import json
import openai


# Initialize empty arrays for words and definitions
words = []
definitions = []

# Open the PDF file in binary mode
pdf_file_path = 'new-york-apartment-residential-lease-agreement-form.pdf'
pdf_file = open(pdf_file_path, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Initialize an empty string to store the extracted text
text = ''

# Iterate through each page in the PDF
for page_num in range(len(pdf_reader.pages)):
    # Get a specific page

    page = pdf_reader.pages[page_num]

    # Extract text from the page
    page_text = page.extract_text()

    # Append the page text to the overall text
    text += page_text

# Close the PDF file
pdf_file.close()

# Save the extracted text to a text file
text_file_path = 'output_text.txt'
with open(text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(text)

# Print a confirmation message
print(f'Text extracted from PDF and saved to {text_file_path}')

#split the textfile into segments
segments = text.split('\n ')
# for segment in segments:
#     print ("segment: " + segment)


#checks if a segments has more than 50 letters
def has_more_than_50_letters(s):
    #variable to count the number of letters
    letter_count = 0

    for char in s:
        if char.isalpha():
            letter_count += 1

    return letter_count > 50

#sets the language to whatever language the user wants
language = 'hindi'
# Set your API key
openai.api_key = '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'

# Set the endpoint
api_url = 'https://api.openai.com/v1/chat/completions'

# Define the model
model = 'text-davinci-003'

#Print when done with numbers to label the chunks.
# Define your prompt
# print("before")
# for segment in segments:
#     print(segment)

#delete segments that have less than 50 letters to make it easier to send it through the API
i = 0;
for segment in segments:
    if (not has_more_than_50_letters(segment)):
        #print('deleted ' + segments[i])
        del segments[i]
        i = i - 1
    i = i + 1

#our model limits the amount of chatGPT responses to 3/min so we're tracking the amount of responses
credits = 0
index = 0
#array for responses
savedResponses = []
#combine multiple segments into one segment
while index < len(segments) - 5:
        # Access the current element and the next element
        current_element = segments[index]
        next_element = segments[index + 1]
        next_element2 = segments[index + 2]
        next_element3 = segments[index + 3]
        next_element4 = segments[index + 4]
        current_element = current_element + next_element + next_element3 + next_element2 + next_element4
        #print (current_element)
        index = index + 5

        #make the prompt to send chatGPT API
        prompt = 'You are a a bank teller. Simplify this text ' + current_element + 'and give me the answer ' + language

        #sends prompt to chatGPT API
        completion = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )

        #saves response by API into an array called savedResponses
        response = completion.choices[0].text
        savedResponses.append(response)
        #print(response)
        credits = credits + 1

        #ensures we aren't going over the chatGPT restriction
        if( credits > 2):
            time.sleep(60)
            credits = 0

#iterates through the segments in savedResponses
for segment in savedResponses:
    print (segment)

def extraQuestions(question, textSegment):
    prompt = 'You are a bank teller. Give me an answer to this question in ' + language + ' :' + question + ' based off of this text segment : ' + textSegment

    completion = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

def storeVocabWords():

    with open('your_file.txt', 'r') as file:
        lines = file.readlines()

    # Process the lines to extract words and definitions
    for i in range(0, len(lines), 4):
        word = lines[i].strip()  # Remove leading/trailing whitespace
        definition = lines[i + 2].strip()  # Remove leading/trailing whitespace

        words.append(word)
        definitions.append(definition)

def getWord(word):
    if word in words:
        index = words.index(word)
        return definitions[index]
    else:
        return 'This definition is not in our index yet'


