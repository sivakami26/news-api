import requests
import send_email

query_keyword = input("Enter the keyword for the news result: ")
url = f"https://newsapi.org/v2/everything?q={query_keyword}&from=2023-09-18\
       &sortBy=publishedAt&apiKey=f6021749ae1a4065b25aa271e0af4006&language=en"

request = requests.get(url)

content = request.json()


message = ("""Subject: Today's news
 
""")
for article in content["articles"][:20]:
    message = (message + article["title"] + "\n"  \
               + article["description"] + "\n"  + article["url"]+ 2*"\n")

message_bytes = message.encode('utf-8')
send_email.send_email(message_bytes)
print("Email alert is sent out successfully")