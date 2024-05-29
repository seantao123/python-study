import requests
import pandas as pd


def get_json_from_web_service(url):
    response = requests.get(url)
    response.raise_for_status()
    json_data = response.json()
    return json_data


def extractPerson(json_response):
    result = json_response["results"]
    item1 = result[0]
    gender = item1['gender']
    name = item1['name']
    first = item1['name']['first']
    last = item1['name']['last']
    fullName = f"{first} {last}"
    number = item1['location']['street']['number']
    name = item1['location']['street']['name']
    city = item1['location']['city']
    country = item1['location']['country']
    postal = item1['location']['postcode']
    adress = f"{number}, {name}, {city}, {country}, {postal}"
    date = item1['dob']['date']
    phone = item1['phone']
    large = item1['picture']['large']

    dict = {
        'gender': gender,
        'fullName': fullName,
        'adress': adress,
        'date': date,
        'phone': phone,
        'large': large
    }
    return dict


url = 'https://randomuser.me/api/'
dictArray = []
for x in range(100):
    retrive = get_json_from_web_service(url)
    dict = extractPerson(retrive)
    dictArray.append(dict)


df = pd.DataFrame(dictArray)
df.to_csv("name.csv")


print()
