#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_csv("C:/Users/Kosmo_05/Desktop/python/data/gapminder.tsv", sep="\t")


# In[5]:


print(df)


# In[6]:


print(type(df))


# In[7]:


print(df.shape)


# In[8]:


print(df.dtypes)


# In[10]:


countries = df['country']


# In[14]:


print(countries.head())


# In[12]:


print(df.loc[3])


# In[13]:


print(df.iloc[3])


# In[17]:


subset = df[['country', 'continent', 'year']]


# In[18]:


print(subset.head())


# In[19]:


print(df.loc[df.shape[0] - 1])


# In[20]:


print(df.loc[df.shape[0] - 1]) # 마지막 행의 출력


# In[21]:


print(df.iloc[-1])  # 마지막 행의 출력


# In[22]:


print(df.tail(n=1)) # 마지막 행의 출력


# In[31]:


print(type(df.tail(n=1))) #단, tail로 얻어온 자료형은 DataFrame으로 Series 형식이 아님에 유의


# In[32]:


print(df.loc[[0, 99, 999]]) # 복수 개 행의 출력


# In[33]:


subset2 = df.loc[:, ['year', 'pop']]  # 슬라이싱 구문을 이용한 데이터 추출 # 전체 행 선택, year, pop 컬럼 선택


# In[34]:


print(subset2.head())


# In[35]:


subset3 = df.iloc[:, [2, 4, -1]] # 전체 행 데이터, 2, 4, -1(마지막) 컬럼 데이터 추출


# In[36]:


print(subset3.head()) 


# In[37]:


# range를 이용한 데이터의 추출
u3_range = range(4)
print(u3_range)
print(df.iloc[:, u3_range].head())


# In[38]:


# 짝수번째 컬럼만 출력
subset4 = df.iloc[:, range(0, df.shape[1], 2)]
print(subset4.head())


# In[39]:


# df를 연도별로 그룹화
grouped_year_df = df.groupby('year')
print(grouped_year_df.head())
print(type(grouped_year_df))


# In[40]:


# 그룹화한 데이터프레임의 산술 평균 구하기
print(grouped_year_df['lifeExp'].mean())


# In[41]:


# 데이터프레임에서 활용 가능한 기초 통계량들
print(grouped_year_df.describe())


# In[42]:


# 여러 컬럼의 산술 평균 구하기
print(grouped_year_df[['lifeExp', 'gdpPercap']].mean())


# In[43]:


# 그룹화된 데이터 개수(빈도) 세기
print(df.groupby('continent')['country'].nunique())


# In[45]:


# Matplotlib 임포트
import matplotlib.pyplot as plt


# In[46]:


life_expectancy = df.groupby('year')['lifeExp'].mean()
print(life_expectancy)


# In[47]:


import matplotlib.pyplot as plt
life_expectancy.plot()


# In[48]:


import pandas as pd
s = pd.Series(['홍길동', 28])
print(s)


# In[49]:


# 인덱스의 지정
s = pd.Series(['홍길동', 28],
index=['Name', 'Age'])
print(s)


# In[50]:


kor = [80, 75, 90, 100, 65] # 데이터 리스트 생성
kor_s = pd.Series(kor) # 시리즈 생성
kor_s.describe() # 통계 요약 메서드


# In[51]:


# 데이터 프레임의 생성
scores_df = pd.DataFrame({
"KOR": [80, 90, 75],
"ENG": [90, 80, 70],
"MATH": [80, 90, 85]},
index = ["홍길동", "김철수", "이영희"]
)
print(scores_df)


# In[52]:


# loc을 이용한 관측치의 확인
print(scores_df.loc['김철수'])
print(type(scores_df.loc['김철수']))
# 단일 관측치는 Series로 반환


# In[55]:


# 동적 컬럼의 추가
scores_df['TOTAL'] = scores_df['KOR'] + scores_df['ENG'] + scores_df['MATH']
scores_df['AVERAGE'] = scores_df['TOTAL']/3
print(scores_df)


# In[56]:


# 불린 추출
# 시리즈 내 값이 80 이상인지 확인
scores_df['AVERAGE'] > 80


# In[57]:


# 불린 추출
# 데이터 프레임 내에서 평균이 80 이상인 학생만 추출
filtered_df = scores_df[scores_df['AVERAGE'] >= 80]
print(filtered_df)


# In[61]:


# thieves.txt 파일로부터 데이터를 불러들여 DataFrame으로 변환
thieves_df = pd.read_csv("C:/Users/Kosmo_05/Desktop/python/data/thieves.txt", sep="\t")
print(thieves_df)


# In[63]:


thieves_df2 = pd.read_csv("C:/Users/Kosmo_05/Desktop/python/data/thieves.txt",sep="\t", header=None)
print(thieves_df2)


# In[66]:


thieves_df3 = pd.read_csv("C:/Users/Kosmo_05/Desktop/python/data/thieves.txt",sep="\t", header=None, index_col=0)
print(thieves_df3)


# In[67]:


# 컬럼의 변경
thieves_df3.columns = ['Height', 'Weight']
print(thieves_df3)


# In[69]:


# 인덱스 이름을 바꿔 봅니다.
thieves_df3.index.name = "Name"
print(thieves_df3)


# In[71]:


# 데이터 프레임을 csv로 저장
thieves_df3.to_csv("C:/Users/Kosmo_05/Desktop/python/data/thieves.csv", encoding="MS949")


# In[72]:


# 결측치
from numpy import nan, NaN, NAN


# In[73]:


exam_scores = pd.Series([90, 80, 120, nan, 95, 80, -10])
print(exam_scores)


# In[74]:


# 결측치의 확인
print(pd.isnull(exam_scores))


# In[75]:


# 결측 빈도 확인
import numpy as np
print("결측치 수:", np.count_nonzero(exam_scores.isnull()))


# In[76]:


# 결측 빈도 확인
num_rows = exam_scores.shape[0]
num_missing = num_rows - exam_scores.count()
print("결측치 수:", num_missing)


# In[77]:


# 이상치를 결측치로 변환
~exam_scores.isin(range(0, 101))
exam_scores[~exam_scores.isin(range(0, 101))] = nan
print(exam_scores)


# In[78]:


# 결측치를 중앙값으로 대체
med_score = exam_scores[exam_scores.notnull()].median()
print(med_score)
exam_scores[exam_scores.isnull()] = med_score
print("평균:", exam_scores.mean())


# In[ ]:




