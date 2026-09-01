import pandas as pd
import numpy as np

# ==========================================================
# PANDAS TUTORIAL - FULL NOTES
# ==========================================================


# ----------------------------------------------------------
# Pandas HOME
# ----------------------------------------------------------
# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and
# manipulating data. "Pandas" = "Panel Data" / "Python Data Analysis"

# ----------------------------------------------------------
# Pandas Intro
# ----------------------------------------------------------
# Pandas allows us to analyze big data and make conclusions
# based on statistical theories. It can clean messy data sets,
# and make them readable and relevant.
print(pd.__version__)


# ----------------------------------------------------------
# Pandas Getting Started
# ----------------------------------------------------------
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)


# ----------------------------------------------------------
# Pandas Series
# ----------------------------------------------------------
a = [1, 7, 2]
myseries = pd.Series(a)   # a Series is like a labeled column
print(myseries)
print(myseries[0])   # access by default index

myseries2 = pd.Series(a, index=["x", "y", "z"])   # custom labels
print(myseries2)
print(myseries2["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myseries3 = pd.Series(calories)   # create Series from dict
print(myseries3)

myseries4 = pd.Series(calories, index=["day1", "day2"])  # select items
print(myseries4)


# ----------------------------------------------------------
# Pandas DataFrames
# ----------------------------------------------------------
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

print(df.loc[0])       # return row as a Series (locate by label)
print(df.loc[[0, 1]])  # return rows 0 and 1

df2 = pd.DataFrame(data, index=["day1", "day2", "day3"])  # named indexes
print(df2)
print(df2.loc["day2"])   # locate named index


# ----------------------------------------------------------
# Pandas Read CSV
# ----------------------------------------------------------
# create a sample csv file first for demonstration
csv_data = """calories,duration
420,50
380,40
390,45
"""
with open("data.csv", "w") as f:
    f.write(csv_data)

df = pd.read_csv('data.csv')
print(df)
print(df.to_string())   # print the ENTIRE DataFrame

pd.set_option('display.max_rows', 100)  # change max rows shown
print(pd.options.display.max_rows)


# ----------------------------------------------------------
# Pandas Read JSON
# ----------------------------------------------------------
json_data = {
    "Duration": {"0": 60, "1": 60, "2": 60},
    "Pulse": {"0": 110, "1": 117, "2": 103},
    "Calories": {"0": 409, "1": 479, "2": 340}
}
import json
with open("data.json", "w") as f:
    json.dump(json_data, f)

df = pd.read_json('data.json')
print(df.to_string())

# a Python dict can also be read directly as JSON
data = {
    "Duration": {"0": 60, "1": 60, "2": 60},
    "Pulse": {"0": 110, "1": 117, "2": 103}
}
df2 = pd.DataFrame(data)
print(df2)


# ----------------------------------------------------------
# Pandas Analyzing Data
# ----------------------------------------------------------
df = pd.read_csv('data.csv')
print(df.head(2))    # first 2 rows
print(df.tail(2))     # last 2 rows
print(df.info())       # information about the dataset
print(df.describe())    # statistical summary (mean, std, etc.)
print(df.shape)          # (rows, columns)
print(df.columns)         # column names


# ==========================================================
# CLEANING DATA
# ==========================================================

# ----------------------------------------------------------
# Cleaning Data
# ----------------------------------------------------------
# Data cleaning means fixing bad data in a data set:
# - Empty cells
# - Data in wrong format
# - Wrong data
# - Duplicates
messy_data = {
    'Name': ['Tom', 'Jack', None, 'Steve'],
    'Age': [25, np.nan, 35, 200],
    'Date': ['2020/12/01', '2020/12/02', 'not a date', '2020/12/04']
}
dirty_df = pd.DataFrame(messy_data)
print(dirty_df)


# ----------------------------------------------------------
# Cleaning Empty Cells
# ----------------------------------------------------------
new_df = dirty_df.dropna()   # remove rows with NULL/empty values
print(new_df)

new_df2 = dirty_df.dropna(subset=['Name'])  # only for a specific column
print(new_df2)

fill_df = dirty_df.copy()
fill_df.fillna(130, inplace=True)   # replace empty values with a value
print(fill_df)

fill_df2 = dirty_df.copy()
fill_df2["Age"].fillna(130, inplace=True)  # fill only one column
print(fill_df2)

mean_df = dirty_df.copy()
x = mean_df["Age"].mean()   # replace using mean
mean_df["Age"].fillna(x, inplace=True)
print(mean_df)

median_df = dirty_df.copy()
x = median_df["Age"].median()  # replace using median
median_df["Age"].fillna(x, inplace=True)
print(median_df)

mode_df = dirty_df.copy()
x = mode_df["Age"].mode()[0]   # replace using mode
mode_df["Age"].fillna(x, inplace=True)
print(mode_df)


# ----------------------------------------------------------
# Cleaning Wrong Format
# ----------------------------------------------------------
format_data = {
    'Date': ['2020/12/01', '2020/12/02', 'not a date', '2020/12/04']
}
fdf = pd.DataFrame(format_data)
fdf['Date'] = pd.to_datetime(fdf['Date'], errors='coerce')  # convert to date
print(fdf)
fdf.dropna(subset=['Date'], inplace=True)   # remove rows with bad dates
print(fdf)


# ----------------------------------------------------------
# Cleaning Wrong Data
# ----------------------------------------------------------
wrong_data = {'Age': [25, 30, 200, 28]}   # 200 is unrealistic wrong data
wdf = pd.DataFrame(wrong_data)

wdf.loc[2, 'Age'] = 30   # set a specific value to correct the wrong data
print(wdf)

wrong_data2 = {'Age': [25, 30, 200, 28]}
wdf2 = pd.DataFrame(wrong_data2)
for x in wdf2.index:
    if wdf2.loc[x, "Age"] > 120:   # loop through and replace by condition
        wdf2.loc[x, "Age"] = 120
print(wdf2)

wrong_data3 = {'Age': [25, 30, 200, 28]}
wdf3 = pd.DataFrame(wrong_data3)
for x in wdf3.index:
    if wdf3.loc[x, "Age"] > 120:   # or simply drop the row
        wdf3.drop(x, inplace=True)
print(wdf3)


# ----------------------------------------------------------
# Removing Duplicates
# ----------------------------------------------------------
dup_data = {
    'Name': ['Tom', 'Tom', 'Jack', 'Steve'],
    'Age': [25, 25, 30, 28]
}
ddf = pd.DataFrame(dup_data)
print(ddf.duplicated())   # returns True for duplicate rows

ddf.drop_duplicates(inplace=True)   # remove duplicate rows
print(ddf)


# ==========================================================
# CORRELATIONS
# ==========================================================

# ----------------------------------------------------------
# Pandas Correlations
# ----------------------------------------------------------
corr_data = {
    'Duration': [60, 60, 60, 45, 45, 60, 60],
    'Pulse': [110, 117, 103, 109, 117, 102, 110],
    'Calories': [409, 479, 340, 282, 405, 300, 400]
}
cdf = pd.DataFrame(corr_data)
print(cdf.corr())
# Result table shows relationship between every column pair.
# Values range from -1 to 1:
# 1   = perfect positive correlation
# 0   = no correlation
# -1  = perfect negative correlation


# ==========================================================
# PLOTTING
# ==========================================================

# ----------------------------------------------------------
# Pandas Plotting
# ----------------------------------------------------------
import matplotlib.pyplot as plt

plot_data = {
    'Duration': [60, 60, 60, 45, 45, 60, 60, 450, 30, 60],
    'Pulse': [110, 117, 103, 109, 117, 102, 110, 104, 109, 98],
    'Calories': [409, 479, 340, 282, 405, 300, 400, 1500, 280, 250]
}
pdf = pd.DataFrame(plot_data)

pdf.plot()   # basic plot of all columns
plt.show()

pdf.plot(kind='scatter', x='Duration', y='Calories')  # scatter plot
plt.show()

pdf["Duration"].plot(kind='hist')   # histogram
plt.show()

pdf.plot(kind='bar')   # bar plot
plt.show()


# ==========================================================
# PANDAS DATAFRAME - ALL PROPERTIES & METHODS REFERENCE
# ==========================================================
# Sample DataFrames used throughout this reference section
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': ['x', 'y', 'x', 'z', 'y']
})
df2 = pd.DataFrame({
    'A': [1, 2, 6],
    'D': [100, 200, 300]
})

