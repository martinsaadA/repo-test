import requests
import json

# Exposed Slack token (DO NOT USE IN PRODUCTION)
SLACK_TOKEN = "xoxb-1234567890-1234567890123-aBcDeFgHiJkLmNoPqRsTuVwX"

def send_slack_message(channel, message):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": channel,
        "text": message
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def get_channel_list():
    url = "https://slack.com/api/conversations.list"
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    # Send a message to a channel
    channel = "#general"
    message = "Hello from the test script!"
    result = send_slack_message(channel, message)
    print(f"Message sent: {result['ok']}")

    # Get list of channels
    channels = get_channel_list()
    if channels['ok']:
        print("Available channels:")
        for channel in channels['channels']:
            print(f"- {channel['name']}")
    else:
        print(f"Error fetching channels: {channels['error']}")

if __name__ == "__main__":
    main()
