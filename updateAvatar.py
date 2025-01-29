import requests

imagePaths = {
    "angry" : "emojis/angry.jpg",
    "happy" : "emojis/happy.jpg",
    "neutral" : "emojis/neutral.jpg",
    "sad" : "emojis/sad.jpg",
    "surprise" : "emojis/surprise.jpg"
}

def updateAvatar(userName, userSecret, emoji):
    url = "https://api.chatengine.io/users/me/"
    filePath = imagePaths[emoji]
    payload={}
    files=[
    ('avatar',('Emoji.jpg',open(filePath,'rb'),'image/jpg'))
    ]
    headers = {
    'Project-ID': 'e3c6d59c-392a-4895-98dd-abec2b82acb2',
    'User-Name': userName,
    'User-Secret': userSecret
    }
    print('from update:', emoji)
    response = requests.request("PATCH", url, headers=headers, data=payload, files=files)