# abs() - Return a DataFrame with the absolute value of each value
print(pd.DataFrame({'A': [-1, -2, 3]}).abs())

# add() - Adds the values of a DataFrame with the specified value(s)
print(df['A'].add(10))

# add_prefix() - Prefix all labels
print(df.add_prefix('col_'))

# add_suffix() - Suffix all labels
print(df.add_suffix('_col'))

# agg() / aggregate() - Apply a function or function name to an axis
print(df[['A', 'B']].agg('sum'))
print(df[['A', 'B']].aggregate(['sum', 'mean']))

# align() - Aligns two DataFrames with a specified join method
a1, a2 = df.align(df2, join='outer', axis=0)
print(a1, a2)

# all() - Return True if all values in the DataFrame are True
print(df[['A', 'B']].all())

# any() - Returns True if any of the values in the DataFrame are True
print(df[['A', 'B']].any())

# append() (deprecated in new pandas, use pd.concat) - append new rows
df_appended = pd.concat([df, pd.DataFrame({'A': [6], 'B': [60], 'C': ['w']})], ignore_index=True)
print(df_appended)

# applymap() - Execute a function for each element in the DataFrame
print(df[['A', 'B']].applymap(lambda x: x * 2))

# apply() - Apply a function to one axis of the DataFrame
print(df[['A', 'B']].apply(np.sum))

