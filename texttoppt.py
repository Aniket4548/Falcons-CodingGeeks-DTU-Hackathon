import openai
import os

# Set up OpenAI API credentials
def generated_text(query):
    openai.api_key = "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"
    
    # global query
    # query =  input("enter the name of topic: ")
# Set the prompt for the presentation
    prompt = '''Create a presentation  {} with slide number and its content in paragraph of 50 words with 12 slides
                '''.format(query)

# Generate the presentation text using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6,
        #frequency_penalty = 0,
        presence_penalty = 1,
    )

    presentation_text = response.choices[0].text

    return presentation_text.lower()
