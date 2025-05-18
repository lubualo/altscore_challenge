from dotenv import load_dotenv
import os
from common.ApiClient import ApiClient
import base64

def main():
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")
    api_client = ApiClient()
    solution_post_url = base_url + "/v1/s1/e3/solution"
    oracle_rolodex_url = base_url + "/v1/s1/e3/resources/oracle-rolodex"
    
    swapi_url = os.getenv("SWAPI_BASE_URL")
    people_url = swapi_url + "/people"
    planets_url = swapi_url + "/planet"
    planets = {};

    while (people_url):
        response = api_client.get(people_url, verify=False)
        people_url = response["next"]
        for person in response["results"]:
            planet = person["homeworld"]
            if (planet not in planets):
                planets[planet] = {"total": 0, "darkSide": 0, "lightSide": 0}

            oracleResponse = api_client.get(oracle_rolodex_url, {"name": person["name"]}, {"API-KEY": api_key })            
            planets[planet]["total"] += 1
            if isDarkSide(decodeOracleResponse(oracleResponse)):
                planets[planet]["darkSide"] += 1
            else:
                planets[planet]["lightSide"] += 1

    planet = api_client.get(findFirstBalancedPlanetUrl(planets), verify=False)
    print("The balanced planet is " + planet["name"])
    
    response = api_client.post(solution_post_url, {"planet": planet["name"]}, {"API-KEY": api_key })
    print(response)

def decodeOracleResponse(oracleResponse):
    return base64.b64decode(oracleResponse["oracle_notes"]).decode('utf-8')

def isDarkSide(decodedOracleResponse):
    return "belongs to the Dark Side" in decodedOracleResponse

def findFirstBalancedPlanetUrl(planets):
    for key in planets:
        if ((planets[key]["lightSide"] - planets[key]["darkSide"]) / planets[key]["total"] == 0):
            return key
    return ""

if __name__ == "__main__":
    main()
