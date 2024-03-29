# Python Tutor with OpenAI Assistant API

Python Tutor is a command-line interface program that acts as a personal Python tutor, utilizing the OpenAI Assistant API to interactively teach Python programming.

You can type your Python programs in the terminal and get real-time feedback from the tutor. The tutor will also suggest new exercises based on your progress.

## Description

This program creates a personalized Python learning session, leveraging OpenAI's Assistant API to provide real-time tutoring for Python learners. It is designed for high school students or anyone starting with Python. The tutor tracks user progress and suggests new exercises as the user advances.

## Features

- Interactive CLI for a personalized Python tutoring experience.
- Real-time feedback and exercise suggestion based on user input.
- Use of OpenAI's powerful Assistant API to simulate a Python tutor.

## Installation

To install the required dependencies, navigate to the project directory and run:

```bash
pip3 install -r requirements.txt
```

### Environment Variables
To run this project, you will need to add the following environment variables to your .env file:

OPENAI_API_KEY=Your OpenAI API key.

## Usage
To start the tutoring session, run the following command in your terminal:

```bash
python3 home.py
```

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## License
This project is licensed under the Apache License v2.0. See the LICENSE file for more details.

## TODO

Create a nice Streamlit wrapper like in https://github.com/BenderScript/VidBot

