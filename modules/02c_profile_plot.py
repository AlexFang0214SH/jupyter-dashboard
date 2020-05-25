# 02C - Plot data profile results

# set plot and create countplot
def count_plot(title, df, col_name):
    plt.figure(figsize=(12, 8))
    plt.title(title)
    sns.countplot(
        data=df,
        y=col_name
    )

count_plot('Count Plot: Project List by Source', df_1618, 'SOURCE')
count_plot('Count Plot: Project List by Document', df_1618, 'DOCUMENT')
count_plot('Count Plot: Project List by Phase', df_1618, 'CURRENT_PHASE')
