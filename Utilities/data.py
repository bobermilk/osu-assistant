# data provider (store variables, hardcode things and functions to get and set data)
import entity
import Utilities.constants as constants

from Tests import fake_provider as fake

# data (singletons)
Sources=entity.Sources()
Jobs=entity.Jobs()

# User toggles
cancel_jobs_toggle=False

# Use these alternative functions below for testing purposes
# The sources tab will only display the mock data when DEBUG=True
# Adding things will add to the actual data, but it is not shown

# returns [(source_key1, source1), (source_key2, source2), ...]
def get_sources_list():
    if constants.DEBUG:
        return fake.Sources.read()
    else:
        return Sources.read()

def get_job_list():
    if constants.DEBUG:
        return fake.Sources.Jobs()
    else:
        return Jobs.get_jobs()