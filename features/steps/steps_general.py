
'''
Created on Sep 10, 2018

@author: agagaleza
'''
import requests
from common.config.request_config_manager import RequestConfigManager
from behave import given, when, then, step
from features.domain_models.pet import Pet


@given(u'Set web application url as "{basic_url}"')
def step_impl(context, basic_url):
    """
    BACKGROUND step is called at begin of each scenario before other steps.
    """
    # -- SETUP
    context.pet = Pet()
    context.requestConfigManager = RequestConfigManager()
    context.requestConfigManager.set_basic_url(basic_url)
    
@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    context.requestConfigManager.set_http_content_type(header_content_type)


@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    context.requestConfigManager.set_http_accept_type(header_accept_type)

@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = context.requestConfigManager.get_basic_url() 
    if 'GET' == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
        context.requestConfigManager.clear_http_request_body()
        context.requestConfigManager.set_get_response_full(url_temp)
    elif 'GET FINDBYSTATUS' == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint() + context.pet.get_pet_status()
        print(url_temp)
        context.requestConfigManager.clear_http_request_body()
        context.requestConfigManager.set_get_response_full(url_temp)
    elif 'POST' == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
#         context.requestConfigManager.clear_http_request_body()
        context.requestConfigManager.set_post_response_full(url_temp)
        
    elif 'PUT' == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
        context.requestConfigManager.set_put_response_full(url_temp)
        
    elif 'DELETE' == http_request_type:
        url_temp += context.requestConfigManager.get_endpoint()
        context.requestConfigManager.set_delete_response_full(url_temp)


@step(u'Valid HTTP response should be received')
def step_impl(context):
    if None in context.requestConfigManager.get_response_full():
        assert False, 'Null response received'
        
@step(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    context.requestConfigManager.set_expected_response_code(expected_response_code)
    actual_response_code = context.requestConfigManager.get_response_full_status_code()
    if str(actual_response_code) not in str(expected_response_code):
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    context.requestConfigManager.set_expected_response_content_type(expected_response_content_type)
    actual_response_content_type = context.requestConfigManager.get_response_full_content_type()
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@then(u'Response BODY should not be null or empty')
def step_impl(context):
    if None in context.requestConfigManager.get_response_full():
        assert False, '***ERROR:  Null or none response body received'
        
@when(u'Set HEADER params for request and response')
def step_impl(context):
    context.execute_steps(u''' when Set HEADER param request content type as "application/json"
    and Set HEADER param response accept type as "application/json" ''')
        
        
        
        
        