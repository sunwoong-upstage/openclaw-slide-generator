#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

state_path = Path(sys.argv[1])
status = sys.argv[2]
phase = sys.argv[3]
summary = sys.argv[4]

if state_path.exists():
    data = json.loads(state_path.read_text(encoding='utf-8'))
else:
    data = {"version": 1, "system": "openclaw-flow"}

data["status"] = status
data["current_phase"] = phase
data["summary"] = summary
data["last_updated"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

state_path.parent.mkdir(parents=True, exist_ok=True)
state_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print(state_path)
