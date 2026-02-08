import requests
import json

url = 'https://discord.com/api/v9/science'
token = "MTIwMDkwMTIzNDE4NjUzMDkxNg.NOEw9R6XHvXOZy7HMW0ooZwBRT4"

# Properly structure the events payload as a JSON array
events_payload = [
    {
        "type": "client_theme_updated",
        "properties": {
            "client_track_timestamp": 1716300304401,
            "accessibility_features": 2621696,
            "client_app_state": "focused",
            "client_heartbeat_session_id": "bc2053b9-10ca-44a5-9a87-303c1014306a",
            "client_performance_memory": 0,
            "client_rtc_state": "DISCONNECTED",
            "client_send_timestamp": 1716300304465,
            "client_track_timestamp": 1716300304401,
            "client_uuid": "ZDAEUk91qhCQ86JZ1w53m48BAAA6AAAA",
            "feature_name": "client_theme",
            "is_persisted": True,
            "location_stack": ["user settings", "client themes theme selector"],
            "rendered_locale": "en-US",
            "theme_name": "default dark",
            "uptime_app": 82
        }
    }
]

payload = {
    'events': json.dumps(events_payload),
    'token': token
}

headers = {
    'Authorization': f'Bot {token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)
