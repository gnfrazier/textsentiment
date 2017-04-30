import json
import cfg

c = cfg.read_cfg()

sub_id = c['txtkey']

key = "Ocp-Apim-Subscription-Key:" + sub_id
content = "Content - Type: application / json"
accept = "Accept: application / json"
