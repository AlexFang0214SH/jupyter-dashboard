# 02 - read data to create dictionary

# load source data
def read_data(path):
    df = pd.read_csv(path)
    return(df)

# verify template and source data
dd_template = read_data('data/data_dictionary_v103.csv')
print('List of Data Dictionary Fields:', '\n', dd_template.columns, '\n')

hm_data = read_data('data/hm_fy1819.csv')
# print(data.info(), '\n')

def create_dictionary(data, system, table, path):
    # create list from data types
    # https://stackoverflow.com/questions/54221673/is-there-a-way-to-export-pandas-dataframe-info-df-info-into-an-excel-file
    df_types = pd.DataFrame(data.dtypes)
    print('Data Field Types:', '\n', df_types.iloc[:,0], '\n')
    list_types = df_types.iloc[:,0].tolist()

    # create list from data types
    # https://stackoverflow.com/questions/30101369/how-can-i-print-out-just-the-index-of-a-pandas-dataframe
    list_fields = df_types.index.tolist()
    print('List of Data Types:', '\n', list_fields, '\n')
    # print(type(list_fields), '\n')

    # create and populate dictionary
    dd = pd.DataFrame(index=data.columns)
    dd = dd.assign(FIELD_NAME = list_fields)
    dd = dd.assign(FIELD_TYPE = list_types)
    dd.insert(2, 'SYSTEM_NAME', system)
    dd.insert(3, 'TABLE_NAME', table)
    dd.insert(4, 'FIELD_ALIAS','TBD')
    dd.insert(5, 'FIELD_DESCRIPTION', 'TBD')
    dd.insert(6, 'FIELD_DESCRIPTION_AUTHORITY', 'TBD')
    dd.insert(7, 'CONFIDENTIAL','N')
    dd.insert(8, 'SENSITIVE', 'N')
    dd.insert(9, 'PII', 'N')
    dd.insert(10, 'PCI', 'N')
    dd.insert(11, 'FIELD_LENGTH','TBD')
    dd.insert(12, 'FIELD_PRECISION', 'TBD')
    dd.insert(13, 'DATA_CLASS', 'TBD')
    dd.insert(14, 'FIELD_UNITS','TBD')
    dd.insert(15, 'DOMAIN_TYPE','TBD')
    dd.insert(16, 'DEFAULT_VALUE', 'TBD')
    dd.insert(17, 'EXAMPLE_VALUE', 'TBD')
    dd.insert(18, 'INPUT_MASK', 'TBD')
    dd.insert(19, 'ALLOWABLE_MIN_VALUE','TBD')
    dd.insert(20, 'ALLOWABLE_MAX_VALUE', 'TBD')
    dd.insert(21, 'EXPECTED_MIN_VALUE', 'TBD')
    dd.insert(22, 'EXPECTED_MAX_VALUE','TBD')
    dd.insert(23, 'REQUIRED', 'N')
    dd.insert(24, 'UNIQUE', 'N')
    dd.insert(25, 'INDEXED', 'N')
    dd.insert(26, 'PRIMARY_KEY', 'N')
    dd.insert(27, 'FOREIGN_KEY','N')
    dd.insert(28, 'DATA_ENTRY_TYPE', 'Manual')
    dd.insert(29, 'SOURCE_SYSTEM', 'TBD')
    dd.insert(30, 'USAGE_NOTES', 'TBD')
    dd.insert(31, 'BUSINESS_TERM', 'TBD')

    # output results
    print('Data Dictionary:\n', dd, '\n')

    # write to csv file when done
    dd.to_csv(path)

create_dictionary(
    hm_data,
    'HM Spreadsheet',
    'HM Spreadsheet',
    'results/data_dictionary_hm.csv'
)
