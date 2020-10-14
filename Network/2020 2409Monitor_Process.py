#Allow less secure apps: google search bật tính năng đăng nhập third party

import sqlite3 as lite
import os
import time
from Send_Email_alert import SendEmail
 
path = os.path.dirname(__file__) + "\\db.sqlite3"
con = lite.connect(path)   
 
while 1:
    with con:
        # row_factory: Dữ liệu trả về là Dictionary
        con.row_factory = lite.Row
        cur = con.cursor() 

        cur.execute("SELECT * FROM cisco_device_ip")
        rows = cur.fetchall()

        for row in rows:
            print ("%s %s %s %s %s %s" % (row["id"], row["name"], row["ip"], row["status"], row["description"], row["date"]))
            # Kiểm tra trạng thái sử dụng Ping 3 gói ICMP.
            response = os.system("ping -n 3 " + row["ip"])
            print(response)
            if response == 0: # thiết bị up với response =  0. 
                if row["status"] == 0:
                    # cập nhật database
                    cur.execute("UPDATE cisco_device_ip SET status=? WHERE ip=?", (1, row["ip"]))
                    con.commit()
                    subject = ("%s IP: %s đã up trở lại!" % (row["name"], row["ip"] ) )
                    to = "linhnh@tosy.com"
                    body = "Device Already up."
                    SendEmail(subject, to, body)
                    print("%s đã up trở lại!" % (row["name"]) ) # gửi mail với nội dung trên.
                else:
                    pass

            else: # thiết bị down với response = 1
                subject = ("%s IP: %s cảnh báo thiết bị down!" % (row["name"], row["ip"]) )
                to = "linhnh@tosy.com"
                body = "Thiết bị down đề nghị xử lý sự cố."
                SendEmail(subject, to, body)
                print("%s cảnh báo thiết bị down!" % (row["name"]) ) # gửi mail với nội dung trên.
                if row["status"] == 0: 
                    pass
                else:
                    # cập nhật database
                    cur.execute("UPDATE cisco_device_ip SET status=? WHERE ip=?", (0, row["ip"]))
                    print("%s cảnh báo thiết bị down!" % (row["name"]) ) # gửi mail với nội dung trên.
                    con.commit()
          
    time.sleep(5)

