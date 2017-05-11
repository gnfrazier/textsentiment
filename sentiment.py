#!/usr/bin/python3

import requests
import configparser
import json
from collections import namedtuple

cfg = configparser.ConfigParser()
cfg.read('config.ini')

sub_id = cfg['cognitive']['key']


def get_headers():
    headers = {"Ocp-Apim-Subscription-Key": sub_id,
               "Content-Type": "application/json",
               "Accept": "application/json"}
    return headers


def get_url(scoretype):
    '''This function is not working'''

    uri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/'
    module = namedtuple('module', ['sent', 'keyphrase', 'lang'])

    stype = module(sent=uri + 'sentiment',
                   keyphrase=uri + 'keyPhrases',
                   lang=uri + 'languages')
    url = stype.scortype
    return url


# Sample sentences
cdict = {'1001': 'I am so happy', '1002': 'I am so mad',
         '1003': 'I dont know how I feel'}
# testuri = 'http://headers.jsontest.com/'
# sent = testuri


def send_docs(data, url=None, headers=None):
    '''Post json to URL passed as msc.'''

    if not headers:
        headers = get_headers()

    if not url:
        url = get_url(sent)  # sentiment is default

    req = requests.post(url, headers=headers, data=data)
    score = req.json()

    return score


def build_fdict(cdict):
    '''Produce json message body from dictionary of id : sentences.'''

    doclist = []
    for idnum, sentence in cdict.items():

        item = {"language": "en",
                "id": idnum,
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


def parse_score(score, review=None):
    if not review:
        review = {}

    for result in score['documents']:
        review[result['id']] = result['score']

    return review


def main():

    doc = build_fdict(cdict)
    score = send_docs(doc, msc=sent, headers=headers)
    print(score)
    parsed = parse_score(score)
    print(parsed)


if __name__ == '__main__':
    main()
