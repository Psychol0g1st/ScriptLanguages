import requests
import json


def main():
    response = requests.get("https://jsonip.com/")
    deserialized = json.loads(response.text)
    print(f"Az ÖN IP címe: {deserialized['ip']}")


if __name__ == "__main__":
    main()
