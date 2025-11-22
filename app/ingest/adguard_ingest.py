import requests
import pandas as pd
from pathlib import Path
import json

ADGUARD_URL = "http://192.168.8.1/control/querylog?limit=1000"
JSON_IN = Path("data/querylog.json")
OUT = Path("data/sample_dns.csv")

# resp = requests.get(ADGUARD_URL)
# data = resp.json()
# print(resp.status.code)
# print(resp.text[:200])

def adguard_ingest_from_file(json_path: Path = JSON_IN, out_path: Path = OUT):
    """
    Read an AdGuard querylog JSON file (with top-level 'data' list),
    normalize to time,client_ip,domain,qtype and write CSV.
    """
    rows = []

    with open(json_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            # each line is a separate JSON object
            obj = json.loads(line)

            # keys based on the sample you showed:
            # {"T": "...", "QH": "...", "QT": "...", "IP": "...", ...}
            rows.append({
                "time": obj.get("T"),
                "client_ip": obj.get("IP"),
                "domain": obj.get("QH"),
                "qtype": obj.get("QT"),
            })

    if not rows:
        df = pd.DataFrame(columns=["time", "client_ip", "domain", "qtype"])
    else:
        df = pd.DataFrame(rows)

    df.to_csv(out_path, index=False)
    return df
