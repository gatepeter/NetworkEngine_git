#Allow less secure apps: google search bật tính năng đăng nhập third party

import sqlite3 as lite
import subprocess, os
import time
from Send_Email_alert import SendEmail
from  SendSkype import SendSky
from threading import Thread
import psutil
from ServerInfor import hostname, ip, cpuinfor, raminfor, hardisk
 

 

def DasboardMonitor():
    path = os.path.dirname(__file__) + "\\db.sqlite3"
    con = lite.connect(path)   
    while 1:
        print('thread_01')
        with con:
            # row_factory: Dữ liệu trả về là Dictionary
            con.row_factory = lite.Row
            cur = con.cursor() 

            cur.execute("SELECT * FROM cisco_device_ip")
            rows = cur.fetchall()

            for row in rows:
                # print ("%s %s %s %s %s %s %s" % (row["id"], row["name"], row["ip"], row["status"], row["description"], row["EnableMonitor"],row["date"]))
                # Kiểm tra trạng thái sử dụng Ping 3 gói ICMP.
                a = 3
                output = subprocess.Popen(["ping.exe","-n", str(a) ,row["ip"]],stdout = subprocess.PIPE).communicate()[0]
                # print(output)
                
                if 'Enable' in str(row["EnableMonitor"]):
                    if  (('unreachable' in str(output)) or ('timed out' in str(output))):
                        # print("Offline")
                        subject = ("%s IP: %s cảnh báo down!" % (row["name"], row["ip"]) )
                        to = "linhnh@tosy.com;ngohoanglinh.dtk5@gmail.com"
                        body = "Cảnh báo Down đề nghị xử lý sự cố."
                        SendEmail(subject, to, body)
                        SendSky(subject)
                        # print("%s cảnh báo thiết bị down!" % (row["name"]) ) # gửi mail với nội dung trên.
                        if row["status"] == 0: 
                            pass
                        else:
                            # cập nhật database
                            cur.execute("UPDATE cisco_device_ip SET status=? WHERE ip=?", (0, row["ip"]))
                            # print("%s cảnh báo thiết bị down!" % (row["name"]) ) # gửi mail với nội dung trên.
                            con.commit()

                    # if response == 0: # thiết bị up với response =  0. 
                    else:
                        if row["status"] == 0:
                            # cập nhật database
                            cur.execute("UPDATE cisco_device_ip SET status=? WHERE ip=?", (1, row["ip"]))
                            con.commit()
                            subject = ("%s IP: %s đã Up!" % (row["name"], row["ip"] ) )
                            to = "linhnh@tosy.com;ngohoanglinh.dtk5@gmail.com"
                            body = "Device Already Up."
                            SendEmail(subject, to, body)
                            SendSky(subject)
                            # print("%s đã up trở lại!" % (row["name"]) ) # gửi mail với nội dung trên.
                        else:
                            pass
                else: pass
            
        time.sleep(5)

def MonitorWeb():
    path = os.path.dirname(__file__) + "\\db.sqlite3"
    con = lite.connect(path) 
    # print('thread_02')
    while 1:
        print('thread_02')
        with con:
        # row_factory: Dữ liệu trả về là Dictionary
            con.row_factory = lite.Row
            cur = con.cursor() 
            Name = str(hostname())
            Ip = str(ip())
            Cpu = str(cpuinfor())
            Ram = raminfor()
            Hd = hardisk()
            cur.execute("UPDATE cisco_server SET hostname=?  WHERE id=?", (Name,1))
            cur.execute("UPDATE cisco_server SET ip=?  WHERE id=?", (Ip,1))
            cur.execute("UPDATE cisco_server SET cpu=?  WHERE id=?", (Cpu,1))
            cur.execute("UPDATE cisco_server SET ram=?  WHERE id=?", (Ram,1))
            cur.execute("UPDATE cisco_server SET hardisk=?  WHERE id=?", (Hd,1))
            con.commit()
        time.sleep(10)
    
ThreadDasboardMonitor=Thread(target=DasboardMonitor)
ThreadDasboardMonitor.start()
# ThreadDasboardMonitor.join()
    
ThreadMonitorWeb=Thread(target=MonitorWeb)
ThreadMonitorWeb.start()
# ThreadMonitorWeb.join()

print("Finished")
