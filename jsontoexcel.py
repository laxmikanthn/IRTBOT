# import pandas
# excel_data_df = pandas.read_excel(
#     'sampledatahockey.xlsx', sheet_name='playerdata')
# #json_str = excel_data_df.to_json()


# json_str = excel_data_df.to_json(orient='records')
# print('excel sheet to json:\n', json_str)


import excel2json
excel2json.convert_from_file('sampledatahockey.xlsx')
