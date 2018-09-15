
'''
Created on Sep 10, 2018

@author: agagaleza
'''
from behave import given, when, then, step
from common.config.request_config_manager import RequestConfigManager


@given(u'Set GET pet app endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    context.requestConfigManager = RequestConfigManager()
    context.requestConfigManager.set_GET_endpoint(get_api_endpoint)
