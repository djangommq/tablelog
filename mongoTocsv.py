import os
import csv
from mongodb_util import *
from tabelog_v1 import file_path

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

# 创建数据库链接对象
export_col=dataToMongodb()


def save_info():
   for c_name in city_name_list:
       info_list=export_col.get_allinfo(c_name)

       f_path=file_path+'tabelog/'
       if not os.path.exists(f_path):
         os.makedirs(f_path)

       filename=f_path+'{}.csv'.format(c_name)
       with open(filename,'a',encoding='utf-8',newline='')as f:
         writer=csv.DictWriter(f,fieldnames=rawHead)
         if not os.path.getsize(filename):
            writer.writeheader()
         for info in info_list:
           writer.writerow(info)


if __name__ == '__main__':
    city_name_list = ["Saitama", "chiba", "Tokyo", "Kanagawa", "aichi", "Kyoto", "Osaka", "hyogo", "fukuoka"]
    # city_name_list = ["Saitama"]
    save_info()
    print('成功导出csv文件')

    # 数据成功导出,关闭数据库链接
    export_col.close_client()