import argparse
import requests
import os

parser = argparse.ArgumentParser()
parser.add_argument("--token", dest="token", help="API token")
parser.add_argument("--repo-name", dest="repo", help="Repo name")
# parser.add_argument("--run-id", dest="run_id", help="Artifact ID")
parser.add_argument("--designite-output", dest="designite_output", help="Designite Output")

def download_artifact(token, run_id, repo):
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10  # Set the timeout value in seconds
    url = f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/artifacts"
    print(url)
    r = requests.get(url, headers=headers, timeout=timeout)
    print(r.json())
    artifact_id = r.json()["artifacts"][0]["id"]
    r = requests.get(f"https://api.github.com/repos/{repo}/actions/artifacts/{artifact_id}/zip", headers=headers, timeout=timeout)
    print(r.json())

def validate(token, designite_output, repo):
    print(os.listdir(designite_output))



if __name__ == "__main__":
    args = parser.parse_args()
    # download_artifact(args.token, args.run_id, args.repo)
    validate(args.token, args.designite_output, args.repo)

    