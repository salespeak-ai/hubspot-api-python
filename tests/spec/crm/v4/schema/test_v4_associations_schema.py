from hubspot import HubSpot
from hubspot.crm.associations.v4.schema import DefinitionsApi


def test_is_discoverable():
    apis = HubSpot().crm.associations.v4.schema
    assert isinstance(apis.definitions_api, DefinitionsApi)