# assign() - Assign new columns
print(df.assign(D=df['A'] + df['B']))

# astype() - Convert the DataFrame into a specified dtype
print(df['A'].astype(float))

# at - Get or set the value of the item with the specified label
print(df.at[0, 'A'])
df.at[0, 'A'] = 1
print(df)

# axes - Returns the labels of the rows and the columns
print(df.axes)

# bfill() - Replaces NULL values with the value from the next row
nadf = pd.DataFrame({'A': [1, np.nan, 3]})
print(nadf.bfill())

# bool() - Returns the Boolean value of a single-element DataFrame
print(pd.DataFrame([[True]]).bool())

# columns - Returns the column labels of the DataFrame
print(df.columns)

# combine() - Compare two DataFrames, let a function decide which values to keep
print(df[['A']].combine(df2[['A']], np.minimum))

# combine_first() - Fill NULLs in first DataFrame with values from second
print(nadf.combine_first(pd.DataFrame({'A': [9, 9, 9]})))

# compare() - Compare two DataFrames and return the differences
df_a = pd.DataFrame({'A': [1, 2, 3]})
df_b = pd.DataFrame({'A': [1, 5, 3]})
print(df_a.compare(df_b))

# convert_dtypes() - Converts the columns into new/best possible dtypes
print(df.convert_dtypes().dtypes)

# corr() - Find the correlation between each column
print(df[['A', 'B']].corr())

# count() - Returns the number of not empty cells for each column/row
print(df.count())

# cov() - Find the covariance of the columns
print(df[['A', 'B']].cov())

# copy() - Returns a copy of the DataFrame
df_copy = df.copy()
print(df_copy)

# cummax() - Calculate the cumulative maximum values
print(df['A'].cummax())

# cummin() - Calculate the cumulative minimum values
print(df['A'].cummin())

# cumprod() - Calculate the cumulative product
print(df['A'].cumprod())

# cumsum() - Calculate the cumulative sum
print(df['A'].cumsum())

# describe() - Returns a description summary for each column
print(df.describe())

# diff() - Difference between a value and the previous row's value
print(df['A'].diff())

# div() - Divides the values of a DataFrame with the specified value(s)
print(df['A'].div(2))

# dot() - Multiplies the values with another array-like object, adds result
print(df[['A', 'B']].dot([1, 1]))

# drop() - Drops the specified rows/columns from the DataFrame
print(df.drop(columns=['C']))

# drop_duplicates() - Drops duplicate values from the DataFrame
print(df.drop_duplicates(subset=['C']))

# droplevel() - Drops the specified index/column level (for MultiIndex)
mi_df = df.set_index(['C', 'A'])
print(mi_df.droplevel('C'))

# dropna() - Drops all rows that contain NULL values
print(nadf.dropna())

# dtypes - Returns the dtypes of the columns
print(df.dtypes)

# duplicated() - Returns True for duplicated rows, otherwise False
print(df.duplicated(subset=['C']))

# empty - Returns True if the DataFrame is empty
print(df.empty)
print(pd.DataFrame().empty)

# eq() - Returns True for values equal to the specified value(s)
print(df['A'].eq(3))

# equals() - Returns True if two DataFrames are equal
print(df.equals(df.copy()))

# eval() - Evaluate a specified string expression
print(df.eval('E = A + B'))

