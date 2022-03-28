import requests
import hashlib


def pwned_check(password):
    
    password = password.encode()  # Turns it into bytes
    
    hashed_password = hashlib.sha1(password).hexdigest()  # Api recuires sha1 hash

    url = "https://api.pwnedpasswords.com/range/" + hashed_password[:5]  
    # Sends first five characters

    pwned_request = requests.get(url)
    pwned_list = pwned_request.text.splitlines()

    secure = True

    for i in pwned_list:
        if i[:i.find(":")].lower() == hashed_password[5:].lower():
            secure = False  # Checks if it is in the returned list

    return secure
