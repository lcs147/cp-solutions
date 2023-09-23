import json
import requests


def get_all_submissions(username):
    return json.loads(
        requests.get(f"https://codeforces.com/api/user.status?handle=lcs147").text
        # requests.get(f"https://codeforces.com/api/user.status?handle=lcs147&from=1&count=1").text
    )["result"]


def main():
    username = input("Enter codeforces username: ")
    subs = get_all_submissions(username)
    accs = []
    for sub in subs:
        if sub["verdict"] == "OK":
            accs.append(
                {
                    "id": sub["id"],
                    "link": f'https://codeforces.com/contest/{sub["problem"]["contestId"]}/submission/"{sub["id"]}',
                }
            )
    print(len(accs), accs[0])
    # save all submissions


if __name__ == "__main__":
    main()
