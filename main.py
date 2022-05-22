from tableauscraper import TableauScraper as TS

url = 'https://datavisualization.cdph.ca.gov/t/SARSCov2/views/CalSuWersDashboard_v5_16445134862180/Cal-SuWers'
ts = TS()
ts.loads(url)
wb = ts.getWorkbook()
data = wb.getCsvData(sheetName='Map')

print(data)
