# data provider (store variables, hardcode things and functions to get and set data)
import entity
import Utilities.constants as constants

from Tests import fake_provider as fake

# Credentials
OAUTH_TOKEN=None

# Lists
MappackJson=None
TournamentJson=None

# data (singletons)
Sources=entity.Sources()
Jobs=entity.Jobs()
Settings=entity.Settings()

# User toggles
cancel_jobs_toggle=False

# Use these test functions below for testing purposes
# The sources tab will only display the mock data when DEBUG=True
# Adding things will add to the actual data, but it is not shown

def get_sources():
    if constants.DEBUG:
        return fake.Sources
    else:
        return Sources

def get_jobs():
    if constants.DEBUG:
        return fake.Jobs
    else:
        return Jobs
        
def get_settings():
    if constants.DEBUG:
        return fake.Settings
    else:
        return Settings