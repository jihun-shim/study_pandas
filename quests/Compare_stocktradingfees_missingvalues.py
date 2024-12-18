# 1.몽고DB 데이터를 불러오기 {'구분' : '변경후'}
# 2.결측치를 채운다. 사용하고자 하는 값 
# 스마트폰.1 스마트폰.1 에 없는 값을 스마트폰 에서 가져와 채운다 
# if 스마트폰.1 == NaN : return 스마트폰 완성되면 CSV 파일로 만들어 다시저장


from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://python_jupyternote_mongo-mongodb-1:27017')
db_name = client['pandas_db']

missing_value = db_name['stock_list']

find_data = list(missing_value.find({'구분':'변경후'}))

find_data_first = pd.DataFrame(find_data)

#결측치 넣기
find_data_first['new스마트폰'] = find_data_first['스마트폰.1'].fillna(find_data_first['스마트폰'])

#NaN 제거
find_data_first = find_data_first.dropna(subset=['new스마트폰'])
pass

def add_elements_df(data_bundle):
    result = data_bundle['HTS']+data_bundle['new스마트폰']
    return result
    pass

find_data_first['HTS+new스마트폰'] = find_data_first.apply(add_elements_df, axis=1)
pass

find_data_first = find_data_first.dropna(subset=['HTS+new스마트폰'])
pass

find_data_first_mean = find_data_first['HTS+new스마트폰'].mean()
pass

filter_data = find_data_first[find_data_first['HTS+new스마트폰']>find_data_first_mean]
pass

import os
current_directory = os.getcwd()
output_path = os.path.join(current_directory, "datasets", "Compare_stocktradingfees_missingvalues.csv")
filter_data.to_csv(output_path)