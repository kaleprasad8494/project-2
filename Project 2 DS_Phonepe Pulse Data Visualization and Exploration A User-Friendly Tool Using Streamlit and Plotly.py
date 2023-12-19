# import streamlit as st
# import pandas as pd
# import plotly.express as px
#
# # Load data from PhonePe Pulse
# data = pd.read_csv('phonepe_pulse_data.csv')
#
#
# # Streamlit app
# def main():
#     st.title('DS_PhonePe Pulse Data Visualization and Exploration')
#
#     # Data Exploration
#     st.header('Data Exploration')
#     explore_data()
#
#     # Data Visualization
#     st.header('Data Visualization')
#     visualize_data()
#
#
# def explore_data():
#     # Display raw data
#     st.subheader('Raw Data')
#     st.dataframe(data)
#
#     # Filter data
#     st.subheader('Data Filters')
#     category = st.selectbox('Select a Category', data['category'].unique())
#     filtered_data = data[data['category'] == category]
#     st.dataframe(filtered_data)
#
#
# def visualize_data():
#     # Group data by category and calculate total count
#     category_counts = data.groupby('category').size().reset_index(name='count')
#
#     # Plot bar chart
#     st.subheader('Category Counts')
#     fig = px.bar(category_counts, x='category', y='count', color='category')
#     st.plotly_chart(fig)
#
#     # Plot line chart
#     st.subheader('Trend over Time')
#     fig = px.line(data, x='date', y='count', color='category', title='Category Trend over Time')
#     st.plotly_chart(fig)
#
#
# # Run the Streamlit app
# if __name__ == '__main__':
#     main()
