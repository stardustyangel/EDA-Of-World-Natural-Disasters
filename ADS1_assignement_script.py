#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 10:25:33 2023

@author: tayssirboukrouba
"""
# importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# defining the functions


def lineplot(data, x_col, y_col, title, x_title, y_title):
    '''
    Creates a line plot of y column values over x column

            Parameters:
                   data (DataFrame): dataframe containing the columns
                   x_col (String): column name  on x axis
                   y_col(String): column name on y axis
                   title (String) : title of the plot
                   x_title (String) : label on x axis
                   y_title (String) : label on y axis

            Returns:
                    None
    '''
    # looping over categorical values of y_col
    for value in data[y_col].unique():
        # grouping x_col values by y_col
        y = data[data[y_col] == value].groupby(x_col)[y_col].count()
        # assigning the x_axis to the index of y_values
        x = y.index
        # removing white space
        plt.xlim(data[x_col].min(), data[x_col].max())
        # plotting
        plt.plot(x, y)
        # labelling
        plt.xlabel(x_title)
        plt.ylabel(y_title)
        plt.title(title)
        # adding a legend
        plt.legend(data[y_col].unique())
        # save as png
        plt.savefig("lineplot.png")

    return


def pieplot(data, column, title):
    '''
    Creates a pie plot of a selected column

            Parameters:
                   data (Dataframe): dataframe containing the column
                   column (String): column name  on x axis
                   title (String) : title of the plot

            Returns:
                    None
    '''
    # defining the figure size
    plt.figure(figsize=(8, 8))
    # defining the categorical variable
    x = data[column].value_counts()
    # defining the labels
    labels = x.index
    # plotting
    plt.pie(x, radius=1, labeldistance=0.5, autopct='%.1f%%')
    # adding a legend
    plt.legend(labels, loc='lower left')
    # save as png
    plt.title(title)
    # save as png
    plt.savefig("pieplot.png")
    return


def barchart(data, x, y, x_title, y_title, title):
    '''
    Creates a bar chart of frequencies of a selected column

            Parameters:
                   data (Dataframe): dataframe containing the columns
                   x (String): column name  on x axis
                   y (List) : list of columns on y axis
                   title (String) : title of the plot
                   x_title (String) : label on x axis
                   y_title (String) : label on y axis


            Returns:
                    None
    '''
    plt.figure()
    # getting the sum of y cols values grouped by the x column
    x = data.groupby(x)[y].sum()
    # getting the top 5
    top_5_x = x.sort_values(ascending=False, by=y)[:5]
    # create spacing between x_axis values (avoid stacking)
    x_axis = np.arange(len(top_5_x.index))
    # plotting :
    # bar chart of first col
    plt.bar(x_axis+0.1, width=0.4, height=top_5_x.iloc[:, 0])
    # bar chart of second col
    plt.bar(x_axis+0.4, width=0.4, height=top_5_x.iloc[:, 1])
    # labelling
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(title)
    # adding legend
    plt.legend(labels=y)
    # changing lables on the x axis
    plt.xticks(x_axis, top_5_x.index)
    # save as png
    plt.savefig("barchart.png")
    return


# reading the csv file as a pandas dataframe
df = pd.read_csv('1970-2021_DISASTERS.csv')

# calling the lineplot() function with the defined arguments
lineplot(data=df, x_col='Year', y_col='Continent',
         title='Evolution of Natural Disasters Between Continents(1970-2021)',
         x_title='Years', y_title='Frequency (Count)')

# calling the pieplot() function with the defined arguments
pieplot(data=df, column='Disaster Subgroup',
        title='Pie Plot of The Disaster Subgroups Proportions')

# calling the barchart() function with the defined arguments
barchart(data=df, x='ISO', y=['Total Deaths', "No Injured"],
         title='Top 5 Countries with most Total Deaths/Injuries (1970-2021)',
         x_title='Countries', y_title='Casulties (in millions)')
