# app 
import Utilities.sensitive_data as sensitive_data

DEBUG=True

gamemode_dict={ 1: "osu", 2:"taiko", 3:"catch", 4:"mania" }
job_status={ 0: "invalid", 1: "pending", 2: "downloading", 3: "downloaded" } # Used to text progress of jobs
# for hardcoded things
if DEBUG:
    oauth_client_id=sensitive_data.oauth_client_id
    oauth_client_secret=sensitive_data.oauth_client_secret