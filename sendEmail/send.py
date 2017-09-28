#!/usr/bin/env python
#coding: utf-8
#该脚本是以图片作为内容发送的，没加入该说明前测试是正常可用的。
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

mailto_list=['wangminglang@guodulink.net','1182640071@qq.com']
mail_host="smtp.exmail.qq.com"  #设置服务器
mail_user="username"    #用户名
mail_pass="passwd"   #口令
mail_postfix="gdlk.net"  #发件箱的后缀

def send_mail(to_list,sub , path):
    def addimg(src,imgid): #文件路径、图片id
        fp = open(src, 'rb')  #打开文件
        msgImage = MIMEImage(fp.read()) #读入 msgImage 中
        fp.close() #关闭文件
        msgImage.add_header('Content-ID', imgid)
        return msgImage

    msg = MIMEMultipart('related')
    #HTML代码
    msgtext = MIMEText("""
    <table width="600" border="0" cellspacing="0" cellpadding="4">
          <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
            <td colspan=2>*数据信息</td>
          </tr>
          <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
             <img src="cid:io"></td><td>
          </tr>

        </table>""","html","utf-8")
    msg.attach(msgtext)
    msg.attach(addimg(path,"io")) #全文件路径，后者为ID 根据ID在HTML中插入的位置
    # msg.attach(addimg("a.png","key_hit")) #同上
    # msg.attach(addimg("a.png","men"))#同上
    # msg.attach(addimg("a.png","swap"))#同上
    me=mail_user
    msg['Subject'] = sub  #主题
    msg['From'] = me   #发件人
    msg['To'] = ";".join(to_list) #收件人列表
    try:
        server = smtplib.SMTP()  #SMTP
        server.connect(mail_host)  #连接
        server.login(mail_user,mail_pass) #登录
        server.sendmail(me, to_list, msg.as_string()) #发送邮件
        server.close()  #关闭
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mailto_list,"zabbix流量图", '../zabbixpng/3521.png'):
        print "发送成功"
    else:
        print "发送失败"