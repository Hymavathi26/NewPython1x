#1.Python testing framework-----Unit Test,nose,pytest
#2.Every testcase should start with test_functionName and file name also create with test_name.py
#3.pytest -h   (it will give all commands like help option,Run throuht terminal)
#4.pytest -k --> mathc the function namelike substrin--pytest -k "name"
#5.pytest -v logs  (--v is verbos)

#how to create booking by using the pytest-->allure reports
#steps:
#create booking
#pass URL
#add headers
#Body/Payload--Json format
#Token /Auth??  NO need for post booking
#verify the bookin id and bookin information(as Json)


import requests
import pytest
@pytest.mark.positive
def test_create_booking_positive():
    print("Create booking testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers={"Content-Type":"application/json"}
    json_payload = {                    #json take data in the single quout doesnot allow double quout
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response=requests.post(url=URL,headers=headers,json=json_payload )
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    #assertions
    assert response.status_code == 200
    #get the response body and verify the json, booking id is not none
    data=response.json()
    booking_id=data["bookingid"]    #FOR PUT REQ WE ARE USING THIS VARIABLE
    print(data)
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Jim", "Failed message - Incorrect Firstname"
    assert data["booking"]["lastname"] == "Brown", "Failed message  - incorrect lastname"

@pytest.mark.negative
def test_create_booking_negative():
    print("Create booking testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {}  # json take data in the single quout doesnot allow double quout
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # assertions
    assert response.status_code == 500   #internal servr Error
    # verification no need for negative TC becoz not passing body



