from ..config import load_RNC_token, load_corpus_settings
import requests


TOKEN = load_RNC_token()
DATE_START = load_corpus_settings().DATE_START
DATE_END = load_corpus_settings().DATE_END
SUBCORPUS = load_corpus_settings().RNC_SUBCORPUS

def get_concordance(word, corpus=SUBCORPUS):
    url = "https://ruscorpora.ru/api/v1/lex-gramm/concordance"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    request_body = {
        "corpus": {"type": corpus},
        "lexGramm": {
            "sectionValues": [
                {
                    "subsectionValues": [
                        {
                            "conditionValues": [
                                {"fieldName": "lex", "text": {"v": word}}
                            ]
                        },
                        {
                            "conditionValues": []
                        }
                    ]
                }
            ]
        },
        "format": "json",
        "size": 10
    }

    response = requests.post(url, json=request_body, headers=headers)

    return response

if __name__ == "__main__":

    data = get_concordance("тензор").json()


    print(data.get("queryStats"))
    print(data.get("subcorpStats"))
    print(data.get("corpusStats"))
    print(data.keys())
    # print(TOKEN)