from dotenv import load_dotenv
import os
from common.ApiClient import ApiClient

def main():
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    api_client = ApiClient()
    get_url = base_url + "/v1/s1/e2/resources/stars"
    solution_post_url = base_url + "/v1/s1/e2/solution"

    # The resonance of a star is fixed from the previous one
    params = {
        "page": 1,
        "sort-by": "resonance",
        "sort-direction": "asc"
    }
    response = api_client.get(get_url, params)
    min_resonance = response[0]["resonance"];
    next_resonance = response[1]["resonance"];
    step = next_resonance - min_resonance
    print("Min resonance: " + str(min_resonance))
    print("Step: " + str(step))
    
    params = {
        "page": 1,
        "sort-by": "resonance",
        "sort-direction": "des"
    }
    response = api_client.get(get_url, params)
    max_resonance = response[0]["resonance"];
    print("Max resonance: " + str(max_resonance))

    sum = 0
    n = 0
    for i in range(min_resonance, max_resonance + 1, step):
        sum += i
        n += 1

    average_resonance = sum // n
    print("Average resonance: " + str(average_resonance))

    response = api_client.post(solution_post_url, {"average_resonance": average_resonance})
    print(response)

if __name__ == "__main__":
    main()
