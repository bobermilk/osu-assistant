# data provider (store variables, hardcode things and functions to get and set data)
import entity
import Utilities.constants as constants

from Tests import fake_provider as fake

# data
Sources=entity.Sources()

# Use these alternative functions below for testing purposes
# The sources tab will only display the mock data when DEBUG=True
# Adding things will add to the actual data, but it is not shown
def get_source_list():
    if constants.DEBUG:
        return (fake.sources)
    else:
        return Sources.read()