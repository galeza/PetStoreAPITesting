'''
Created on Nov 26, 2018

@author: agagaleza
'''

from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager
from hamcrest import assert_that, equal_to, contains_string
from common.config.request_constants import RequestConstants
import logging
from features.domain_models.tag import Tag
from features.domain_models.user import User
from hamcrest.library.collection.isdict_containingkey import has_key

logger = logging.getLogger(__name__)
user_details = {}

@step(u'"{http_request_type}" api user request endpoint is set as "{endpoint}"')
def step_impl(context, http_request_type, endpoint):
    context.requestConfigManager = RequestConfigManager()
    if (RequestConstants.JSON_USER_GET_LOGIN == http_request_type or RequestConstants.JSON_POST == http_request_type):
        context.requestConfigManager.set_endpoint(endpoint)

@when(u'User details are set as "{user_property}" and "{value}"') 
def step_impl(context, user_property, value):
    for row in context.table:
        user_details[row['user_property']] = row['value']
    context.user.set_user_details(user_details)
    
@when(u'User username and password are specified as "{username}" and "{password}"')
def step_impl(context, username, password):
    context.user.username = username
    context.user.password = password
    context.requestConfigManager.set_http_request_url_query_param(context.user)
    
@when(u'Request BODY form parameters are set using user details')
def step_impl(context):
    context.requestConfigManager.set_http_request_body_with_user_details(context.user)   