# import requests

# def fetch_data_from_api(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print("Failed to fetch data from API. Status code:", response.status_code)
#             return None
#     except requests.exceptions.RequestException as e:
#         print("Error fetching data:", e)
#         return None

# # api_url = "https://api.gstefiling.co.in/"
# api_url = "https://gstapi.charteredinfo.com/commonapi/v1.0/returns?aspid=1754502724&password=R@ghav2020&Action=RETTRACK&Gstin=27AAKPM3407D1ZY&fy=2022-23"
# # 
# api_data = fetch_data_from_api(api_url)

# if api_data:
#     print("Data retrieved successfully from API!")
#     print("API Data:", api_data)
# else:
#     print("Failed to retrieve data from API. Exiting...")

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# import requests
# import pandas as pd

# def fetch_data_from_api(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print("Failed to fetch data from API. Status code:", response.status_code)
#             return None
#     except requests.exceptions.RequestException as e:
#         print("Error fetching data:", e)
#         return None

# # api_url = "https://api.gstefiling.co.in/"
# api_url = "https://sandbox.surepass.io/api/v1"
# # api_url = "https://gstapi.charteredinfo.com/commonapi/v1.1/search?aspid=1754502724&password=R@ghav2020&Action=TP&Gstin=27AAKPM3407D1ZY&SearchGstin=27AEOFS4249H1ZJ"

# api_data = fetch_data_from_api(api_url)

# if api_data:
#     print("Data retrieved successfully from API!")
    
#     # Convert JSON data to a pandas DataFrame
#     df = pd.json_normalize(api_data)
#     print(df)
#     # Optionally, you can store the DataFrame to a CSV file
#     # df.to_csv('api_data1.csv', index=False)
    
# else:
#     print("Failed to retrieve data from API. Exiting...")

# ------------------------------------------------------------------------------------------------------------------------------------------


# import pandas as pd
# import json

# # JSON-like string
# data_str = '[{"valid": "Y", "mof": "ONLINE", "dof": "17-03-2023", "ret_prd": "022023", "rtntype": "GSTR3B", "arn": "AB2702232926533", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "17-03-2023", "ret_prd": "022023", "rtntype": "GSTR1", "arn": "AB2702232921484", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "22-02-2023", "ret_prd": "012023", "rtntype": "GSTR3B", "arn": "AB270123913650J", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "22-02-2023", "ret_prd": "012023", "rtntype": "GSTR1", "arn": "AB270123913541K", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "24-01-2023", "ret_prd": "122022", "rtntype": "GSTR3B", "arn": "AC271222829477X", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "20-01-2023", "ret_prd": "122022", "rtntype": "GSTR1", "arn": "AC2712224826251", "status": "Filed"}, {"mof": "ONLINE", "dof": "31-12-2022", "ret_prd": "032022", "rtntype": "GSTR9C", "arn": "AD2703225422584", "status": "Filed"}, {"mof": "ONLINE", "dof": "30-12-2022", "ret_prd": "032022", "rtntype": "GSTR9", "arn": "AD270322522077C", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "20-12-2022", "ret_prd": "112022", "rtntype": "GSTR1", "arn": "AB2711225218691", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "20-12-2022", "ret_prd": "112022", "rtntype": "GSTR3B", "arn": "AB271122580162I", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "23-11-2022", "ret_prd": "102022", "rtntype": "GSTR3B", "arn": "AB271022727470K", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "21-11-2022", "ret_prd": "102022", "rtntype": "GSTR1", "arn": "AB271022671994X", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "19-10-2022", "ret_prd": "092022", "rtntype": "GSTR1", "arn": "AB270922888860I", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "19-10-2022", "ret_prd": "092022", "rtntype": "GSTR3B", "arn": "AB270922947572R", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "20-09-2022", "ret_prd": "082022", "rtntype": "GSTR3B", "arn": "AB270822364839I", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "10-09-2022", "ret_prd": "082022", "rtntype": "GSTR1", "arn": "AA270822551946Q", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "19-08-2022", "ret_prd": "072022", "rtntype": "GSTR3B", "arn": "AB270722316550E", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "18-08-2022", "ret_prd": "072022", "rtntype": "GSTR1", "arn": "AB270722209877S", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "20-07-2022", "ret_prd": "062022", "rtntype": "GSTR3B", "arn": "AB270622976626N", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "20-07-2022", "ret_prd": "062022", "rtntype": "GSTR1", "arn": "AB270622970678K", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "18-06-2022", "ret_prd": "052022", "rtntype": "GSTR3B", "arn": "AB270522203517E", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "03-06-2022", "ret_prd": "052022", "rtntype": "GSTR1", "arn": "AA2705221820958", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "30-05-2022", "ret_prd": "042022", "rtntype": "GSTR3B", "arn": "AB2704226902438", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "18-05-2022", "ret_prd": "042022", "rtntype": "GSTR1", "arn": "AB2704221439072", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "19-04-2022", "ret_prd": "032022", "rtntype": "GSTR1", "arn": "AB270322660064G", "status": "Filed"}, {"valid": "Y", "mof": "ONLINE", "dof": "19-04-2022", "ret_prd": "032022", "rtntype": "GSTR3B", "arn": "AB2703226607626", "status": "Filed"}]'

# # Parse JSON string
# data = json.loads(data_str)

# # Create DataFrame
# df = pd.DataFrame(data)

# # Display DataFrame
# print(df)

# ---------------------------------------------------------------------------------------------------------------------------------
import requests

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (status code >= 400)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None
    except ValueError as e:
        print("Error parsing JSON response:", e)
        return None

api_url = "https://app.surepass.io/api/v1/user/verify-email?verification_uri=.eJwNy8EKAiEQANB_8dxBXGWcblEQdIiCqKM441iym0ZJFNG_17u_j-KpSO2hJDVXrd-CYVju3vroD3C9rPebEz8W29Wkzy9QM_WUe8mFYy-tht5Gqf-WPCJaDWQgMrlskviIDo0VGyFHBjQaLMWBnAfyAzgmAaEMmVFQfX-leCpU.ZcWrGQ.FNB093TR8VCuFrKMYFuJtIbMVYM"
api_data = fetch_data_from_api(api_url)

if api_data:
    print("Data retrieved successfully from API!")
    print("API Data:", api_data)
else:
    print("Failed to retrieve data from API. Exiting...")