# explode() - Converts each element of a list-like column into a row
edf = pd.DataFrame({'A': [[1, 2], [3, 4]]})
print(edf.explode('A'))

# ffill() - Replaces NULL values with the value from the previous row
print(nadf.ffill())

# fillna() - Replaces NULL values with the specified value
print(nadf.fillna(0))

# filter() - Filter the DataFrame according to the specified filter
print(df.filter(items=['A', 'B']))

# first() - Returns the first rows of a specified date selection
date_df = pd.DataFrame({'A': range(5)}, index=pd.date_range('2021-01-01', periods=5))
print(date_df.first('2D'))

# floordiv() - Divides and floors the values
print(df['A'].floordiv(2))

# ge() - Returns True for values greater than or equal to specified value
print(df['A'].ge(3))

# get() - Returns the item of the specified key
print(df.get('A'))

# groupby() - Groups the rows/columns into specified groups
print(df.groupby('C').sum(numeric_only=True))

# gt() - Returns True for values greater than the specified value
print(df['A'].gt(3))

# head() - Returns the header row and the first N rows
print(df.head(3))

# iat - Get or set the value of the item at the specified position
print(df.iat[0, 0])
df.iat[0, 0] = 1
print(df)

# idxmax() - Returns the label of the max value
print(df['A'].idxmax())

# idxmin() - Returns the label of the min value
print(df['A'].idxmin())

# iloc - Get/set values of a group of elements by integer position
print(df.iloc[0])
print(df.iloc[0:2])

# index - Returns the row labels of the DataFrame
print(df.index)

# infer_objects() - Change dtype of columns to a more specific one
print(df.infer_objects().dtypes)

# info() - Prints information about the DataFrame
df.info()

# insert() - Insert a column in the DataFrame
df_ins = df.copy()
df_ins.insert(1, 'NewCol', [0, 0, 0, 0, 0])
print(df_ins)

# interpolate() - Replaces NaN values using interpolation
print(nadf.interpolate())

# isin() - Returns True if elements are in the specified value list
print(df['A'].isin([1, 3, 5]))

# isna() - Finds NaN values
print(df.isna())

# isnull() - Finds NULL values
print(df.isnull())

# items() - Iterate over the columns of the DataFrame
for label, content in df.items():
    print(label)

# iterrows() - Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    print(index, row['A'])

# itertuples() - Iterate over the rows as named tuples
for row in df.itertuples():
    print(row)

# join() - Join columns of another DataFrame
left = pd.DataFrame({'K': ['a', 'b'], 'L': [1, 2]}).set_index('K')
right = pd.DataFrame({'K': ['a', 'b'], 'M': [3, 4]}).set_index('K')
print(left.join(right))

# last() - Returns the last rows of a specified date selection
print(date_df.last('2D'))

# le() - Returns True for values less than or equal to specified value
print(df['A'].le(3))

# loc - Get/set values of a group of elements by label
print(df.loc[0])
print(df.loc[df['A'] > 2])

# lt() - Returns True for values less than the specified value
print(df['A'].lt(3))

# keys() - Returns the keys of the info axis (column labels)
print(df.keys())

# kurtosis() - Returns the kurtosis of the values
print(df[['A', 'B']].kurtosis())

# mask() - Replace all values where the specified condition is True
print(df['A'].mask(df['A'] > 3, 0))

# max() - Return the max of the values
print(df.max(numeric_only=True))

# mean() - Return the mean of the values
print(df.mean(numeric_only=True))

# median() - Return the median of the values
print(df.median(numeric_only=True))

# melt() - Reshape the DataFrame from wide to long format
print(df.melt(id_vars=['C'], value_vars=['A', 'B']))

# memory_usage() - Returns the memory usage of each column
print(df.memory_usage())

# merge() - Merge DataFrame objects
print(df.merge(df2, on='A', how='inner'))

# min() - Returns the min of the values
print(df.min(numeric_only=True))

# mod() - Modulus (remainder) of the values
print(df['A'].mod(2))

# mode() - Returns the mode of the values
print(df['C'].mode())

# mul() - Multiplies the values with the specified value(s)
print(df['A'].mul(2))

# ndim - Returns the number of dimensions of the DataFrame
print(df.ndim)

# ne() - Returns True for values not equal to the specified value
print(df['A'].ne(3))

# nlargest() - Sort descending and return specified number of rows
print(df.nlargest(2, 'A'))

