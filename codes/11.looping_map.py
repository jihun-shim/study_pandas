def add_elements(first, second=1):
    result = first + second
    return result

list_first = [1,2,3]
list_second = [4,5,6]

# with zip
# 1,4
# 2,5
# 3,6

# map 과 for 문의 유사 비슷한 점
# for 이해

result_list = list()

# 1.use one parameter 파라미터 한개사용
# for number_first in list_first:
#     result = add_elements(number_first)
#     result_list.append(result)
# result_list
# pass

# use two parameters 파라미터 두개사용
# for number_first, number_second in zip(list_first, list_second):
#     result = add_elements(number_first, number_second)
#     result_list.append(result)
# result_list
# pass

# 2.map() : callback function 맵 함수의사용

# one parameter
# result_map = map(add_elements, list_first)
# result_map_list = list(result_map)
# pass

# two parameter
# result_map = map(add_elements, list_first, list_second)
# result_map_list = list(result_map)
# pass

# 3.apply() with pandas 판다스에서 사용
data = {'col_first': list_first
        , 'col_second' : list_second}

import pandas as pd
df_first = pd.DataFrame(data)
pass

# one parameter 한개의 파라미터
# result_df = df_first['col_first'].apply(add_elements)
# pass

# over two parameter : dataFrame 두개이상 데이터 프레임으로 던져줄때
def add_elements_df(serise_bundle):
    result = serise_bundle['col_first'] + serise_bundle['col_second']
    return result
    pass

df_first['add_elements'] = df_first.apply(add_elements_df, axis=1)
pass

