import requests
import qrcode
import time

# 当前暂未实现自动化获取二维码,先完成一个手动的版本

id = input("请输入活动ID: ")
now_time = int(round(time.time()))
url_QD = id + "|"+str(now_time) +"|"+ "QD"
print("有效期" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time)))
img = qrcode.make(url_QD)
print("签到二维码已生成,请在当前目录下查看(qrcode_QD.png)")
img.save("qrcode_QD.png")

url_QT = id +"|"+ str(now_time) +"|"+ "QT"
print("有效期" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time)))
img = qrcode.make(url_QT)
print("签退二维码已生成,请在当前目录下查看(qrcode_QT.png)")
img.save("qrcode_QT.png")
