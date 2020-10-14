import psutil
import  platform
import socket
import shutil


def hostname():
    name = str(platform.node())
    return name

def ip():
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def cpuinfor():
    cpu = str(psutil.cpu_percent())   + " %"  
    return cpu

def raminfor():
    ram = str(psutil.virtual_memory().percent)   + " %"   
    return ram

def hardisk():
    total, used, free = shutil.disk_usage("/")
    Total = total // (2**30)
    Used = used // (2**30)
    Free = free // (2**30)
    Alls = ("Total: %d GiB" % (total // (2**30))) + " //" + ("Used: %d GiB" % (used // (2**30))) +  " //" + ("Free: %d GiB" % (free // (2**30)))
    return Alls




