import requests
import pymongo
from lxml import etree
# client = pymongo.MongoClient("localhost",27017)
# db = client["youxin"]
data=dict()
url = "https://sz.zu.anjuke.com/fangyuan/p{}/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
r = requests.get(url.format(1),headers=headers)
html = etree.HTML(r.text)
# print(html.xpath('//title'))
items = html.xpath('//div[@class="list-content"]/div')
print(r.status_code)
# print(items)
# print(r.text)
for i in items[2:-1]:
    data["title"]= i.xpath('div[1]/h3/a/@title')[0]
    data["url"] = i.xpath('div[1]/h3/a/@href')[0]
    data["location"] = i.xpath('div[1]/address/text()')[1].split()
    data["size"] = i.xpath('div[1]/p/text()')[0].strip()
    data["price"] = i.xpath('div[2]/p/strong/text()')[0]
    print(data)





# import pymongo
# class Mongo_Data():
#     def __init__(self,base_name,ip="localhost"):
#         self.client = pymongo.MongoClient(ip,27017)
#         self.db = self.client[base_name]
#     def get_all_coll_names(self):
#         coll_names = self.db.collection_names()
#         return coll_names
#
#     def get_collection(self,colle_name,db):
#         coll = db[colle_name]
#         return coll
#     def insert_data2coll(self,data,coll):
    #     coll.insert(data)
    # def remove_coll(self,coll,data,all=False):
    #     if all:
    #         coll.remove()
    #     else:
    #         coll.remove(data)
    # def update_coll(self,coll,old_data,new_data):
    #     coll.update(old_data,{"$set":new_data})
    # def find_one_docum(self,coll):
    #     one = coll.find_one()
    #     return one
    # def find_multi_docum(self,coll):
    #     all = coll.find()
    #     return all
    # def get_docum_num(self):
    #     num = self.find_multi_docum().count()
# if __name__ == '__main__':
#     fir  = Mongo_Data("BMWAMG")
#     coll = fir .get_collection("M5E63",fir.db)
#     fir.remove_coll(coll)

    # names = fir.get_all_coll_names()
    # print(names)






