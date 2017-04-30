import json
import requests
import cfg

c = cfg.read_cfg()

sub_id = c['txtkey']


headers = {"Ocp-Apim-Subscription-Key": sub_id,
           "Content - Type": "application / json",
           "Accept": "application / json"}

uri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/'

sent = uri + 'sentiment'
keyphrase = uri + 'keyPhrases'
lang = uri + 'languages'

comments = ['Great site.  Maybe free shipping for items over 49 dollars for all of us steady repeat customers.   Sometimes I have to wait for the shipping specials then I change my mind and do not order',
            'The prices for most products are reasonable.  There are options for all pricing levels in most categories.  Shipping charges seem a bit high though.']


def send_docs(msc=sent, headers=headers, docs=docs):

    r = requests.post(msc, headers, data=docs)
    score = r.json()

    return score


def build_docs(sententences):

    doclist = []
    id = 1000
    for sentence in sententences:
        id += 1
        item = {"language": "en",
                "id": id,
                "text": sentence}
        doclist.append(item)
    docs = {"documents": doclist}

    return docs


def main():
    docs = build_docs(comments)
    score = send_docs(msc=sent, headers=headers, docs=docs)
    print(score)


if __name__ == '__main__':
    main()
