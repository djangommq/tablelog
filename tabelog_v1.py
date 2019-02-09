# -*- coding: utf-8 -*-
import csv
import datetime
import os
import random
import json

import requests
from bs4 import BeautifulSoup

import sys
from time import sleep

from mongodb_util import *

VERSION = COLLECTION

# 创建链接mongodb数据库对象那个
clientMongodb=dataToMongodb()

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)) , '../crawlerOutput/' + VERSION + '/tabelog/')
# file_path = os.path.join(os.path.dirname(__file__),'crawlerOutput/' ,VERSION , '/tabelog/')
web_name = 'tabelog/'
user_agerts = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
    "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"
]


def getInfo(url):
    saveLog('获取页面{}的数据'.format(url))
    header = {
        'Host': 'tabelog.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': random.choice(user_agerts),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'DNT': '1',
        'Referer': 'https://tabelog.com/tokyo/A1303/A130301/13199289/dtlratings/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh,zh-CN;q=0.9',
        'Cookie': '_ga=GA1.2.1950227645.1521457568; _gid=GA1.2.2087309422.1521457568; s_fid=75ECF5B293C35A58-0F6BFA53CB265A95; ma_k=a6cc9eeaec17a42e2893e8c31a01da24; do_i=4f9d1d14c7c22c73470d21637a6f6b8f; ta_l=1; s_nr=1521457694858; tabelogusr=Ndq5D4zAjPF_1521548378982; s_cc=true; _tabelog_session_id=4d14056ba65e86b5d575806132138ed5; mo_r=f5e28a3d89278e270f2a0bbcfe4c1a31; inbound-jpuse=1; jack_ad_disp_count=2; ysc=; detail_score_open=0; s_sq=%5B%5BB%5D%5D; s_ptc=0.004%5E%5E0.006%5E%5E0.000%5E%5E0.110%5E%5E0.065%5E%5E0.178%5E%5E16.276%5E%5E0.109%5E%5E16.598; s_royal=site%3A802-2579186%3A6%2Ctabelog%3A802-2579186%3A4',
    }
    with requests.get(url, headers=header) as res:
        return res


def saveLog(str=''):
    logFile = file_path + 'log/' + web_name + '{}_log.csv'.format(city_name)
    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logHead = ['ruandate', 'str']
    logData = {
        'ruandate': date_time,
        'str': str
    }
    print('{} \t {}'.format(date_time, str))
    logPath = os.path.split(logFile)
    isExists = os.path.exists(logPath[0])
    if not isExists:
        os.makedirs(logPath[0])
    with open(logFile, 'a', encoding='utf-8', newline='') as log_file:
        log_csv = csv.DictWriter(log_file, fieldnames=logHead)
        if not os.path.getsize(logFile):
            log_csv.writeheader()
        log_csv.writerow(logData)


def saveInfo(res):
    rawHead = [
        'shop_status',
        'Store Name',
        'TEL',
        'Postal Code',
        'Address',
        'Prefecture',
        'City / Ward Name',
        'Address',
        'Category',
        'Budget',
        # 'Budget (day)',
        'RatingCount',
        'Rating',
        'Transpotation',
        'Hours',
        'Holiday',
        '# of Seats',
        'ParkingLot',
        'Service',
        'Homepage',
        'SNS',
        'Open Date',
        'ID',
        'lat',
        'lng'
    ]

    rawData = {}
    infoList = [
        # '予約可否',
        '交通手段',
        '営業時間',
        '定休日',
        '予算（口コミ集計）',
        # '支払い方法',
        '席数',
        # '個室',
        # '貸切',
        '禁煙・喫煙',
        '駐車場',
        # '空間・設備',
        # '携帯電話',
        # '飲み放題コース',
        # 'コース',
        # 'ドリンク',
        # '料理',
        # '利用シーン',
        # 'ロケーション',
        'サービス',
        'ホームページ',
        # '公式アカウント',
        'オープン日',
    ]
    infoListEn = [
        # 'Reservationavailability',
        'Transpotation',
        'Hours',
        'Holiday',
        'Budget',
        # 'methodofpayment',
        '# of Seats',
        # 'PrivateRoom',
        # 'reserved',
        'SNS',
        'ParkingLot',
        # 'SpaceOrEquipment',
        # 'mobilephone',
        # 'Allyoucandrinkcourse',
        # 'course',
        # 'drink',
        # 'cuisine',
        # 'Usescene',
        # 'Location',
        'Service',
        'Homepage',
        # 'Officialaccount',
        'Open Date',
    ]
    soup = BeautifulSoup(res.content, "lxml")
    # 餐馆状态：正常，休息，搬迁
    status_soup = soup.find('div', attrs={'class': 'rdheader-rstname-wrap'}).find('span', recursive=False)
    print(status_soup)
    if status_soup:
        status = status_soup['class'][-1]
        print(status)
        rawData['shop_status'] = status
    else:
        rawData['shop_status'] = ''
    jsonStr = soup.find('script', attrs={'type': 'application/ld+json'})
    try:
        jsonStr = str(jsonStr.contents[0])
    except Exception as e:
        jsonStr = ''
    jsonArr = json.loads(jsonStr)

    rawData['ID'] = res.url.split("/")[-1]
    rawData['Store Name'] = jsonArr.get('name', "")
    rawData['Category'] = jsonArr.get('servesCuisine', "")
    # rawData['image'] = jsonArr.get('image', "")
    # rawData['addressCountry'] = jsonArr.get('address', {}).get('addressCountry', "")
    rawData['Postal Code'] = jsonArr.get('address', {}).get('postalCode', "")
    rawData['Prefecture'] = jsonArr.get('address', {}).get('addressRegion', "")
    rawData['City / Ward Name'] = jsonArr.get('address', {}).get('addressLocality', "")
    rawData['Address'] = jsonArr.get('address', {}).get('streetAddress', "")
    rawData['lat'] = jsonArr.get('geo', {}).get('latitude', "")
    rawData['lng'] = jsonArr.get('geo', {}).get('longitude', "")
    rawData['TEL'] = jsonArr.get('telephone', "")
    # rawData['priceRange'] = jsonArr.get('priceRange', "")
    rawData['RatingCount'] = jsonArr.get('aggregateRating', {}).get('ratingCount', "")
    rawData['Rating'] = jsonArr.get('aggregateRating', {}).get('ratingValue', "")
    tables = soup.find_all('table', class_='c-table c-table--form rstinfo-table__table')
    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            column = tr.find('th').stripped_strings
            column = [x for x in column]
            column = ''.join(column)
            if column and column in infoList:
                index = infoList.index(column)
                try:
                    columnName = infoListEn[index]
                except IndexError:
                    print(index)
                values = tr.find('td').strings
                value = [x.strip() for x in values]
                value = ' '.join(value).strip()
                rawData[columnName] = value
    rawPath = file_path + web_name
    isExists = os.path.exists(rawPath)
    if not isExists:
        os.makedirs(rawPath)
    rawFile = '{}{}_raw.csv'.format(rawPath, city_name)
    saveLog('保存店铺{}的数据'.format(rawData.get('Store Name')))
    # with open(rawFile, 'a', encoding='utf-8', newline='') as raw_file:
    #     # print(rawData)
    #     raw_csv = csv.DictWriter(raw_file, fieldnames=rawHead)
    #     if not os.path.getsize(rawFile):
    #         raw_csv.writeheader()
    #     raw_csv.writerow(rawData)

    # 将数据保存到mongodb数据库
    clientMongodb.insert_info(rawData,city_name)


