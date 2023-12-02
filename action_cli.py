import argparse
import requests
import os
import zipfile

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

    print("Validating")
    print(f"Current Directory = {os.getcwd()}")
    print(os.listdir())
    print(os.listdir("/"))
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10  # Set the timeout value in seconds
    url = f"https://api.github.com/repos/{repo}/actions/artifacts"
    print(url)
    r = requests.get(url, headers=headers, timeout=timeout)
    print(r.json())
    for artifacts in r.json()["artifacts"]:
        if artifacts["name"] == designite_output:
            artifact_id = artifacts["id"]
            print(artifact_id)
            r = requests.get(artifacts["archive_download_url"], headers=headers, timeout=timeout)
            print(r.headers)
            if r.status_code == 200:
                # Save the downloaded artifact to a local file
                with open(f'{designite_output}.zip', 'wb') as f:
                    f.write(r.content)

                os.makedirs(designite_output, exist_ok=True)
                # Extract the downloaded artifact
                with zipfile.ZipFile(f'{designite_output}.zip', 'r') as zip_ref:
                    zip_ref.extractall(designite_output)
                
                print(f"Artifact '{designite_output}' downloaded successfully.")
            else:
                print(f"Failed to download artifact '{designite_output}'.")            
            print("Extracting")
            print(os.listdir())
            break
    
    # print(os.listdir(designite_output))



if __name__ == "__main__":
    args = parser.parse_args()
    # download_artifact(args.token, args.run_id, args.repo)
    validate(args.token, args.designite_output, args.repo)

    