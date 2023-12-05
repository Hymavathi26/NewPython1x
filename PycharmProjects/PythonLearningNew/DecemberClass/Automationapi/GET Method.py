#API
#requests library
#why request module?
# to perform GET, POST, PUT,DELETE,PATCH Operations and verify
#different http method
#with using Main method
import requests

# def main():
#     print("hello")
#
# main()

#(OR)
def main():
  #get url
  response_body = requests.get("https://restful-booker.herokuapp.com/booking/926")
  print(response_body)
  print(response_body.text)
  print(response_body.status_code)
  print(response_body.json())

  if response_body.status_code==200:
      print("TC#1 - GET request is successfully")
  else:
      print("TC#2 - GET request is not successfully")  #if pass incorrect id it returns error


if __name__ == "__main__":
    main()


# To make an API Testing Req.
# url, auth, headers, cookies, data (payload), json, file

# Validate in API Testing
# response, headers, statuscode,responseTime, JSON Schema Validation





