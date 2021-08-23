# 그냥 코드만 옮겨놓은 것.

import pandas as pd
import bs4
import matplotlib.pyplot as plt

path = 'D:\정부발주사업정보.json'
raw_data = pd.read_json(path)
raw_data.columns = raw_data.loc[0]
raw_data = raw_data.drop(0)

istitutions_dict = raw_data['소관명'].value_counts().to_dict()

institution = list(istitutions_dict.keys())
num_of_insti = list(istitutions_dict.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(institution, num_of_insti, color ='maroon',
        width = 0.4)
 
plt.xlabel("기관이름들")
plt.ylabel("총 사업 수")
plt.title("기관별 사업 수주")
plt.show()