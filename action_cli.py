# import typer


# def main(api_token: str, vcs: str = "github"):
#     print(vcs)

# if __name__=="__main__":
#     typer.run(main)

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--token", dest="token", help="API token")
parser.add_argument("--repo-name", dest="repo", help="Repo name")
parser.add_argument("--run-id", dest="run_id", help="Artifact ID")

def download_artifact(token, run_id, repo):
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10  # Set the timeout value in seconds

    r = requests.get(f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/artifacts", headers=headers, timeout=timeout)
    print(r.json())
    artifact_id = r.json()["artifacts"][0]["id"]
    r = requests.get(f"https://api.github.com/repos/{repo}/actions/artifacts/{artifact_id}/zip", headers=headers, timeout=timeout)
    print(r.json())

if __name__ == "__main__":
    args = parser.parse_args()
    download_artifact(args.token, args.run_id, args.repo)
    