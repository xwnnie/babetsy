import requests
import json
from datetime import datetime


url = "http://127.0.0.1:5000/api/orders"

payload = {"created_at": "2022-06-08T05:04:39.080Z",
           "order_number": "ORDER_613891865925189", "buyer_id": 1, "products": [{"product_id": 2, "quantity": 8}, {"product_id": 1, "quantity": 6}]}

headers = {'Content-Type': 'application/json',
    'csrf_token': 'ImUyYTk5ZGFiZGI0M2RhNTdlZDZiZDMzNjVkNGM1NWVlMTQ1NTkzOGMi.YpBaaQ.iv2Pc7GgVA-dUpMwVRgHda6gLYA',
    'session': 'eyJjc3JmX3Rva2VuIjoiZTJhOTlkYWJkYjQzZGE1N2VkNmJkMzM2NWQ0YzU1ZWUxNDU1OTM4YyJ9.YpBaaQ.BpSS6YphsQ-UQZANHJ2l00oK3TQ',
    'Cookie': 'session=.eJwljs1qwzAQhF9F6ByKfleSnyL3EsyudhWbunGxnFPIu1elp5lhhuF76blt2Bfpevp8aXUO0d_SO95FX_R1E-yitv2u1oc6d4W1jlKdy9rVz9h86Nv7dhknh_RFT-fxlJFW1pN2GSEFQkfRDQexQjIhBY_OW0_ZEZfKUWoLIph9AmewCYitDmLOUChgSEnYl8Y5OsdCWECEW_M-UomMBJRBHIRokUptFDgY4wM0M_DnZ5fjn8aOWPvR5nP_kscfnrGCXMZFBSZyUJpn5JgplZY4G6iDEqx-_wJ0FFew.YqAkuQ.Sxlzzwd7GgUTo4MyXJcy6tNtfSc; csrf_token=IjIwMWVhZDlkYWJjNmRiYjI2OWYzZGFkNThiNzlmN2Q4MDZjMTNiNjEi.YqAkzw.hhQkNR3Uby0uVXHAhFMgLkZallw'
}
payload = json.dumps(payload)

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
