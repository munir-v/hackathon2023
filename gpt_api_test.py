#!/usr/bin/env python3
import os
import openai
import constants

# Set up the OpenAI API client
api_key = constants.GPT_API_KEY
openai.api_key = api_key

def ask_gpt(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{question}\nAnswer:",
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = response.choices[0].text.strip()
    return answer


if __name__ == "__main__":
    # question = input()
    question = str(os.environ["KMVAR_GPTprompt"])
    answer = ask_gpt(question)
    print(answer)