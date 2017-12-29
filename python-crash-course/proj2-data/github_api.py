import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status:", r.status_code)
response_dict = r.json()

print(response_dict.keys())
print("Total repos:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repos returned:", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)