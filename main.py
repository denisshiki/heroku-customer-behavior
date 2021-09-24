import pandas as pd
import streamlit as st
import ipywidgets as widgets
import plotly.express as px

url = 'kmeans_data.csv'

st.set_page_config(layout="wide")

st.title('🔎Exploratory Analysis')
st.write('This page is to analyse the result data that was built in the link below:') 
st.markdown('[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/denisshiki/Customer-Analysis)')
st.write('If you have any doubts, you can contact me on LinkedIn 😄') 
st.markdown('[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/denis-shiki-1239901b6/)')

@st.cache(allow_output_mutation = True)
def get_data(url):
	data = pd.read_csv(url)
	return data

def barplot_category(data):

	df =get_data(url)
	st.title('Barplot')

	st.subheader('Select an attribute for the Barplot:')

	att_select = st.selectbox("Barplot", df.columns)
	fig = px.bar(df, x=att_select, color_discrete_sequence= px.colors.sequential.Rainbow, color = 'Clusters')
	st.plotly_chart(fig, use_container_width = True)

def boxplot_category(data):

	df = get_data(url)

	st.title('Boxplot')
	st.subheader('Select an x attribute for the boxplot:')
	att_select_x = st.selectbox('Boxplot x', df.columns)

	st.subheader('Select an y attribute for the boxplot:')
	att_select_y = st.selectbox('Boxplot y', df.columns)

	fig = px.box(df, x = att_select_x, y= att_select_y, color = 'Clusters')
	st.plotly_chart(fig, use_container_width = True)

def scatter_category(data):
	df = get_data(url)

	st.title('Scatterplot')
	st.subheader('Select an x attribute for the scatterplot:')
	att_select_x = st.selectbox('Scatter x', df.columns)

	st.subheader('Select an y attribute for the scatterplot:')
	att_select_y = st.selectbox('Scatter y', df.columns)

	fig = px.scatter(df, x = att_select_x, y= att_select_y, color = 'Clusters')
	st.plotly_chart(fig, use_container_width = True)


if __name__ == '__main__':

	url = 'kmeans_data.csv'

	data = get_data(url)

	barplot_category(data)

	boxplot_category(data)

	scatter_category(data)