#!/usr/bin/python3

import requests
import configparser
import json

cfg = configparser.ConfigParser()
cfg.read('config.ini')

sub_id = cfg['cognitive']['key']


headers = {"Ocp-Apim-Subscription-Key": sub_id,
           "Content-Type": "application/json",
           "Accept": "application/json"}

uri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/'

# testuri = 'http://headers.jsontest.com/'


sent = uri + 'sentiment'
# sent = testuri
keyphrase = uri + 'keyPhrases'
lang = uri + 'languages'

# Sample sentences
comments = ['I am so happy', 'I am so mad', 'I dont know how I feel']


def send_docs(data, msc=sent, headers=headers):
    '''Post json to URL passed as msc.'''

    r = requests.post(msc, headers=headers, data=data)
    score = r.json()

    return score


def build_docs(sententences, id=1000):
    '''Produce json message body from list of sententences.'''

    doclist = []

    for sentence in sententences:
        id += 1
        item = {"language": "en",
                "id": id,
                "text": sentence}
        doclist.append(item)
    docs = {"documents": doclist}
    docs = json.dumps(docs)

    return docs


def test_docs(doc=None, msc=None, headers=None):
    '''A score for 3 sentences for dev to reduce api calls.'''

    score = {'documents': [{'id': '1001', 'score': 0.971985986240645}, {
        'id': '1002', 'score': 0.048940735444031},
        {'id': '1003', 'score': 0.144271018300534}], 'errors': []}

    return score


def main():
    doc = build_docs(comments)

    score = send_docs(doc, msc=sent, headers=headers)
    print(score)


if __name__ == '__main__':
    main()
