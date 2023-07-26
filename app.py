import os
from dotenv import load_dotenv
from b2sdk.v2 import InMemoryAccountInfo, B2Api

info = InMemoryAccountInfo() 
b2_api = B2Api(info)

application_key_id = '4a5b6c7d8e9f'
application_key = '001b8e23c26ff6efb941e237deb182b9599a84bef7'
b2_api.authorize_account("production", application_key_id, application_key)