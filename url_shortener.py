import pyshorteners

url = input("Enter your url: ")
short_url = pyshorteners.Shortener().tinyurl.short(url)
print(short_url)
