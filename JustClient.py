#coding=utf-8
#create by wml
#date 2017.09.14
from zabbixFunction import ZabbixFunction
from sendEmail import send
import ConfigParser , time , datetime

url="http://ip:port/zabbix/api_jsonrpc.php"   #192.168.168.147
urlvalue="http://ip:port/zabbix/index.php"
urlpng="http://ip:port/zabbix/chart2.php"
dataType={"Content-Type":"application/json"}
user='username'
password='passwd'
type='png' #png代表图片   value代表数据
token='268b118a45f419b20f56cc6776d23637'   #268b118a45f419b20f56cc6776d23637
path='zabbixpng' #zabbixpng
period=86400 #数据持续时间
pngwidth=1200
pngheight=800 #当type为'png'时,此字段表示数据数量
starttime='20170913000000'
size = 60


inforList = {}

def getPng(itemId):
    zabbix_function = ZabbixFunction(url, dataType ,user , password , urlpng , urlvalue , token , size)
    return zabbix_function.getValue( itemId ,type , path , period , starttime, pngwidth , pngheight)

def getGroupList():
    return ZabbixFunction().getGroupList(token , url , dataType)

def getHostId(groupId):
    return ZabbixFunction().getHostList( groupId , token , url , dataType)

def getItemId(histId):
    return ZabbixFunction().getItemList( type , histId , token , url , dataType)

def getToken():
    zabbix_function = ZabbixFunction(url, dataType ,user , password , urlpng , urlvalue , token , size)
    return zabbix_function.getToken()

if __name__ == "__main__":

    print '11'
