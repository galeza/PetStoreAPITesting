Feature: REST API Python and Bahave testing framework
	Raise request(s) concerning pet shop using Python requests moduls
	User can perform CRUD operations: add, modify, get, delete pet. + Validate HTTP response code and parse JSON response 
	
Background: 
	Given Set web application url as "https://petstore.swagger.io/v2/"

Scenario Outline: User can add new pet using POST request
  Given Set POST pet api endpoint as "pet"
  When Set HEADER param request content type as "application/json"
  	And Set HEADER param response accept type as "application/json" 
	And Set pet details as "<particular>" and "<value>" below
	
		| particular                                     | value  |
		| name                                           | Elwanek|
		| photoUrls                                      | /Users/a/Documents/Sel/workspace/PetStoreAPITesting1 |
		| photoUrls                                      | /Users/a/Documents/Sel/workspace/PetStoreAPITesting2 |

	And Add pet "<status>"
	And Set BODY form param using pet details  
	And Raise "POST" HTTP request
  Then Valid HTTP response should be received 
	And Response http code should be 200 
	And Response HEADER content type should be "application/json" 
	And Response BODY should not be null or empty 
	And Response BODY contains newly added pet details
    Examples: Pets
      | status |
      | pending|
      | available|
      |sold|
		
Scenario: GET pet request using pet ID

  Given Set POST pet api endpoint as "pet"
  When Set HEADER params for request and response
	And Set pet details as "Elwanek" and "/Users/a/Documents/Sel/workspace/PetStoreAPITesting1 " and "pending"
	And Set BODY form param using pet details  
	And Raise "POST" HTTP request
    And Valid HTTP response should be received 
	And Response http code should be 200 
    And Set GET pet request endpoint was set as "pet/"
    And Set HEADER params for request and response
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
#  	And Validate response
	And Response http code should be 200 
	And Response HEADER content type should be "application/json" 
	And Response BODY should not be null or empty 
	And Response BODY contains newly added pet details