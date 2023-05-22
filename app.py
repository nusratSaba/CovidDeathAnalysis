import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium 

st.title('Covid Death Data Analysis')

tab1, tab2, tab3 = st.tabs(["Dataset Overview", "Dataset Visualizations", "Location"])

covid_dataset = pd.read_csv("./data/dataset.csv")
row_num = covid_dataset.shape[0]
col_num = covid_dataset.shape[1]
TProState_null = covid_dataset['Province_State'].isna().sum()
nullValues_deathCol = covid_dataset['Deaths'].isna().sum()
nullValues_ConfirmedCol = covid_dataset['Confirmed'].isna().sum()

covid_dataset['Deaths'] = covid_dataset['Deaths'].fillna(0.0)
covid_dataset['Confirmed'] = covid_dataset['Confirmed'].fillna(0.0)


with tab1:
	st.header("Data Overview")
	st.write(covid_dataset.head(5))
	st.write('Total Row Number :', row_num)
	st.write('Total Column Number :', col_num)
	st.write('Total **Province_State** null rows :', TProState_null)
	st.write('Total **Deaths** null rows :', nullValues_deathCol)
	st.write('Total **Confirmed** null rows :', nullValues_ConfirmedCol)


with tab2:
	st.header("Visualizations")

	st.caption('Line Chart')
	# line_x = list(covid_dataset['Deaths'])
	# line_y = list(covid_dataset['Confirmed'])
	# plt.plot(line_x, line_y)
	# plt.xlabel('Deaths')
	# plt.ylabel('Confirmed')

	# st.plt.show()

	st.caption('Histogram')
	st.caption('Scatterplot')


with tab3:
	st.header("Location")
	m = folium.Map()





