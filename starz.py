import requests

repos = requests.get("https://api.github.com/users/tamton-aquib/repos?per_page=100").json()

nvim_repos = sorted(
    (r for r in repos if r["name"].endswith(".nvim")),
    key=lambda x: x["stargazers_count"],
    reverse=True,
)

res = """
<h3 align="center">Neovim plugins</h3>

<div align="center">

| :star2: | :fork_and_knife: | Name | Description |
|---|---|---|---|
"""
for repo in nvim_repos:
    res += f"| {repo['stargazers_count']} "
    res += f"| {repo['forks_count']} "
    res += f"| [{repo['name']}]({repo['html_url']}) "
    res += f"| {repo['description']} |\n"

res += """
</div>

<sup>This table was automatically generated as a fun experiment from [this](https://github.com/tamton-aquib/tamton-aquib/blob/main/starz.py) github workflow action.</sup>

---
"""

try:
    with open("README.md", "r") as file:
        data = file.read()
        begin_index = data.find("<!-- BEGIN -->")
        end_index = data.find("<!-- END -->")
        if begin_index != -1 and end_index != -1:
            new_data = data[: begin_index + len("<!-- BEGIN -->")] + "\n" + res + "\n" + data[end_index:]
            with open("README.md", "w") as file:
                file.write(new_data)
                print("README.md updated successfully!")
        else:
            print("Could not find <!-- BEGIN --> and/or <!-- END --> in README.md")
except FileNotFoundError:
    print("README.md not found")
