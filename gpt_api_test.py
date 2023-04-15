#!/usr/bin/env python3
import os
import openai
import constants

# Set up the OpenAI API client
api_key = constants.GPT_API_KEY
openai.api_key = api_key

# def ask_gpt(question):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=f"{question}\nAnswer:",
#         temperature=0.7,
#         max_tokens=500,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )

#     answer = response.choices[0].text.strip()
#     return answer

def generate_text(query):
    response = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo", 
        messages=[ 
        {"role": "system", 
         "content": "You are a helpful assistant."}, 
         {"role": "user", "content": query} 
        ] 
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # question = input()
    # answer = ask_gpt(question)
    question = str(os.environ["KMVAR_GPTprompt"])
    # question = "Who are you?"
    answer = generate_text(question)
    print(answer)