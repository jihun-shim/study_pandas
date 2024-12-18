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

def add_elements_df(data_row, data_col_one, data_col_two):
    # 결측치(NaN)가 있으면 data_col_one 값을 data_col_two 로 채우기
    if pd.notna(data_row[data_col_two]):
        return data_row[data_col_two]
    else:
        return data_row[data_col_one]

# 스마트폰 결측치 넣기
def add_elements_sp(data_row):
    return add_elements_df(data_row, '스마트폰', '스마트폰.1')

find_data_first['new_스마트폰'] = find_data_first.apply(add_elements_sp, axis=1)

# HTS 결측치 넣기
def add_elements_hts(data_row):
    return add_elements_df(data_row, 'HTS', 'HTS.1')

find_data_first['new_HTS'] = find_data_first.apply(add_elements_hts, axis=1)

# NaN값 제거
find_data_first = find_data_first.dropna(subset=['new_스마트폰','new_HTS'])

# 열 작성
def new_hts_스마트폰(data_row):
    return data_row['new_HTS'] + data_row['new_스마트폰']

find_data_first['new_HTS_스마트폰'] = find_data_first.apply(new_hts_스마트폰, axis=1)

# 평균 값 내기
find_data_first_mean = find_data_first['new_HTS_스마트폰'].mean()
pass

# 평균 이상인 데이터만 필터링
filter_data = find_data_first[find_data_first['new_HTS_스마트폰']>find_data_first_mean]

import os
current_directory = os.getcwd()
output_path = os.path.join(current_directory, "datasets", "Compare_stocktradingfees_missingvalues.csv")
filter_data.to_csv(output_path)

'''
부족한점
아직 혼자서 함수를 작성하지 못함 
특정부분이상 가면 어떻게 만들어야 할지 생각이 안남

결국
GPT 도움 받아 작성 
함수작성 하는 방법 등등 다시보고 연습하기...
'''