# notna() - Finds values that are not NaN
print(df.notna())

# notnull() - Finds values that are not NULL
print(df.notnull())

# nsmallest() - Sort ascending and return specified number of rows
print(df.nsmallest(2, 'A'))

# nunique() - Returns the number of unique values
print(df.nunique())

# pct_change() - Percentage change between previous and current value
print(df['A'].pct_change())

# pipe() - Apply a function to the DataFrame
print(df.pipe(lambda d: d[['A', 'B']] * 2))

# pivot() - Re-shape the DataFrame
pivot_src = pd.DataFrame({'foo': ['a', 'a', 'b'], 'bar': [1, 2, 1], 'baz': [10, 20, 30]})
print(pivot_src.pivot(index='foo', columns='bar', values='baz'))

# pivot_table() - Create a spreadsheet-style pivot table
print(df.pivot_table(values='A', index='C', aggfunc='sum'))

# pop() - Removes an element/column from the DataFrame
df_pop = df.copy()
popped = df_pop.pop('C')
print(popped, df_pop)

# pow() - Raise the values to the values of another DataFrame
print(df['A'].pow(2))

# prod() / product() - Returns the product of all values
print(df[['A', 'B']].prod())
print(df[['A', 'B']].product())

# quantile() - Returns the values at the specified quantile
print(df['A'].quantile(0.5))

# query() - Query the DataFrame
print(df.query('A > 2'))

# radd() - Reverse-add
print(df['A'].radd(10))

# rdiv() - Reverse-divide
print(df['A'].rdiv(100))

# reindex() - Change the labels of the DataFrame
print(df.reindex([0, 1, 10]))

# reindex_like() - Reindex a DataFrame to match another's index/columns
print(df.reindex_like(df2))

# rename() - Change the labels of the axes
print(df.rename(columns={'A': 'Alpha'}))

# rename_axis() - Change the name of the axis
print(df.rename_axis('idx'))

# reorder_levels() - Re-order the index levels (for MultiIndex)
print(mi_df.reorder_levels(['A', 'C']))

# replace() - Replace the specified values
print(df['C'].replace('x', 'X'))

# reset_index() - Reset the index
print(df.reset_index(drop=True))

# rfloordiv() - Reverse floor-divide
print(df['A'].rfloordiv(10))

# rmod() - Reverse-modulus
print(df['A'].rmod(10))

# rmul() - Reverse-multiply
print(df['A'].rmul(2))

# round() - Round all values to the specified format
print(df[['A', 'B']].round(1))

# rpow() - Reverse power
print(df['A'].rpow(2))

# rsub() - Reverse subtract
print(df['A'].rsub(10))

# rtruediv() - Reverse true-divide
print(df['A'].rtruediv(10))

# sample() - Returns a random selection of elements
print(df.sample(2))

# sem() - Returns the standard error of the mean
print(df[['A', 'B']].sem())

# select_dtypes() - Returns columns of selected data types
print(df.select_dtypes(include='number'))

# shape - Returns the number of rows and columns
print(df.shape)

# set_axis() - Sets the index/columns of the specified axis
print(df.set_axis(['r1', 'r2', 'r3', 'r4', 'r5'], axis=0))

# set_flags() - Returns a new DataFrame with the specified flags
print(df.set_flags(allows_duplicate_labels=False))

# set_index() - Set the Index of the DataFrame
print(df.set_index('C'))

# size - Returns the number of elements in the DataFrame
print(df.size)

# skew() - Returns the skew of the values
print(df[['A', 'B']].skew())

# sort_index() - Sorts the DataFrame according to the labels
print(df.sort_index(ascending=False))

# sort_values() - Sorts the DataFrame according to the values
print(df.sort_values('A', ascending=False))

# squeeze() - Converts a single column DataFrame into a Series
print(df[['A']].squeeze())

# stack() - Reshape from wide table to long table
print(df[['A', 'B']].stack())

# std() - Returns the standard deviation of the values
print(df[['A', 'B']].std())

# sum() - Returns the sum of the values
print(df.sum(numeric_only=True))

# sub() - Subtracts the specified value(s)
print(df['A'].sub(1))

# swaplevel() - Swaps two specified index levels
print(mi_df.swaplevel())

# T - Turns rows into columns and columns into rows
print(df[['A', 'B']].T)

# tail() - Returns the headers and the last N rows
print(df.tail(3))

