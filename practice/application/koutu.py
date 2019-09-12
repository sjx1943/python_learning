import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('/Users/SJX/Desktop/784695892.jpg', 'rb')},
    data={'size': 'auto','bg_color':''},
    headers={'X-Api-Key': 'bC4g1HtvXkGGuzdfpfZ6k8wo'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)

