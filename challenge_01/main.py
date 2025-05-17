from dotenv import load_dotenv
import os
from common.ApiClient import ApiClient
import re

def main():
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    api_client = ApiClient()
    get_url = base_url + "/v1/s1/e1/resources/measurement"
    solution_post_url = base_url + "/v1/s1/e1/solution"
    response = api_client.get(get_url)
    while (response["distance"] == 'failed to measure, try again' and response["time"] == 'failed to measure, try again'):
        response = api_client.get(get_url)

    print(response)
    # Possible improvement: use a dataclass instead of a dictionary for the api response
    distance = convertStringMeasuermentToFloat(response["distance"])
    time = convertStringMeasuermentToFloat(response["time"])
    speed = round(distance / time)
    print("Speed: " + str(speed))
    response = api_client.post(solution_post_url, {"speed": str(speed)})
    print(response)

def convertStringMeasuermentToFloat(timeString):
    match = re.search(r"([\d.]+)", timeString)
    return float(match.group(1))


if __name__ == "__main__":
    main()
