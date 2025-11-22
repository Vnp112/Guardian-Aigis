# app/ingest/pull_from_router.py
import subprocess
from pathlib import Path

ROUTER_IP = "192.168.8.1"
REMOTE = "/etc/AdGuardHome/data/querylog.json"
LOCAL = Path("data/querylog.json")
IDENTITY = Path.home() / ".ssh" / "id_ed25519"

def pull_logs():
    cmd = [
        "scp",
        "-O", # use scp mode due to no sshfs
        "-i", str(IDENTITY),
        f"root@{ROUTER_IP}:{REMOTE}",
        str(LOCAL),
    ]
    subprocess.run(cmd, check=True)
