import requests
from app.config import GITHUB_TOKEN, BASE_URL

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_repos(username: str):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch repositories")

    return response.json()


def create_issue(data):
    url = f"{BASE_URL}/repos/{data.repo_owner}/{data.repo_name}/issues"
    print(url)

    payload = {
        "title": data.title,
        "body": data.body
    }


    response = requests.post(url, json=payload, headers=headers)
    print(response)
    if response.status_code != 201:
        raise Exception(response.json())

    return response.json()

def list_issues(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(response.text)

    return [
        {
            "id": issue["id"],
            "number": issue["number"],
            "title": issue["title"],
            "state": issue["state"],
            "created_at": issue["created_at"]
        }
        for issue in response.json()
    ]