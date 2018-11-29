Feature: REST API Python and Behave testing framework
	Python requests module is used to raise requests concerning pet shop 
	User can add, modify, delete pet. HTTP responses are validated and JSON response is parsed.

#    BACKGROUND steps are called at begin of each scenario before other steps.
Background: 
	Given Swagger PetStore web application url is set as "https://petstore.swagger.io/v2/"

# Logs user into the system
Scenario: GET user login

  Given "GET LOGIN" api user request endpoint is set as "user/login"
  When HEADER param response accept type is set as "application/json" 
	And User username and password are specified as "test" and "abc123" 
	And Request BODY form parameters are set using pet details  
	And "GET LOGIN" HTTP request is raised
    Then Valid HTTP response is received 
	And Response http code is 200 
	And Response http text contains session number 
	And Response HEADER content type is "application/json" 
	And Response BODY is not null or empty 

# Create user
Scenario: Add new user using POST request
  Given "POST" api user request endpoint is set as "user"
  When  HEADER params for request and response are specified
	And User details are set as "<user_property>" and "<value>"
	
		| user_property                                  | value  |
		| username                                       | Elwanek|
		| first_name                                     | Elwanek |
		| last_name                                      | Danillo |
		| email                                          | danillo@gmail.com|
		| password                                       | danillo|
		| phone                                          | 123456789|
		| user_status                                    | 1|
	And Request BODY form parameters are set using user details  
	And "POST" HTTP request is raised
  Then  Valid HTTP response is received 
	And Response http code is 200 
	And Response HEADER content type is "application/json" 
	And Response BODY is not null or empty 

