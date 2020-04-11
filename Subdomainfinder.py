#this script will find the subdomain for anywebsite available. Well You need a good wordlist, which I'll put in the same repo.

#start -------->

import requests
url =""
def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass

#put the website name in this variable(target_url) just put like talktovik.github.io or anything.
target_url = ""
with open("/Users/apple/Downloads/wordlist_subdomain_udm.txt","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word +"." + target_url
        response =request(test_url)
        if response:
            print("[+] Discovered the subdomain -->" + test_url)
