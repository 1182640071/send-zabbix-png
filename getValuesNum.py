#coding=utf-8
import json
import urllib2,time

class getNUM():
    def getPng(self ,  hostid ,token='',url='',header={"Content-Type":"application/json"}):
        # based url and required header
        url = "http://ip:port/zabbix/api_jsonrpc.php"
        header = {"Content-Type":"application/json"}
        # request json
        data = json.dumps(
        {
           "jsonrpc":"2.0",
           "method":"history.get",
            # history参数可能的取值
            # 0 - float;
            # 1 - string;
            # 2 - log;
            # 3 - integer;
            # 4 - text.
           "params":{
               "output":"extend",
               "history":3,
               "sortfield":"clock",
               "itemids":"24407",
               "sortorder":"DESC",
               "limit":600
           },
           "auth":"eb9c2a73493243deef3b8de155bc13d6", # theauth id is what auth script returns, remeber it is string
           "id":1,
        })
        # create request object
        request = urllib2.Request(url,data)
        for key in header:
           request.add_header(key,header[key])
        # get host list
        try:
           result = urllib2.urlopen(request)
        except Exception as e:
           if hasattr(e, 'reason'):
               print 'We failed to reach a server.'
               print 'Reason: ', e.reason
           elif hasattr(e, 'code'):
               print 'The server could not fulfill the request.'
               print 'Error code: ', e.code
        else:
           response = json.loads(result.read())
           result.close()
           print "in- Number Of Hosts: ", len(response['result'])
           for host in response['result']:
               # print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(host["clock"]))) + ' , ' + str(int(host["value"]))
               # print time.strftime("%Y-%m-%d",time.localtime())
               print host["clock"],host["value"]