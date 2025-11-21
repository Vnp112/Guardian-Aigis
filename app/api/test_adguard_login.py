import requests

ADGUARD_URL = "http://192.168.8.1"

def test_login():
    s = requests.Session()
    payload = {"password": "pword"}

    r = s.post(f"{ADGUARD_URL}/control/login", json=payload)

    print("Login status:", r.status_code)
    print("Cookies:", s.cookies)

    r2 = s.get(f"{ADGUARD_URL}/control/status")
    print("Status code for /control/status:", r2.status_code)
    print("Response:", r2.text)

if __name__ == "__main__":
    test_login()