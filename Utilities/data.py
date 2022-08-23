# data provider (store variables, hardcode things and functions to get and set data)
import entity
import Utilities.constants as constants

from Tests import fake_provider as fake

# data (singletons)
Sources=entity.Sources()
Jobs=entity.Jobs()

# Use these alternative functions below for testing purposes
# The sources tab will only display the mock data when DEBUG=True
# Adding things will add to the actual data, but it is not shown
def get_source_list():
    if constants.DEBUG:
        return fake.Sources.read()
    else:
        return Sources.read()

def get_job_list():
    if constants.DEBUG:
        return fake.Sources.Jobs()
    else:
        return Jobs.get_jobs()