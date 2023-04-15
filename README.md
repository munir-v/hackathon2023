# hackathon2023

## Inspiration
The inspiration behind developing this app came from a desire to utilize the powerful capabilities of GPT for the benefit of students. GPT has the ability to perform many natural language processing tasks, such as summarizing text, correcting grammar, and translation. With the help of this GUI desktop app, students can fully take advantage of GPT.

## What it does
The app provides the ability to quickly and easily receive help from GPT via a keyboard shortcut. For example, 

## How we built it
To build this project, I used Python as the primary programming language. I used Keyboard Maestro, a macro and automation app for Mac that provides GUI capabilities, to create a user-friendly interface for the app. Python was used to handle the GPT API requests and to process the responses, while Keyboard Maestro was used to create a simple and intuitive interface for users to interact with.

## Challenges we ran into
The main challenge I faced during the development of this app was debugging the Python code. I encountered a few bugs while trying to make a receive calls from the GPT API, specifically, in trying to get the right model (gpt-3.5-turbo) to be used. Another challenge was getting Keyboard Maestro to pass the system clipboard to the Python script.

## What we learned
Developing this app taught me how to use the GPT API effectively. I learned how to integrate GPT into my code, send text inputs to the API, and handle the API's responses. I also learned how to parse the JSON data that is returned by the API. Finally, I improved my skills with making simple GUIs with Keyboard Maestro.

