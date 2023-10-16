import requests
import send_email

url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-09-16\
       &sortBy=publishedAt&apiKey=f6021749ae1a4065b25aa271e0af4006")

request = requests.get(url)

content = request.json()


message = ("""Subject: Your daily news alert for Tesla 
""")
for article in content["articles"]:
    message = message + article["title"] + "\n" + article["description"] + 2*"\n"

message_bytes = message.encode('utf-8')
send_email.send_email(message)
print("Email alert is sent out successfully")