# take() - Returns the specified elements
print(df.take([0, 2]))

# to_xarray() - Returns an xarray object (requires xarray package)
# print(df.to_xarray())

# transform() - Execute a function for each value in the DataFrame
print(df[['A', 'B']].transform(lambda x: x * 2))

# transpose() - Turns rows into columns and columns into rows
print(df[['A', 'B']].transpose())

# truediv() - Divides the values (true division)
print(df['A'].truediv(2))

# truncate() - Removes elements outside a specified set of values
print(df.truncate(before=1, after=3))

# update() - Update one DataFrame with values from another
df_upd = df.copy()
df_upd.update(pd.DataFrame({'A': [99]}, index=[0]))
print(df_upd)

# value_counts() - Returns the number of unique rows/values
print(df['C'].value_counts())

# values - Returns the DataFrame as a NumPy array
print(df.values)

# var() - Returns the variance of the values
print(df[['A', 'B']].var())

# where() - Replace all values where the specified condition is False
print(df['A'].where(df['A'] > 2, 0))

# xs() - Returns the cross-section of the DataFrame
print(mi_df.xs('x', level='C'))

# __iter__() - Returns an iterator of the info axes (column names)
for col in df:
    print(col)


# ==========================================================
# EXTRA TOPICS (BONUS - beyond the official tutorial)
# ==========================================================

# ----------------------------------------------------------
# Pandas GroupBy
# ----------------------------------------------------------
gb_df = pd.DataFrame({
    'Team': ['A', 'A', 'B', 'B', 'C'],
    'Points': [10, 20, 15, 25, 30],
    'Rank': [1, 2, 1, 2, 1]
})
grouped = gb_df.groupby('Team')   # groups rows by column value
print(grouped.sum(numeric_only=True))         # sum per group
print(grouped.mean(numeric_only=True))        # mean per group
print(grouped['Points'].max())                 # max of one column per group

for name, group in grouped:   # iterate over groups
    print(name)
    print(group)

print(grouped.agg({'Points': 'sum', 'Rank': 'min'}))  # multiple aggregations
print(grouped.size())    # number of rows in each group


# ----------------------------------------------------------
# Pandas Merging, Joining & Concatenating
# ----------------------------------------------------------
left = pd.DataFrame({'id': [1, 2, 3], 'name': ['Tom', 'Jack', 'Steve']})
right = pd.DataFrame({'id': [1, 2, 4], 'score': [90, 85, 70]})

print(pd.merge(left, right, on='id', how='inner'))  # inner join (matching only)
print(pd.merge(left, right, on='id', how='left'))    # left join (keep all left)
print(pd.merge(left, right, on='id', how='right'))    # right join
print(pd.merge(left, right, on='id', how='outer'))     # outer join (all rows)

left2 = left.set_index('id')
right2 = right.set_index('id')
print(left2.join(right2))   # join() works on index by default

df_top = pd.DataFrame({'A': [1, 2]})
df_bottom = pd.DataFrame({'A': [3, 4]})
print(pd.concat([df_top, df_bottom]))                 # stack vertically
print(pd.concat([df_top, df_bottom], ignore_index=True))  # reset index after concat
print(pd.concat([df_top, df_bottom], axis=1))           # stack side by side (columns)


# ----------------------------------------------------------
# Pandas Pivot Tables
# ----------------------------------------------------------
sales = pd.DataFrame({
    'Store': ['A', 'A', 'B', 'B'],
    'Product': ['Shoes', 'Shirts', 'Shoes', 'Shirts'],
    'Sales': [100, 150, 200, 130]
})
print(sales.pivot(index='Store', columns='Product', values='Sales'))
# pivot() requires unique index/column combinations (no duplicates)

sales2 = pd.DataFrame({
    'Store': ['A', 'A', 'A', 'B'],
    'Product': ['Shoes', 'Shoes', 'Shirts', 'Shoes'],
    'Sales': [100, 50, 150, 200]
})
print(sales2.pivot_table(index='Store', columns='Product', values='Sales', aggfunc='sum'))
# pivot_table() can handle duplicates by aggregating them


# ----------------------------------------------------------
# Pandas MultiIndex (Hierarchical Indexing)
# ----------------------------------------------------------
arrays = [['A', 'A', 'B', 'B'], ['x', 'y', 'x', 'y']]
midx = pd.MultiIndex.from_arrays(arrays, names=('Letter', 'Sub'))
midf = pd.DataFrame({'Value': [1, 2, 3, 4]}, index=midx)
print(midf)

