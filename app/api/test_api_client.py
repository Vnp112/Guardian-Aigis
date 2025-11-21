import requests

BASE = "http://127.0.0.1:8000"

def test_alerts():
    r = requests.get(f"{BASE}/alerts", timeout=5)
    print("Status:", r.status_code)
    data = r.json()
    print("Keys:", data.keys())
    print("First alert:", data["alerts"][0] if data["alerts"] else None)

def test_devices():
    r = requests.get(f"{BASE}/devices", timeout=5)
    print("Devices:", r.json()["devices"])

def test_history(ip: str):
    r = requests.get(f"{BASE}/devices/{ip}/history", timeout=5)
    data = r.json()
    print("IP:", data["ip"])
    print("Num windows:", len(data["history"]))

if __name__ == "__main__":
    test_alerts()
    test_devices()
    test_history("192.168.8.135")  # swap with one from /devices
