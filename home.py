import os
import time

import openai
from dotenv import load_dotenv
from colorama import Fore, Style


def check_run(client, thread_id, run_id):
    while True:
        # Refresh the run object to get the latest status
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )

        if run.status == "completed":
            print(f"{Fore.GREEN} Run is completed.{Style.RESET_ALL}")
            break
        elif run.status == "expired":
            print(f"{Fore.RED}Run is expired.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.YELLOW} OpenAI: Run is not yet completed. Waiting...{run.status} {Style.RESET_ALL}")
            time.sleep(1)  # Wait for 1 second before checking again


def chat_loop(client, assistant, thread):
    while True:
        # Input from user

        user_input = input(f"{Fore.CYAN} User: ")
        print(Style.RESET_ALL)

        if user_input == "quit":
            break

        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_input
        )

        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )

        check_run(client, thread.id, run.id)

        # Get the latest messages from the thread
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )

        # Get the latest message from the user
        user_message = messages.data[1].content[0].text.value

        # Get the latest message from the assistant
        assistant_message = messages.data[0].content[0].text.value

        # Print the latest message from the user
        # print(f"{Fore.CYAN} User: {user_message} {Style.RESET_ALL}")

        # Print the latest message from the assistant
        print(f"{Fore.BLUE} Assistant: {assistant_message} {Style.RESET_ALL}")


def main():
    load_dotenv(override=True, dotenv_path=".env")  # take environment variables from .env.
    openai.api_key = os.getenv("OPENAI_API_KEY")

    client = openai.Client()

    print(f"{Fore.MAGENTA} Welcome to the Python Tutor. I am here to help you learn python...{Style.RESET_ALL}\n")
    print(f"{Fore.MAGENTA} You can start by typing, for example,  'start with a simple exercise' {Style.RESET_ALL}\n")
    print(f"{Fore.MAGENTA} You can type `quit` to exit ...{Style.RESET_ALL}\n")

    assistant = client.beta.assistants.create(
        name="Python Tutor",
        instructions="You are a personal Python tutor. You are teaching a high-school student learn Python. Track the "
                     "user progress and assign new exercises as the user progresses.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-1106-preview"
    )

    thread = client.beta.threads.create()

    chat_loop(client, assistant, thread)


if __name__ == "__main__":
    main()
