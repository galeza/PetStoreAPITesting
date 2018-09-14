
'''
Created on Sep 10, 2018

@author: agagaleza
'''
import requests

from behave import given, when, then, step

basic_config = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}

@given(u'Set web application url as "{basic_url}"')
def step_impl(context, basic_url):
    basic_config['basic_url'] = basic_url
    
@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type


@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type

@given(u'Set GET pet app endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    basic_config['GET_api_endpoint'] = get_api_endpoint

@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = basic_config['basic_url']
    if 'GET' == http_request_type:
        url_temp += basic_config['GET_api_endpoint']
        http_request_body.clear()
        basic_config['response_full'] = requests.get(url_temp,
                                                                                         headers=http_request_header,
                                                                                         params=http_request_url_query_param,
                                                                                         data=http_request_body)
#     elif 'POST' == http_request_type:
#         url_temp += global_general_variables['POST_api_endpoint']
#         http_request_url_query_param.clear()
#         global_general_variables['response_full'] = requests.post(url_temp,
#                                                                                          headers=http_request_header,
#                                                                                          params=http_request_url_query_param,
#                                                                                          data=http_request_body)
#     elif 'PUT' == http_request_type:
#         url_temp += global_general_variables['PUT_api_endpoint']
#         http_request_url_query_param.clear()
#         global_general_variables['response_full'] = requests.put(url_temp,
#                                                                                          headers=http_request_header,
#                                                                                          params=http_request_url_query_param,
#                                                                                          data=http_request_body)
#     elif 'DELETE' == http_request_type:
#         url_temp += global_general_variables['DELETE_api_endpoint']
#         http_request_body.clear()
#         global_general_variables['response_full'] = requests.delete(url_temp,
#                                                                                             headers=http_request_header,
#                                                                                             params=http_request_url_query_param,
#                                                                                             data=http_request_body)


@then(u'Valid HTTP response should be received')
def step_impl(context):
    if None in basic_config['response_full']:
        assert False, 'Null response received'
        
@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    basic_config['expected_response_code'] = expected_response_code
    actual_response_code = basic_config['response_full'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print (str(basic_config['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    basic_config['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = basic_config['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@then(u'Response BODY should not be null or empty')
def step_impl(context):
    if None in basic_config['response_full']:
        assert False, '***ERROR:  Null or none response body received'
        
        
        
        
        
        
        
        