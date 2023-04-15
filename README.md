# GPT Genius

## Background

### Inspiration
The inspiration behind developing GPT Genius came from a desire to utilize the powerful capabilities of GPT for the benefit of students. GPT has the ability to perform many natural language processing tasks, such as summarizing text, correcting grammar, and translation. With the help of this GUI desktop app, students can fully take advantage of GPT.

### What it does
The app provides the ability to quickly and easily receive help from GPT via a keyboard shortcut. For example, the user can highlight a passage of text on the screen, press the keyboard shortcut to activate the app, then select "Summarize in one paragraph." The app then copies the highlighted text and returns a response in a new window with the summarized response.

### How it was built
To build this project, I used Python as the primary programming language. I used Keyboard Maestro, a macro and automation app for Mac that provides GUI capabilities, to create a user-friendly interface for the app. Python was used to handle the GPT API requests and to process the responses, while Keyboard Maestro was used to create a simple and intuitive interface for users to interact with.

## Setup and Requirements

1. You will need an [API key](https://platform.openai.com/account/api-keys) from OpenAI to use this app.

2. To use GPT Genius, first clone this repo onto your computer. You will also need to install [Keyboard Maestro](https://www.keyboardmaestro.com/main/) and download the Keyboard Maestro [macro that runs the GUI](). Once Keyboard Maestro is installed, open the macro file. It should appear automatically in Keyboard Maestro. 

2. The macro may appear to be greyed out in the list of macros. If that is the case, simply right-click on it and select "enable macro".

3. Open the cloned repository, and create a new file called `constants.py` in the root directory. This file should contain one line as follows: `GPT_API_KEY = ""`. In the quotes, paste your API key from step 1.

4. Scroll down in the macro file until you see the action below the "CHANGE THIS PATH" comment. Replace the file path in the action with the local directory of `gpt_api_call.py`, which appears in the repo you cloned previously.

4. You are all set! Press the keyboard shortcut `cmd+opt+ctrl+p` to start using GPT Genius.