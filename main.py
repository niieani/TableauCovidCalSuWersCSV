from tableauscraper import TableauScraper as TS
import csv

url = 'https://datavisualization.cdph.ca.gov/t/SARSCov2/views/CalSuWersDashboard_v5_16445134862180/Cal-SuWers'
ts = TS()
ts.loads(url)
wb = ts.getWorkbook()
data = wb.getCsvData(sheetName='Map')

# filename = 'items.csv'
# f = open(filename, 'w', newline='')

data.to_csv('items.csv')
data.to_excel('items.xlsx')

# print(data, file=f, sep=';')

# if __name__ == '__main__':
#     filename = 'items.csv'
#     try:
#         with open(filename, 'w', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerows(data)
#             # for item in data:
#             #     writer.writerow(dir(item))
#     except BaseException as e:
#         print('BaseException:', filename)
#     else:
#         print('Data has been loaded successfully !')
