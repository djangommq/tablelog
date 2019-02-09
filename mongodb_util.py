import pymongo
from config import MONGODB_SERVER,MONGODB_PORT,USER,PASSWORD

COLLECTION='20181224'

class dataToMongodb():
  def __init__(self):
    self.client=pymongo.MongoClient(MONGODB_SERVER,MONGODB_PORT)
    self.db=self.client['tabelog']
    self.db.authenticate(USER,PASSWORD)


  # 向mongodb数据库插入一条数据
  def insert_info(self,info_dict,cityname):
    collection = self.db[COLLECTION + cityname]
    if len(info_dict)==0:
      pass
    else:
      collection.insert_one(info_dict)


  # 获取mongodb表中所有的数据,并返回
  def get_allinfo(self,cityname):
      print(COLLECTION + cityname)
      collection = self.db[COLLECTION + cityname]
      result=collection.find()
      allinfo_list=[]
      # 去掉'_id'项并以列表的形式返回所有数据
      for res in result:
        res.pop('_id')
        allinfo_list.append(res)

      return allinfo_list

  # 关闭数据库连接
  def close_client(self):
      self.client.close()



# if __name__ == '__main__':
#     # dict={'name':'xiaoqiao','age':16}
#     dm=dataToMongodb()
#     # dm.insert_info(dict)
#     # print('完成')
#     print(dm.get_allinfo())