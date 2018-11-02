Feature: REST API Python and Behave testing framework
	Python requests module is used to raise requests concerning pet shop 
	User can add, modify, delete pet. HTTP responses are validated and JSON response is parsed.
	
Background: 
	Given Swagger PetStore web application url is set as "https://petstore.swagger.io/v2/"


Scenario Outline: Add new pet using POST request
  Given "POST" api pet request endpoint is set as "pet"
  When  HEADER params for request and response are specified
	And Pet details are set as "<pet_property>" and "<value>"
	
		| pet_property                                   | value  |
		| name                                           | Elwanek|
		| photoUrls                                      | /Users/a/Documents/Sel/workspace/PetStoreAPITesting1 |
		| photoUrls                                      | /Users/a/Documents/Sel/workspace/PetStoreAPITesting2 |

	And Pet "<status>" is specified
	And Request BODY form parameters are set using pet details  
	And "POST" HTTP request is raised
  Then  Valid HTTP response is received 
	And Response http code is 200 
	And Response HEADER content type is "application/json" 
	And Response BODY is not null or empty 
	And Response BODY contains newly added pet details
    Examples: Pets
      | status |
      | pending|
      | available|
      |sold|

@smoke		
Scenario: GET pet request using pet ID

  Given "POST" api pet request endpoint is set as "pet"
  When HEADER params for request and response are specified
	And Pet details are specified as "Elwanek" and "/Users/a/Documents/Sel/workspace/PetStoreAPITesting1 " and "pending"
	And Request BODY form parameters are set using pet details  
	And "POST" HTTP request is raised
    And Valid HTTP response is received 
	And Response http code is 200 
    And "GET" api pet request endpoint is set as "pet"
    And HEADER params for request and response are specified
	And "GET" HTTP request is raised
  Then Valid HTTP response is received
#  	And Validate response
	And Response http code is 200 
	And Response HEADER content type is "application/json" 
	And Response BODY is not null or empty 
	And Response BODY contains newly added pet details

Scenario Outline: GET pet request using pet status

  Given "GET FINDBYSTATUS" api pet request endpoint is set as "pet/findByStatus" 
  When Pet status is set as "<status>"
    And HEADER params for request and response are specified
	And "GET FINDBYSTATUS" HTTP request is raised
  Then Valid HTTP response is received
#  	And Validate response
	And Response http code is 200 
	And Response HEADER content type is "application/json" 
	And Response BODY is not null or empty 
	And Response BODY pet status is equal to pet status
    Examples: Pets
      | status |
      | pending|
      | available|
      |sold|
      
	      		
Scenario: DELETE pet request using pet ID

  Given "POST" api pet request endpoint is set as "pet"
  When HEADER params for request and response are specified
	And Pet details are specified as "Elwanek" and "/Users/a/Documents/Sel/workspace/PetStoreAPITesting1 " and "sold"
	And Request BODY form parameters are set using pet details  
	And "POST" HTTP request is raised
    And Valid HTTP response is received 
	And Response http code is 200 
    And "DELETE" api pet request endpoint is set as "pet"
    And HEADER params for request and response are specified
	And "DELETE" HTTP request is raised
  Then Valid HTTP response is received
#  	And Validate response
	And Response http code is 200 
	And Response HEADER content type is "application/json" 
	And Response BODY is not null or empty 
	
Scenario: UPDATE pet request using pet ID

  Given "POST" api pet request endpoint is set as "pet"
  When HEADER params for request and response are specified
	And Pet details are specified as "Elwanek" and "/Users/a/Documents/Sel/workspace/PetStoreAPITesting1 " and "pending"
	And Request BODY form parameters are set using pet details 
	And "POST" HTTP request is raised
    And Valid HTTP response is received 
	And Response http code is 200 
    And "PUT" api pet request endpoint is set as "pet"	
    And Pet details are specified as "Elwanek2" and "/Users/a/Documents/Sel/workspace/PetStoreAPITesting2 " and "sold"
    And Request BODY form parameters are set using pet details
	And "PUT" HTTP request is raised
  Then Valid HTTP response is received
#  	And Validate response
	And Response http code is 200 
	And Response HEADER content type is "application/json" 
	And Response BODY is not null or empty 	
		
Scenario: UPLOAD pet photo/image POST request using pet ID

  Given "POST" api pet request endpoint is set as "pet"
  When HEADER params for request and response are specified
	And Pet details are specified as "Maja" and "pending"
	And Request BODY form parameters are set using pet details 
	And "POST" HTTP request is raised
    And Valid HTTP response is received 
	And Response http code is 200 
    And "POST UPLOADIMAGE" api pet request endpoint is set as "pet"	
    And Photo is selected as "smallDog.jpeg"
    And Request BODY form parameters are set using pet photo details 
	And "POST UPLOADIMAGE" HTTP request is raised
  Then Valid HTTP response is received
#  	And Validate response
	And Response http code is 200 
	And Response HEADER content type is "application/json" 
	And Response BODY is not null or empty 		
	And Response BODY contains uploaded file name