def limit_detect(res):
    text = res.text
    if 'アクセスが制限されています' in text:
        return True
    else:
        return False


def save_success_id(id):
    file_path = './{}_has_get.txt'.format(city_name)
    with open(file_path, 'a') as f:
        f.writelines(str(id)+'\n')


def last_success_id():
    file_path = './{}_has_get.txt'.format(city_name)
    try:
        with open(file_path, 'r') as f:
            s = f.readlines()[-1]
            return int(s)
    except:
        return 0


if __name__ == '__main__':
    # Osaka         27000001, 27105562
    # hyogo         28000001, 28052175
    # Kyoto         26000001, 26030906
    # aichi         23000001, 23067905    共48,845店舗
    # fukuoka       40000001, 40049040    共35,109店舗
    # Kanagawa      14000001, 14072039
    # Tokyo         13000001, 13223273
    # chiba         12000001, 12044580    共31,599店舗
    # Saitama       11000001, 11047653    共34,853店舗

    area_data = {
        "11": {
            'id': 11,
            'name': "Saitama",
            'first_id': 11000001,
            'last_id': 11048000,
        },
        "12": {
            'id': 12,
            'name': "chiba",
            'first_id': 12000001,
            'last_id': 12044900,
        },
        "13": {
            'id': 13,
            'name': "Tokyo",
            'first_id': 13000001,
            'last_id': 13224700,
        },
        "14": {
            'id': 14,
            'name': "Kanagawa",
            'first_id': 14000001,
            'last_id': 14072450,
        },
        "23": {
            'id': 23,
            'name': "aichi",
            'first_id': 23000001,
            'last_id': 23068250,
        },
        "26": {
            'id': 26,
            'name': "Kyoto",
            'first_id': 26000001,
            'last_id': 26031050,
        },
        "27": {
            'id': 27,
            'name': "Osaka",
            'first_id': 27000001,
            'last_id': 27106150,
        },
        "28": {
            'id': 28,
            'name': "hyogo",
            'first_id': 28000001,
            'last_id': 28052450,
        },
        "40": {
            'id': 40,
            'name': "fukuoka",
            'first_id': 40000001,
            'last_id': 40049300,
        },
    }
    if len(sys.argv) == 2:
        index = int(sys.argv[1])
    else:
        index = 0

    for area in area_data.values():
        if index == 0:
            print('默认获取全部城市的数据')
            pass
        else:
            if area.get('id') != index:
                continue
        city_name = area.get('name')
        first_id = area.get('first_id')
        last_id = area.get('last_id')
        tmp_id = last_success_id()
        if tmp_id == 0:
            start_id = first_id
            end_id = last_id
        elif tmp_id >= last_id:
            print('本地区请求结束.')
            saveLog('本地区请求结束.')
            continue
        else:
            start_id = tmp_id + 1
            end_id = last_id
        for id in range(start_id, end_id):
            url = "https://tabelog.com/kyoto/A2601/A260201/" + str(id)
            try:
                res = getInfo(url)
                # sleep(random.randint(0, 2))
                if limit_detect(res):
                    saveLog('网络ip被限制, 无法继续')
                    break
                if res.status_code == 200:
                    saveLog('{}, 正常返回'.format(res.status_code))
                    save_success_id(id)
                saveInfo(res)
            except Exception as err:
                saveLog('页面{}出错'.format(url))
                saveLog(err)

    # 数据存储完毕, 关闭数据库链接
    clientMongodb.close_client()
