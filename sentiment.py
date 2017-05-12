#!/usr/bin/python3

import requests
import configparser
import json


cfg = configparser.ConfigParser()
cfg.read('config.ini')

sub_id = cfg['cognitive']['key']

# Sample sentences
cdict = {'1001': 'I am so happy', '1002': 'I am so mad',
         '1003': 'I dont know how I feel'}
# testuri = 'http://headers.jsontest.com/'
# sent = testuri


def get_headers():
    '''Default headers with sub_id from global value'''

    headers = {"Ocp-Apim-Subscription-Key": sub_id,
               "Content-Type": "application/json",
               "Accept": "application/json"}
    return headers


def get_url(scoretype):
    '''Create URL based on query type'''

    uri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/'

    stype = {'sent': uri + 'sentiment',
             'keyphrase': uri + 'keyPhrases',
             'lang': uri + 'languages'}
    url = stype[scoretype]
    return url


def send_docs(data, stype=None, url=None, headers=None):
    '''Post json to URL passed as data'''

    if not headers:
        headers = get_headers()

    if not stype:
        stype = 'sent'  # sentiment is default

    if not url:
        url = get_url(stype)

    req = requests.post(url, headers=headers, data=data)
    score = req.json()

    return score


def build_docs(cdict):
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


def test_phrase():
    '''Keyphrases for 3 sentences for dev to reduce api calls'''

    phrase = {'errors': [], 'documents': [
        {'keyPhrases': ['happy'], 'id': '1001'},
        {'keyPhrases': ['mad'], 'id': '1002'},
        {'keyPhrases': ['dont'], 'id': '1003'}]}

    return phrase


def parse_score(score, stype, review=None):
    '''Take documents and return score or phrases as dict with id as key'''

    if not review:
        review = {}

    stype_ref = {'sent': 'score',
                 'keyphrase': 'keyPhrases', 'lang': 'language'}
    ref = stype_ref[stype]
    for result in score['documents']:
        review[result['id']] = result[ref]

    return review


def main():
    stype = 'keyphrase'
    doc = build_docs(cdict)
    score = send_docs(doc, stype)
    print(score)
    parsed = parse_score(score, stype)
    print(parsed)


if __name__ == '__main__':
    main()
