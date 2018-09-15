Feature: REST API Python and Bahave testing framework
	Raise request(s) concerning pet shop using Python requests moduls
	User can perform CRUD operations: add, modify, get, delete pet. + Validate HTTP response code and parse JSON response 
	
Background: 
	Given Set web application url as "https://petstore.swagger.io/v2/"

#Scenario: User can add new pet using POST request
#  Given Set POST pet api endpoint as "pet"
#  When Set HEADER param request content type as "application/json"
#	And Set HEADER param response accept type as "application/json" 
#	And Set BODY form param using pet details 
#	And Raise "POST" HTTP request
#  Then Valid HTTP response should be received 
#	And Response http code should be 200 
#	And Response HEADER content type should be "application/json" 
#	And Response BODY should not be null or empty 
#	And Response BODY contains newly added pet details
		
Scenario: GET pet request using pet ID
  Given Set GET pet request endpoint
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json" 
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200 
	And Response HEADER content type should be "application/json" 
	And Response BODY should not be null or empty 
	#And Validate json response "Maxik" and "sold"	as "pet/2