import hashlib
import hmac
import json
from datetime import datetime, timezone

import requests

payload = {
    "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "name": "Nguyen Minh Quoc",
    "email": "nguyenminhquocbk@gmail.com",
    "resume_link": "https://drive.google.com/file/d/1_vB8nzgGIWESZEiwsA9UG6fENgWsm4Eb/view?usp=sharing",
    "repository_link": "https://github.com/nminhquoc/b12-application",
    "action_run_link": "TO_BE_FILLED"
}

json_payload = json.dumps(payload, separators=(',', ':'), sort_keys=True)
secret = b"hello-there-from-b12"
signature = hmac.new(
    secret,
    json_payload.encode("utf-8"),
    hashlib.sha256
).hexdigest()

headers = {
    'Content-Type': 'application/json',
    'X-Signature-256': f'sha256={signature}'
}


def main():
    response = requests.post(
        "https://b12.io/apply/submission",
        data=json_payload,
        headers=headers
    )
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    if response.status_code == 200:
        data = response.json()
        print("RECEIPT:", data.get("receipt"))


if __name__ == '__main__':
    main()
