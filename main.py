import streamlit
import pandas as pd
import numpy as np

st.title('테스트')

temp = pd.DataFrame([(1,2), (3, 4)], column = ['test1', 'test2'])

st.dataframe(temp)

temp.to_csv('temp.csv')
