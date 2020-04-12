import requests
url =""
def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = input("what is the name of target website.please don't add https:// with url")
with open("","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url +  "/" + word
        response =request(test_url)
        if response:
            print("[+] Discovered the path -->" + test_url)
