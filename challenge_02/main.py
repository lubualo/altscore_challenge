from dotenv import load_dotenv
import os
from common.ApiClient import ApiClient

def main():
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")
    api_client = ApiClient()
    get_url = base_url + "/v1/s1/e2/resources/stars"
    solution_post_url = base_url + "/v1/s1/e2/solution"

    # The resonance of a star is fixed from the previous one. As they are evenly spaced the midpoint is the average
    params = {
        "page": 1,
        "sort-by": "resonance",
        "sort-direction": "asc"
    }
    response = api_client.get(get_url, params, {"API-KEY": api_key })
    min_resonance = response[0]["resonance"];
    print("Min resonance: " + str(min_resonance))
    
    params = {
        "page": 1,
        "sort-by": "resonance",
        "sort-direction": "des"
    }
    response = api_client.get(get_url, params, {"API-KEY": api_key })
    max_resonance = response[0]["resonance"];
    print("Max resonance: " + str(max_resonance))

    average_resonance = round((min_resonance + max_resonance) / 2)

    print("Average resonance: " + str(average_resonance))

    response = api_client.post(solution_post_url, {"average_resonance": average_resonance}, {"API-KEY": api_key })
    print(response)

if __name__ == "__main__":
    main()
