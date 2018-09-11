Feature: REST API Python and Bahave testing framework
	Raise request(s) concerning pet shop using Python requests moduls
	Validate HTTP response code and parse JSON response 
	
Background: 
	Given Set web application url as "https://petstore.swagger.io/v2/"
	
Scenario: GET pet request using pet ID
  Given Set GET pet app endpoint as "pet/1"
  When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "application/json" 
	# And Set ID param as "1" 
	And Raise "GET" HTTP request
  Then Valid HTTP response should be received
	And Response http code should be 200 
	And Response HEADER content type should be "application/json" 
	And Response BODY should not be null or empty 
	And Validate json response "Maxik" and "sold"	