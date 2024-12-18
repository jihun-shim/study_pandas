# 1.몽고DB 데이터를 불러오기 {'구분' : '변경후'}
# 2.결측치를 채운다. 사용하고자 하는 값 
# 스마트폰.1 스마트폰.1 에 없는 값을 스마트폰 에서 가져와 채운다 
# if 스마트폰.1 == NaN : return 스마트폰 완성되면 CSV 파일로 만들어 다시저장


from pymongo import MongoClient

client = MongoClient('mongodb://python_jupyternote_mongo-mongodb-1:27017')
db_name = client['pandas_db']

missing_value = db_name['stock_list']

find_data = missing_value.find(
                                {'구분':'변경후'}
                                )


print(find_data)


