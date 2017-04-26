from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
from azure.common.credentials import UserPassCredentials
import cfg

c = cfg.read_cfg()

subscription_id = c['txtkey']
