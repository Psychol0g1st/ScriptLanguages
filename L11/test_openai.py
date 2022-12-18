#!/usr/bin/env python3

import os
from pprint import pprint
import sys
import openai
from yachalk import chalk

def get_response(prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    text = response["choices"][0]["text"]  # type: ignore
    return text


def main():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    
    while True:
        try:
            question = input(chalk.bold("gpt3> "))
            if question != "":
                response = get_response(question)
                if(response != ""):
                    print("Answer:")
                    print(response)
                    question = response
        except KeyboardInterrupt as e:
            print("end")
            sys.exit(0)

##############################################################################

if __name__ == "__main__":
    main()