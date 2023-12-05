#without using main function
import requests
response_body=requests.get("https://restful-booker.herokuapp.com/booking/926")
print(response_body.text)
print(response_body.headers)

#verify
#assertions:difference between acutal result(AR) and expected result(ER)
#status_code ER = 200
#AR = 200

#if id = 927
#ER = 404--fprbidden
#AR = 404--forbidden

