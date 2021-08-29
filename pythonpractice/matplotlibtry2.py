# 1일차
# https://wikidocs.net/92083 필요한 한국어 자료는 여기 다 있다고 보면 될 거 같ㄷ.ㅏ
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4],[1, 2, 3, 4])
plt.show()
#----------------------------------------------------------------------
data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [2, 3, 5, 10, 8]}
plt.plot('data_x', 'data_y', data=data_dict)
plt.show()
#----------------------------------------------------------------------
#json파일 가져오기. 
path = r'D:\정부발주사업정보.json'
raw_df = pd.read_json(path)
raw_df.iloc[0]
column_names = '회계년도 소관명 회계명 계정명 분야명 부문명 프로그램명 단위사업명 세부사업명 비용성격 국회확정액(백만원)'
raw_df.columns = [column_names.split()]
raw_df.drop([0], axis=0, inplace=True)
#----------------------------------------------------------------------
#축에 이름(label)붙여주기
#xlabel(축이름, 축이름과 그래프박스의 간격(labelpad), 축이름의 위치(loc), 축이름의 폰트(fontdict))
plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel("x Axis")
plt.ylabel("y Axis")
plt.show()
#----------------------------------------------------------------------
#그래프의 범례(legend)표시
#legend(범례위치 좌표로 표시된다.(loc), 범례텍스트상자테두리(frameon), 텍스트상자테두리그림자(shadow), 폰트사이즈(fontsize), 텍스트 표시될 열(ncol))함수. plot할 때 label을 써 넣는데, 이 label이 범례가 된다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()
#----------------------------------------------------------------------
#축의 범위지정
#xlim([xmin, xmax]) 혹은 axis([xmin, xmax, ymin, ymax])
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.xlim([0, 5])      # X축의 범위: [xmin, xmax]
plt.ylim([0, 20])     # Y축의 범위: [ymin, ymax]

plt.show()
#----------------------------------------------------------------------
#다양한 마커들
#plot의 매개변수 marker를 통해 지정하든지, 그냥 'bo'이런 식으로 하든지.. 너무 많아서 그냥 검색 ㄱ
plt.plot([4, 5, 6], marker="H")
plt.plot([3, 4, 5], marker="d")
plt.plot([2, 3, 4], marker="x")
plt.plot([1, 2, 3], marker=11)
plt.plot([0, 1, 2], marker='$Z$')
plt.show()
#----------------------------------------------------------------------
#색상 지정
#plot(color)를 통해.
plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], color='limegreen')
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], color='violet')
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], color='dodgerblue')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
#----------------------------------------------------------------------
#마커, 색상지정, 선 스타일 지정의 집합체
#plot(color, marker, linestyle)로 한다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], color='#e35f62',
         marker='o', linestyle='--')
#----------------------------------------------------------------------
#그래프 영역 채우기
#fill_between(x[시작점:끝점], y[시작점:끝점], 투명도(alpha)) x축 방향으로 영역이 채워진다.
#두 그래프 사이의 영역은 fill_between(x[1:3], y1[1:3], y2[1:3], color='lightgray', alpha=0.5)
x = [1, 2, 3, 4]
y = [2, 3, 5, 10]

plt.plot(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_between(x[1:3], y[1:3], alpha=0.5)

plt.show()
#----------------------------------------------------------------------
#그리드 설정하기
#gird(True, 축(axis)설정)
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)
plt.grid(True, axis='y')

plt.show()
#----------------------------------------------------------------------
#눈금 이름(label)지정하기
#xticks(눈금의 개수(list나 array), 이름(label리스트))
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.xticks(np.arange(0, 2, 0.2), labels=['Jan', '', 'Feb', '', 'Mar', '', 'May', '', 'June', '', 'July'])
plt.yticks(np.arange(0, 7), ('0', '1GB', '2GB', '3GB', '4GB', '5GB', '6GB'))

plt.show()
#----------------------------------------------------------------------
#수평선 표시하기
#axhline(y값, xmin, xmax, 수평선color, 기타등등), hlines도 마찬가지
x = np.arange(0, 4, 0.5)

plt.plot(x, x + 1, 'bo')
plt.plot(x, x**2 - 4, 'g--')
plt.plot(x, -2*x + 3, 'r:')

plt.axhline(4.0, 0.1, 0.9, color='lightgray', linestyle='--', linewidth=2)
plt.hlines(-0.62, 1.0, 2.5, color='gray', linestyle='solid', linewidth=3)

plt.show()
#----------------------------------------------------------------------
#수직선 표시하기
#axvline(x값, ymin, ymax, 수평선color, 기타등등)
x = np.arange(0, 4, 0.5)

plt.plot(x, x + 1, 'bo')
plt.plot(x, x**2 - 4, 'g--')
plt.plot(x, -2*x + 3, 'r:')

plt.axvline(1.0, 0.2, 0.8, color='lightgray', linestyle='--', linewidth=2)
plt.vlines(1.8, -3.0, 2.0, color='gray', linestyle='solid', linewidth=3)

plt.show()