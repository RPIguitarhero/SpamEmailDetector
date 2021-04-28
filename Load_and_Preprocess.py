'''
Author:Kai Kang
Description:simple file loader and text preprocessor

'''
import mailbox
#function to get email text from email body
def preprocess(msg): #getting plain text 'email body'
    body = None
    #single body email
    if msg.get_content_type() == 'text/plain':
        body = msg.get_payload(decode=True)   
    #multiboy email       
    elif msg.is_multipart():
        for part in msg.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    #return mail text which concatenates both mail subject and body
    mailcontent=str(msg['subject'])+" "+str(body)
    return mailcontent


    