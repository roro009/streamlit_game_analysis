#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# In[20]:

st.set_option('deprecation.showPyplotGlobalUse', False)
game_details = pd.read_csv("games_details.csv")

# In[27]:


subset_data = game_details.sample(n=500)  # Adjust the sample size based on your dataset size

def visualize_correlation():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='FG_PCT', y='PTS', data=subset_data, alpha=0.7)
    plt.title('Correlation between FG_PCT and PTS')
    plt.xlabel('Field Goal Percentage (FG_PCT)')
    plt.ylabel('Points Scored (PTS)')
    fig = plt.subplots()
    st.pyplot(fig)

def main():
    st.title("Game Analysis")
    st.header("What is the correlation between the field goal percentage (FG_PCT) and the points scored (PTS) by players?")

    st.header('Correlation Visualization')
    visualize_correlation()


    st.header('Subset of Data')
    st.dataframe(subset_data.head())

if __name__ == '__main__':
    main()

