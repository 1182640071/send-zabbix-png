#coding=utf-8
#create by wml
#date 2017.09.14
import sys
import datetime
import cookielib, urllib2,urllib

class getPNG():
    '''
    生成png图片,从zabbix接口中获得
    '''
    def __init__(self ,upper , period , starttime , path , width , height):
        self.url = upper.urlvalue
        self.urlpng = upper.urlpng
        self.user = upper.user
        self.password = upper.password
        self.period = period
        self.starttime = starttime
        self.width = width
        self.height = height
        self.path = path


    def getoper(self,url,name,password):
        #初始化的时候生成cookies
        cookiejar = cookielib.CookieJar()
        urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
        values = {"name":name,'password':password,'autologin':1,"enter":'Sign in'}
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data)
        try:
            urlOpener.open(request,timeout=10)
            return urlOpener
            # self.urlOpener=urlOpener
        except urllib2.HTTPError, e:
            print 'error: ' ,e

    def GetGraph(self , s ,url,values,image_dir):
        key=values.keys()
        if "graphid" not in key:
            print u"请确认是否输入graphid"
            sys.exit(1)
        #以下if 是给定默认值
        if  "period" not in key :
            #默认获取一天的数据，单位为秒
            values["period"]=86400
        if "stime" not in key:
            #默认为当前时间开始
            values["stime"]=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        if "width" not in key:
            values["width"]=800
        if "height" not in key:
            values["height"]=200
        data=urllib.urlencode(values)
        request = urllib2.Request(url,data)
        url = s.open(request)
        image = url.read()
        imagename="%s/%s.png" % (image_dir, values["graphid"])
        f=open(imagename,'wb')
        f.write(image)

    def getPng(self , itemID):
        urlopener=self.getoper(self.url,self.user,self.password)
        if urlopener is None:
            print '[ERROR]zabbix接口链接错误'
            exit(1)
        else:
            values={"graphid":itemID,"period":self.period,"stime":self.starttime,"width":self.width,"height":self.height}
            self.GetGraph(urlopener,self.urlpng,values,self.path)
