# 02B - Clean data
# reference: https://realpython.com/python-data-cleaning-numpy-pandas/

def find_duplicates(df, col, col_name, msg):
    print(msg, '\n')
    df.sort_values(col_name)

    # output validation results
    if df.shape[0] > 0:
        print('Duplicate Record Count: ', df.shape[0], '\n')
        print('Record ID / Record Value')
        print(df[col_name], '\n')
    elif df.shape[0] == 0:
        print('Column values are unique!\n')

# docyear 1618 projects: distppno
col_name_distppno = 'DISTPPNO'
col_proj_distppno = df_1618['DISTPPNO']
dup_proj_distppno = df_1618[col_proj_distppno.isin(col_proj_distppno[col_proj_distppno.duplicated()])]
find_duplicates(
    dup_proj_distppno,
    col_proj_distppno,
    col_name_distppno,
    '*** Validate Unique Values: Docyear 1618 Projects - District PPNO ***'
)

# docyear 1618 projects: ea number
col_name_ea = 'EA_NUMBER'
col_proj_ea = df_1618['EA_NUMBER']
dup_proj_ea = df_1618[col_proj_ea.isin(col_proj_ea[col_proj_ea.duplicated()])]
find_duplicates(
    dup_proj_ea,
    col_proj_ea,
    col_name_ea,
    '*** Validate Unique Values: Docyear 1618 Projects - EA Number ***'
)

# docyear 1618 projects: ppno
col_name_ppno = 'PPNO'
col_proj_ppno = df_1618['PPNO']
dup_proj_ppno = df_1618[col_proj_ppno.isin(col_proj_ppno[col_proj_ppno.duplicated()])]
find_duplicates(
    dup_proj_ppno,
    col_proj_ppno,
    col_name_ppno,
    '*** Validate Unique Values: Docyear 1618 Projects - PPNO Number ***'
)

# docyear 1618 projects: efis number
col_name_efis = 'EFISPROJID'
col_proj_efis = df_1618['EFISPROJID']
dup_proj_efis = df_1618[col_proj_efis.isin(col_proj_efis[col_proj_efis.duplicated()])]
find_duplicates(
    dup_proj_efis,
    col_proj_efis,
    col_name_efis,
    '*** Validate Unique Values: Docyear 1618 Projects - EFIS Number ***'
)
