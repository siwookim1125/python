import pandas as pd

sc = pd.read_excel("pracsc.xlsx", sheet_name="Sheet1", engine="openpyxl")

# 특정 조건의 데이터를 엑셀로 내보내기.
# with pd.ExcelWriter("파일경로/파일명.xlsx") as writer:
#      temp1.to_excel(writer, index=True (데이터프레임의 인덱스 출력 여부 설정), sheet_name='시트이름')
#example
# with pd.ExcelWriter("output.xlsx") as writer:
#     temp1.to_excel(writer, index=True, sheet_name='test1')
#     temp2.to_excel(writer, index=False, sheet_name='test2')
# 출처: https://traumees.tistory.com/39 [트라움트리:티스토리]

#3d작업구분 별로 시트 내보내기
dlist = ["모델링", "사진촬영", "스캐닝"]

with pd.ExcelWriter("prac1.xlsx") as writer:
    for d in dlist :
        newData = sc["3D작업구분"].str.contains(d)
        print(sc[newData]) #데이터프레임[조건] 컬럼의 내용이, 조건에 맞는데이터만 데이터프레임으로 뽑아냄.
        print(d)
        sc[newData].to_excel(writer, index=False, sheet_name=d)






