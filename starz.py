# TODO: Code cleanup!
### In Prod
import requests
repos = requests.get("https://api.github.com/users/tamton-aquib/repos").json()

### In Test
# import json
# with open('./nice.json') as f:
    # repos = json.load(f)

#######################################################################

# filter_list = ["stuff.nvim", "keys.nvim", "essentials.nvim", "mpv.nvim", "nvim"]
top_repos = filter(
    lambda x: x["stargazers_count"] > 15, #  and x["name"] not in filter_list,
    sorted(repos, key=lambda x: x["stargazers_count"], reverse=True)
)

res = """
<h3 align="center">My Popular Projects</h3>

| :star2: | :fork_and_knife: | Name | Description |
|---|---|---|---|
"""
for repo in top_repos:
    res += f"| {repo['stargazers_count']} "
    res += f"| {repo['forks_count']} "
    res += f"| [{repo['name']}]({repo['html_url']}) "
    res += f"| {repo['description']} |\n"

res += """
<sup>This table was automatically generated as a fun experiment from [this](https://github.com/tamton-aquib/tamton-aquib/blob/main/starz.py) github workflow action.</sup>

---
"""

try:
    with open('README.md', 'r') as file:
        data = file.read()
        begin_index = data.find("<!-- BEGIN -->")
        end_index = data.find("<!-- END -->")
        if begin_index != -1 and end_index != -1:
            new_data = data[:begin_index + len("<!-- BEGIN -->")] + "\n" + res + "\n" + data[end_index:]
            with open('README.md', 'w') as file:
                file.write(new_data)
                print("README.md updated successfully!")
        else:
            print("Could not find <!-- BEGIN --> and/or <!-- END --> in README.md")
except FileNotFoundError:
    print("README.md not found")
