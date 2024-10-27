import json
import requests

dUrl = 'https://httpbin.org/patch'

dheader = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'user-name':'["arc","vigo"]'
}

dResp = requests.patch(url=dUrl,headers=dheader)

user_name = json.loads(dheader['user-name'])

print("converted list:",user_name)


