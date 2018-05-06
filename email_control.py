import smtplib
import imapclient

import time

try: 
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imapObj.login('kyawkyawassistance@gmail.com', '232322989')
    imapObj.select_folder('INBOX', readonly=True)
    imapObj.search(
except:
    print("Something went wrong..")


