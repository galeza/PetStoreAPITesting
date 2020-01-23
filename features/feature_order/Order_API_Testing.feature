Feature: REST API Python and Behave testing framework
	Python requests module is used to raise requests concerning pet shop 
	User can add, modify, delete pet. HTTP responses are validated and JSON response is parsed.

#    BACKGROUND steps are called at begin of each scenario before other steps.
Background: 
	Given Swagger PetStore web application url is set as "https://petstore.swagger.io/v2/"

# Gets inventory
Scenario: GET store inventory

  Given "GET" api order request endpoint is set as "store/inventory"
  When HEADER param response accept type is set as "application/json" 
  And "GET" HTTP request is raised
  Then Valid HTTP response is received 
  And Response http code is 200 
  And Response http text contains session number 
  And Response HEADER content type is "application/json" 
  And Response BODY is not null or empty 