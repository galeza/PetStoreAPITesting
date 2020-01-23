'''
Created on Jan 23, 2020

@author: agagaleza
'''
from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager
from common.config.request_constants import RequestConstants

# specific id
@step(u'"{http_request_type}" api order request endpoint is set as "{endpoint}"')
def step_impl(context, http_request_type, endpoint):
    context.requestConfigManager = RequestConfigManager()
    if (RequestConstants.JSON_GET == http_request_type):
        context.requestConfigManager.set_endpoint(endpoint)
   
