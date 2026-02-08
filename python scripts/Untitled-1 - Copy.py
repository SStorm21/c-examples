
def test():
    import requests
    for i in range(1):
        message="هلا فيك"#input('( * ) message:> ')
        token ="MTIwMDkwMTIzNDE4NjUzMDkxNg.GfBveD.mEMhkmy68Srrqj2vLZVLvSQVFVhvIvii7at74s"#input('( + ) token >: ')
        channel_id="1228299028303708171"#input('( * )channel id :> ')
        message = str(message)
        url=f'https://discord.com/api/v9/channels/{channel_id}/messages'
        payload = {
            'content': message}
        headers = {
            'Authorization': token
        }            
        res=requests.post(url,json=payload,headers=headers)
        print(res.text)
        message="2هلا فيك"#input('( * ) message:> ')
        token ="MTIwMDkwMTIzNDE4NjUzMDkxNg.GfBveD.mEMhkmy68Srrqj2vLZVLvSQVFVhvIvii7at74s"#input('( + ) token >: ')
        channel_id="1228299028303708171"#input('( * )channel id :> ')
        message = str(message)
        url=f'https://discord.com/api/v9/channels/{channel_id}/messages'
        payload = {
            'content': message}
        headers = {
            'Authorization': token
        }            
        res=requests.post(url,json=payload,headers=headers)
        print(res.text)
test()