import requests

#payload = {
#    'content':'hello world'
#}#
#header = {
#    'authorization':"MTEwMDQ5MjI3NjkxMzkzNDQ4Ng.GPHzRH.Y4_eX2g06RKfbjB_I8SoR4NaJ1mSPY95h2sCK4"
#}
#r = requests.post('https://discord.com/channels/1116702802924806265/1177419524241362994',
#                  json=payload,headers=header)



# Replace these values with your actual router's IP address and login credentials
router_ip = '192.168.0.1'
username = 'admin'
password = 'admin'

# Replace this with the MAC address of the device you want to block
mac_address = '0C:FE:45:ED:3C:23'

# Build the URL for the access control API endpoint
url = f'http://192.168.0.1/api/access_control'

# Create a session and authenticate with the router
session = requests.Session()
login_data = {
    'username': username,
    'password': password
}
session.post(f'http://192.168.0.1', data=login_data)

# Add the device to the access control list
access_control_data = {
    'action': 'block',
    'mac_address': mac_address
}
response = session.post(url, data=access_control_data)

# Check the response
if response.status_code == 200:
    print("Device successfully added to access control list.")
else:
    print("Failed to add device to access control list.")




