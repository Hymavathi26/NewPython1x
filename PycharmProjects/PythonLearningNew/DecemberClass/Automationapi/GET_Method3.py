import requests


def main():
    id = 9475
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + str(id)
    print(full_url)

    response_body = requests.get(full_url)
    assert response_body.status_code == 200  # if Sc !=200 it wii ive error,else it will not give an error

    Data = response_body.json()
    # Assertions
    #verification of keys
    assert 'firstname' in Data, "Incorrect firstname"
    assert 'lastname' in Data, "Incorrect lastname"

    # verification of data
    assert Data['firstname'] == "Jim", "incorrect firstname"
    assert Data['lastname'] == "Brown", "INcorrect lastname"
    assert Data['bookingdates']['checkin'] == "2018-01-01", "Incorrect booking date message"


if __name__ == '__main__':
    main()
