import requests
import json
import sys


def main():
    word_id = input("Type A Word To Search: ").replace(" ", "%20")
    define = str(get_definition(word_id))
    print(f'The Definition: "{define}"', end="\n\n")
    jres = get_json(word_id)
    print(f"Word Used in a sentence: {get_example(jres)}", end="\n\n")
    try:
        get_synonyms(jres)
        print(f"Some synonyms for {word_id} are:", end=' "')
        print(*get_synonyms(jres), sep='" , "', end='" \n\n')
    except ValueError:
        print("This Word Has No Synonyms")
    try:
        get_antonyms(jres)
        print(f"Some antonyms for {word_id} are: ", end='"')
        print(*get_antonyms(jres), sep='" , "', end='" \n\n')
    except ValueError:
        print("This Word Has No Antonyms")


def get_json(word_id: str):
    app_id = "39dd753f"
    app_key = "e6ed01b484b0e689fd973232a092da75"
    # language = "en-gb"
    # word_id = 'enough'
    url = (
        "https://od-api.oxforddictionaries.com/api/v2/thesaurus/en-gb/"
        + word_id.lower().strip()
    )
    responce = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    jres = responce.json()
    if responce.status_code != 200:
        raise ValueError("This word has no synonyms or antonyms")
    return jres


def get_definition(word_id: str):
    app_id = "39dd753f"
    app_key = "e6ed01b484b0e689fd973232a092da75"
    responce = requests.get(
        "https://od-api.oxforddictionaries.com/api/v2/words/en-gb?q="
        + word_id
        + "&fields=definitions",
        headers={"app_id": app_id, "app_key": app_key},
    )
    if responce.status_code != 200:
        raise ValueError("Word not found")
    jres = responce.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    return jres["definitions"][0]


def get_synonyms(jres: dict) -> list:
    s = jres["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    synonyms = []
    try:
        s["synonyms"]
    except KeyError:
        raise ValueError("This Word Has No Synonyms")
    for result in s["synonyms"]:
        synonyms.append(result["text"])
    return synonyms


def get_antonyms(jres: dict):
    s = jres["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    antonyms = []
    try:
        s["antonyms"]
    except KeyError:
        raise ValueError("There are no antonyms for this word")
    for result in s["antonyms"]:
        antonyms.append(result["text"])
    return antonyms


def get_example(jres: dict) -> str:
    s = jres["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    example = s["examples"][0]["text"]
    return example


if __name__ == "__main__":
    main()


# print("code {}\n".format(r.status_code))
# print("json \n" + json.dumps(r.json(), indent = 1))

# print(json.dumps(o,indent = 2))
