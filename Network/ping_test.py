import os


def CheckPing(address):
    response = os.system("ping -n 1 " + address)
    print(response)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus


host = '8.8.8.81'
CheckPing(host) 
