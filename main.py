import requests
import time

url = 'https://test1ng.com/'  # replace with your website

while True:  # always will be true so runs forever
    response = requests.get(url)
    #if response.status_code == 200:
    #    print('Website is up.')
    #else:
    #    print('Website is down. Status code:', response.status_code)
    time.sleep(3)