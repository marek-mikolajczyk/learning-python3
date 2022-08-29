# based on awesome tutorial
# https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0


# this script connects to Gitlab users API using
# environmental variables as url and credentials

import os
import requests
import json
import pandas as pd

gitlab_pat = os.getenv('GITLAB_PAT')
gitlab_url = os.getenv('GITLAB_URL')
gitlab_address = gitlab_url + "/api/v4/users?private_token=" + gitlab_pat


""" debug """
print(gitlab_address)
print(f"my gitlab token is {gitlab_pat}")
print(f"my gitlab url is {gitlab_address}")

r = requests.get(gitlab_address, verify=False)
with open('aaa.txt', 'w') as f:
    f.write(r.text)

with open('aaa_pretty.txt', 'w') as f:
    f.write(json.dumps(r.json(), indent=4))

users_list = []
for user_info in r.json():
    users_list.append([user_info['id'], user_info['name']])


print('now showing users_list as json')
print(users_list)


print('now showing users_list as pretty json')
print(json.dumps(r.json(), indent=4))


users_df = pd.DataFrame(data=users_list, columns=['id', 'name'])
users_df.sort_values(by=['id'], inplace=True, ascending=True)
users_df.to_csv('aaa.csv', index=False)

print('now showing users_list in table format')
print(users_df.to_string(index=False))