print(midf.loc['A'])            # select outer level
print(midf.loc[('A', 'x')])      # select specific combination
print(midf.unstack())             # pivot inner index level into columns
print(midf.reset_index())          # flatten MultiIndex into columns


# ----------------------------------------------------------
# Pandas Excel Files
# ----------------------------------------------------------
# writing to Excel requires: pip install openpyxl
excel_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
excel_df.to_excel('data.xlsx', index=False, sheet_name='Sheet1')  # write to Excel

read_excel_df = pd.read_excel('data.xlsx')   # read from Excel
print(read_excel_df)

# writing multiple sheets
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    excel_df.to_excel(writer, sheet_name='First')
    excel_df.to_excel(writer, sheet_name='Second')


# ----------------------------------------------------------
# Pandas Time Series / Date Range
# ----------------------------------------------------------
dates = pd.date_range(start='2024-01-01', periods=5, freq='D')  # daily dates
print(dates)

ts = pd.Series(range(5), index=dates)
print(ts)

print(ts.resample('2D').sum())   # resample to a different frequency

ts_df = pd.DataFrame({'value': range(10)},
                      index=pd.date_range('2024-01-01', periods=10, freq='D'))
print(ts_df['2024-01-03':'2024-01-06'])   # slice by date range

print(ts_df.rolling(window=3).mean())      # rolling (moving) average


# ----------------------------------------------------------
# Pandas apply(), map(), applymap()
# ----------------------------------------------------------
amap_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(amap_df['A'].map(lambda x: x * 10))     # map() -> works on a Series only
print(amap_df.apply(np.sum))                    # apply() -> works on rows/columns (axis)
print(amap_df.apply(lambda row: row['A'] + row['B'], axis=1))  # row-wise apply
print(amap_df.applymap(lambda x: x * 2))          # applymap() -> works element-wise on whole DataFrame


# ----------------------------------------------------------
# Pandas String Methods (.str accessor)
# ----------------------------------------------------------
str_df = pd.DataFrame({'Name': [' Tom ', 'JACK', 'steve']})
print(str_df['Name'].str.strip())        # remove whitespace
print(str_df['Name'].str.upper())         # uppercase
print(str_df['Name'].str.lower())          # lowercase
print(str_df['Name'].str.contains('a'))     # check substring
print(str_df['Name'].str.replace('T', 'J', regex=False))  # replace characters
print(str_df['Name'].str.len())               # length of each string


# ----------------------------------------------------------
# Pandas Categorical Data
# ----------------------------------------------------------
cat_df = pd.DataFrame({'Size': ['S', 'M', 'L', 'M', 'S']})
cat_df['Size'] = cat_df['Size'].astype('category')  # convert to category dtype
print(cat_df.dtypes)
print(cat_df['Size'].cat.categories)   # list categories

cat_df['Size'] = cat_df['Size'].cat.set_categories(['S', 'M', 'L'], ordered=True)
print(cat_df['Size'] < 'L')   # ordered comparison


# ----------------------------------------------------------
# Pandas Rolling / Window Functions
# ----------------------------------------------------------
win_df = pd.DataFrame({'Value': [1, 2, 3, 4, 5, 6]})
print(win_df.rolling(window=3).mean())    # rolling average over window of 3
print(win_df.expanding().sum())             # expanding (cumulative growing window) sum
print(win_df.ewm(span=3).mean())              # exponentially weighted mean


# ----------------------------------------------------------
# Pandas Binning (cut & qcut)
# ----------------------------------------------------------
ages = pd.Series([5, 15, 25, 35, 45, 60])
bins = pd.cut(ages, bins=[0, 18, 35, 60], labels=['Minor', 'Adult', 'Senior'])
print(bins)   # fixed-width bins

quantile_bins = pd.qcut(ages, q=3)  # equal-sized quantile bins
print(quantile_bins)


# ----------------------------------------------------------
# Pandas Crosstab
# ----------------------------------------------------------
cross_df = pd.DataFrame({
    'Gender': ['M', 'F', 'F', 'M', 'M'],
    'Result': ['Pass', 'Pass', 'Fail', 'Fail', 'Pass']
})
print(pd.crosstab(cross_df['Gender'], cross_df['Result']))  # frequency table


# ==========================================================
# END OF NOTES
# ==========================================================