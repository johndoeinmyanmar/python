import requests
import json

base_url = 'https://graph.facebook.com/me'
access_token = 'EAACEdEose0cBAIiZBwY1AaTQR4B0uqyy0t9ZBwQidYZB4zy0p3OV48lmZCNrZA7ispuqpp3r75yMUZBiLu9rRTW7iMhrFZCfPOOxw4S7z4OE6RM5k1SLFI6futjutDGiZBjZBfB0LsWqnkZAUz3ehw4naKT3C78hTCyxzWHOr6Xkz9r4I9IClxY21m3TeFpCr59s4ZD'

# Get 10 likes for 10 friends
fields = 'id,name,friends.limit(10).fields(likes.limit(10))'

url = '%s?fields=%s&access_token=%s' %(base_url, fields, access_token,)

print(url)

content = requests.get(url).json()

print(json.dumps(content, indent=1))
