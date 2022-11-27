#!/usr/bin/env python3

import os
from pprint import pprint
import sys
import openai


def get_response(prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-002",
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
    question = input("First question:\n")
    print("-------------------------------------")
    while True:
        try:
            response = get_response(question)
            if(response != ""):
                print("\n-------------------------------------\n")
                pprint(response)
                question = response
        except KeyboardInterrupt as e:
            print("end")
            sys.exit(0)


##############################################################################

if __name__ == "__main__":
    main()