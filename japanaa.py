"""Importing libraries"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go

"""Reading data set"""
df = pd.read_csv(r"C:\Users\user\Desktop/japanese_universities.csv", index_col = 0)
df

"""info will view the columns and Data types"""
df.info()


"""describe will show the mean, median and mode of the data set"""
df.describe()


"""Getting the missing values of the dataset"""
missing_values = df.isnull().sum()
print(missing_values)

"""Knowing the correlation of all the  variables"""
numeric_columns = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_columns.corr()
correlation_matrix


"""heatmap of the japanese universities dataset"""
def heatmap():
    fig, ax = plt.subplots() 
    fig.set_size_inches(15,10)
    sns.heatmap(correlation_matrix, vmax =.8, square = True, annot = True,cmap='YlGn' )
    plt.title('Correlation Matrix',fontsize=15);
    return


"""calling the function"""
heatmap()


"""Bar plot of the japanese universities dataset"""
def barplot():
    fig1 = px.bar(df, x='state', color='type', title='University Types Across States',
             labels={'state': 'State', 'type': 'University Type'},
             category_orders={'type': ['National', 'Public', 'Private']})

    display(fig1)
    return


"""calling the function"""
barplot()


"""Histogram of distribution of variables"""
def histplot():
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 8))


    axes[0, 0].set_title("Distribution of department_count")
    sns.histplot(data=df, x="department_count", ax=axes[0, 0], kde=True)


    axes[0, 1].set_title("Distribution of Faculty count")
    sns.histplot(data=df, x="faculty_count", ax=axes[0, 1], kde=True)


    axes[1, 0].set_title("Distribution of review count")
    sns.histplot(data=df, x="review_count", ax=axes[1, 0], kde=True)


    axes[1, 1].set_title("Distribution of review rating")
    sns.histplot(data=df, x="review_rating", ax=axes[1, 1], kde=True)
    plt.tight_layout()
    plt.show()
    return


"""calling the function"""
histplot()





"""line graph of Japanese universisties dataset"""

def line():
    df['found'] = pd.to_datetime(df['found'])

    # Create a new column for decades
    df['decade'] = (df['found'].dt.year // 10) * 10

    # Group by decade and count the number of universities
    df_decade = df.groupby('decade').size().reset_index(name='count')


    fig = px.line(df_decade, x='decade', y='count', markers=True,
              title='University Growth Over Decades',
              labels={'decade': 'Decade', 'count': 'Number of Universities'})
    fig.show()
    return


"""calling the function"""
line()




"""boxplot of faculty count,departmentcount and university types"""
def boxplot():
    plt.figure(figsize=(14, 6))

    # Faculties
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df, x='type', y='faculty_count', palette='viridis')
    plt.title('Diversity of Universities in Terms of Faculties')
    plt.xlabel('University Type')
    plt.ylabel('Number of Faculties')

    # Departments
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='type', y='department_count', palette='viridis')
    plt.title('Diversity of Universities in Terms of Departments')
    plt.xlabel('University Type')
    plt.ylabel('Number of Departments')

    plt.tight_layout()
    plt.show()
    return

"""calling the function"""
boxplot()




