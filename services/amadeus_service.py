import requests

AMADEUS_AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_LOCATION_URL = "https://test.api.amadeus.com/v1/reference-data/locations"
AMADEUS_HOTEL_URL = "https://test.api.amadeus.com/v2/shopping/hotel-offers"

def get_amadeus_token(key, secret):
    r = requests.post(
        AMADEUS_AUTH_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": key,
            "client_secret": secret
        },
        timeout=10
    )
    r.raise_for_status()
    return r.json()["access_token"]

def get_city_code(city, token):
    r = requests.get(
        AMADEUS_LOCATION_URL,
        headers={"Authorization": f"Bearer {token}"},
        params={"keyword": city, "subType": "CITY", "page[limit]": 1},
        timeout=10
    )
    r.raise_for_status()
    data = r.json()["data"]
    return data[0]["iataCode"] if data else None

def search_hotels(city_code, checkin, checkout, token):
    r = requests.get(
        AMADEUS_HOTEL_URL,
        headers={"Authorization": f"Bearer {token}"},
        params={
            "cityCode": city_code,
            "checkInDate": checkin,
            "checkOutDate": checkout,
            "adults": 1,
            "bestRateOnly": "true"
        },
        timeout=10
    )
    r.raise_for_status()
    return r.json()["data"]
