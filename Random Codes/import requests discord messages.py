import requests

print("Started!")

token = 'MTExNzU2MjU2MjI0Mjk0NTA2NQ.GF4u9i.zt8GmX-NFEuk7dW6gmXuHG8RU6Qo1OqtaWfC64'
channel_id = '1119674681411248169'

send_message_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

payload = {
    'content': 'كلزق'
}

headers = {
    'Authorization': token
}
response = requests.post(send_message_url, json=payload, headers=headers)

if response.status_code == 200:
    print("Message sent successfully")
    
    message_id = response.json()['id']
    
    delete_message_url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}'
    
    response_delete = requests.delete(delete_message_url, headers=headers)
    
    if response_delete.status_code == 204:
        print("Message deleted successfully")
    else:
        print("Failed to delete message:", response_delete.text)
else:
    print("Failed to send message:", response.text)

print("Done!")
