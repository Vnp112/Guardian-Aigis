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
    with open(JSON_IN) as f:
        obj = json.load(f)
    entries = obj["data"]
    rows = []
    for entry in entries:
        #print(entry["question"]["type"])
        rows.append({"time": entry["time"],
                     "client_ip": entry["client"],
                     "domain": entry["question"]["name"],
                     "qtype": entry["question"]["type"]})
    
    df = pd.DataFrame(rows)
    df.to_csv(OUT, index=False)
    return df
