from skpy import Skype
phone = '0987610269'
passw = 'linh260989'
sk = Skype(phone, passw)

def SendSky(msgsky):
    contact = sk.contacts['live:.cid.62b8fe298b0d3995'] 
    contact.chat.sendMsg(msgsky)





# SendSky('how a u')