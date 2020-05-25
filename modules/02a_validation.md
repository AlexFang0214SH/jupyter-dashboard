## Section 2 - Data Validation

## Python DataFrames

Rather than manually editing and saving spreadsheets, what if there was a tool which save all those steps, allow for collaboration and make it easy to share/publish your work? Yes, a database could do such a task but how about one which can combine text, publish in multiple formats (pdf, latex, html) and perform data science in a human-readable programming language such as Python? (Sorry, SQL!)

Well, this notebook is that tool and Python DataFrames (via the Pandas module) are the way by which to transform data without having to worry about whether your application (i.e. Excel) will crash and corrupt your source file when working with large datasets.

The links below will provide additional info but in general, data tables are loaded into the notebook and stored as DataFrames and assigned as variables which are like sheets within an Excel file. DataFrames can then be joined, manipulated and transformed programmatically. Rather than linking across a spreadsheet which can become complex and unsustainable over time, DataFrames can be managed cleaned with organized code (e.g. cells within this notebook).

The code examples will demonstrate how to explore the dataset before analyzing it using [summary statistics](https://en.wikipedia.org/wiki/Summary_statistics) and other techniques to examine the shape, properties and range of the dataset. Such exploration is used to evaluate which methods and plots make sense for a given dataset.

## Exercises

If you are new to DataFrames, then please review the links below:

* [Intro to DataFrames](https://databricks.com/glossary/what-are-dataframes)
* [DataFrames - DataCamp](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python)
* [Data Science Notes](https://chrisalbon.com/)
* [Summary Statistics Usage](https://chrisalbon.com/python/data_wrangling/pandas_dataframe_descriptive_stats/)

Please run code cells below with the "run" button located in the top menu. Cells will show the following:

1. Read in data into a DataFrame
2. Print first 5 rows of DataFrame
3. Extract numeric columns into separate DataFrame
4. Describe the dataset with summary statistics
5. Calculate correlation matric between numeric columns
