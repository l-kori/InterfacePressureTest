import requests
import json
import time
import smtplib
import threading as thd
from apscheduler.schedulers.blocking import BlockingScheduler
from email.mime.text import MIMEText
from email.utils import formataddr
#实时量化
def sslh():
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    time1 = time.strftime("%H%M", time_local)
    res = requests.get("https://pre-serverplus.huanshoulv.com/aimapp/stock/fundflowBlocks?block_type=3&data_count=30&date_type=1&device_id=184499f0b92018b4c03c7952de6c6f58569c64c3&device_token=c624c097e1e5dd12aa62ad46e685e65a9ac265db242e901ce09baecc29a11605&div=IOSH010912&hsl_id=5c0dbfc02c2eea2a80fad73c&inflow_type=1&ts=1554486429")
    r = res.text
    rr = json.loads(r)
    long = len(rr["data"])
    if long == 0 :
        failure_send("实时量化")
    else:
        # success_send("实时量化")
        print("实时量化数据正常")
#大单净额
def ddje():
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    time1 = time.strftime("%H%M", time_local)
    # print(type(time1))
    if int(time1) <=1500 :
        res = requests.get("https://pre-serverplus.huanshoulv.com/aimapp/stock/fundflowLineJG/600018.SS?device_id=184499f0b92018b4c03c7952de6c6f58569c64c3&device_token=c624c097e1e5dd12aa62ad46e685e65a9ac265db242e901ce09baecc29a11605&div=IOSH010912&hsl_id=5c0dbfc02c2eea2a80fad73c&min_time="+str(time1)+"&ts=&with_ca=1")
        # print(res.url)
        r = res.text
        rr = json.loads(r)
        try:
            falg = any(rr['data']['list'][0][7])
            print("大单净额数据正常")
        except Exception:
            failure_send("大单净额")
    else:
        print("大单净额数据正常")
        pass
#分时量
def fsl():
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    time1 = time.strftime("%H%M", time_local)
    res = requests.get("https://pre-serverplus.huanshoulv.com/aimapp/stock/basicCa/000607.SZ?device_id=184499f0b92018b4c03c7952de6c6f58569c64c3&device_token=c624c097e1e5dd12aa62ad46e685e65a9ac265db242e901ce09baecc29a11605&div=IOSH010912&fundflow_min_time=&hq_type_code=&hsl_id=5c0dbfc02c2eea2a80fad73c&min_time="+str(time1)+"&new_tick=true&tick=1&tick_filter_callauction=false&ts="+str(time_now)+"&with_lastday=1")
    r = res.text
    # print(res.url)
    rr = json.loads(r)
    # print(rr["data"]["stockData"]["current_amount"])
    falg = any(rr["data"]["stockData"]["current_amount"])
    if falg is False :
        failure_send("分时量")
    else:
        # success_send("实时量化")
        print("分时量数据正常")

def success_send(a):
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    time1 = time.strftime("%H%M", time_local)
    ret = True
    try:
        # 邮件内容
        msg = MIMEText(str(time1) +a+"The result is data.", 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["赖显东", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["赖显东", my_user])
        # 邮件的主题
        msg['Subject'] = a+"实时状态"

        # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
        # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
        # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(my_sender, my_pass)
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        # 关闭连接
        server.quit()
        # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception:
        ret = False
        print(ret)


def failure_send(a):
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    time1 = time.strftime("%H%M", time_local)
    ret = True
    try:
        # 邮件内容
        msg = MIMEText(str(time1) +a+"The result is not data.", 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["赖显东", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["赖显东", my_user])
        # 邮件的主题
        msg['Subject'] = a+"实时状态"

        # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
        # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
        # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(my_sender, my_pass)
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        # 关闭连接
        server.quit()
        # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception:
        ret = False
        print(ret)

def fn():
    sslh()
    ddje()
    fsl()
    thd.Timer(10, fn).start()



if __name__ == '__main__':
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    time1 = time.strftime("%H%M", time_local)

    # 发件人邮箱账号
    my_sender = 'laixiandong@huanshoulv.com'
    # user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
    my_pass = 'Kori19981215'
    # 收件人邮箱账号
    my_user = 'laixiandong@huanshoulv.com'
    # sslh()
    # ddje()
    # fsl()
    scheduler = BlockingScheduler()
    print("任务启动")
    scheduler.add_job(fn, 'cron', day_of_week='0-4', hour=16, minute=8)
    scheduler.start()


