import requests
import pytest


def create_token():  # this is not testcase normal function
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data = response.json()  # convert into json format
    token = data["token"]
    print(token)
    return token

def create_booking():      #this is not tc its just function and we use this for put request
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
    return booking_id


# make put req
def test_put_request():  #By using create_token() & create_bookin() sunctions we can resuse put request
    # booking ID and token we use
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()   #it gives id each time
    PUT_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()  # taking from create_token request
    headers = {"Content-Type": "application/json",
               "Cookie": cookie_value
               }
    print(headers)
    json_payload = {
        'firstname': "Jim",
        'lastname': "Brown",
        'totalprice': 111,
        'depositpaid': True,
        'bookingdates': {
            'checkin': "2018-01-01",
            'checkout': "2019-01-01"
        },
        'additionalneeds': "Breakfast"
    }
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    #print(response.text)
    #assertions
    assert response.status_code == 200
    # get the response body and verify
    data = response.json()
    print(data)
    assert data["firstname"] == "Jim", "Failed message - Incorrect Firstname"
    assert data["lastname"] == "Brown", "Failed message  - incorrect lastname"

def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    PUT_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()  # taking from create_token request
    headers = {"Content-Type": "application/json",
               "Cookie": cookie_value
               }
    print(headers)
    response = requests.delete(url=PUT_URL, headers=headers)
    # print(response.text)
    # assertions
    assert response.status_code == 201

