# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 上午10:52
# @Author  : WeiChunXi
# @Email   : 15991652432@163.com
import requests

url = "http://117.34.74.220:8010/XHMonitoringServer/account/api/login"

payload = "{\n  \"systemName\" : \"榆林系统\",\n  \"appVersion\" : \"7.0.1\",\n  \"deviceIdentifier\" : \"6HdVuA0gGnP5XiIbS8DdDfPRiyHQxiidxiIgcgrGA16QcPTVy8lNUaSMZL8ysShI\",\n  \"osVersion\" : \"12.0\",\n  \"deviceType\" : 1,\n  \"timeStamp\" : 1541754304134,\n  \"userPassword\" : \"6001218a918da7598f55b0d77abdd8ae\",\n  \"iVersion\" : 1,\n  \"phoneNumber\" : \"13720426368\"\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "fc9a43d5-e6e5-4b15-b6e5-c847d39db6c3"
    }

response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)

print(response.text)