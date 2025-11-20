from fastapi import FastAPI
from pathlib import Path
import pandas as pd
import json

app = FastAPI()

def load_file(file):
    if not file.exists():
        return pd.DataFrame()
    return pd.read_csv(file)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/ping")
async def get_ping():
    return {"status": "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}"}


@app.get("/alerts")
def get_alerts():
    path = Path("data/alerts.csv")
    # if not path.exists():
    #     return {"alerts": []}
    # alerts_csv = pd.read_csv(path)
    alerts_csv = load_file(path)
    # Iterative method
    # rows = []
    # for idx, row in alerts_csv.iterrows():
    #     rows.append({"client_ip": row["client_ip"],
    #                  "minute": row["minute"],
    #                  "qpm": row["qpm"],
    #                  "uniq": row["uniq"],
    #                  "avg_len": row["avg_len"],
    #                  "score": row["score"]})
    
    # Pandas built in conversion
    rows = alerts_csv.to_dict(orient="records")
    return {"alerts": rows}

@app.get("/devices")
def get_devices():
    path = Path("data/features.csv")
    features_csv = load_file(path)
    rows = features_csv.to_dict(orient="records")
    devices = sorted(set([row["client_ip"] for row in rows]))
    return {"devices": devices}
    
@app.get("/devices/{ip}/history")
def get_device_history(ip: str):
    path = Path("data/features.csv")
    features_csv = load_file(path)
    if not path.exists():
        return {"ip": ip, "history": []}
    ip_data = features_csv[features_csv["client_ip"] == ip].sort_values("minute")
    ip_data = ip_data.to_dict(orient="records")
    return{"ip": ip, "history": ip_data}
    
@app.get("/features")
def get_features():
    path = Path("data/features.csv")
    if not path.exists():
        return {"features": []}
    features_csv = load_file(path)
    features = features_csv.to_dict(orient="records")
    return {"features": features}