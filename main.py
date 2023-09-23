from html.parser import HTMLParser
import json
import bs4
import requests
from bs4 import BeautifulSoup
import mechanicalsoup
from urllib.request import urlopen


def get_all_submissions(username):
    return json.loads(
        # requests.get(f"https://codeforces.com/api/user.status?handle=lcs147").text
        requests.get(f"https://codeforces.com/api/user.status?handle=lcs147&from=1&count=1").text
    )["result"]


def getCode(url):
    response = requests.Session().get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")
    code = soup.find(id="program-source-text").text
    return code


def main():
    username = "lcs147"
    subs = get_all_submissions(username)
    accs = []
    for sub in subs:
        if sub["verdict"] == "OK":
            print(sub)
            accs.append(
                {
                    "sub_id": sub["id"],
                    "link": f'https://codeforces.com/contest/{sub["problem"]["contestId"]}/submission/{sub["id"]}',
                    "problem_id": f"{sub['problem']['contestId']}{sub['problem']['index']}",
                }
            )
    print(len(accs), accs[0])

    for sub in accs:
        sub["code"] = getCode(sub["link"])


if __name__ == "__main__":
    main()
