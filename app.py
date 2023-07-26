"""Import the necessary libraries including the dotenv library in order to access the .env file in the local packages"""

import os
from dotenv import load_dotenv
from b2sdk.v2 import InMemoryAccountInfo, B2Api

####Load the components stored in the .env file so that they can be accessed on this page
load_dotenv()


### Instantiate the InMemoryAccountInfo so that BackBlaze Database can call the API to load the login information
info = InMemoryAccountInfo() 
b2_api = B2Api(info)


###Add the application key_id and key from the .env file so the api can log into the correct bucket
application_key_id = os.environ.get("B2_APP_KEY_ID")
application_key = os.environ.get("B2_APP_KEY")
b2_api.authorize_account("production", application_key_id, application_key) 

###Create the connection to the bucket within the backblaze account
ig_scheduler_bucket = b2_api.get_bucket_by_name("Test-Instagram-Photo-Bucket")


### Temporary photo location for testing of backblaze account to see if bucket and api is connected
local_file_path = "/Users/ryanmccoy/Aether/EM-Flywheel.png"
b2_file_name = "EM-Flywheel.png"
file_info = {"how": "good-file"}


"""
API Connection to upload the photo
Takes in 4 things:
1) The bucket location listted above as 'ig_scheduler_bucket'
2) local_file = the location of the photo you want to upoad
3) file_name = the name of the photo for easy read on the database side
4) file_infos = extra information to be stored with the photo - given in dictionary form

"""
bucket = ig_scheduler_bucket
bucket.upload_local_file(
    local_file = local_file_path,
    file_name = b2_file_name,
    file_infos = file_info,
)
