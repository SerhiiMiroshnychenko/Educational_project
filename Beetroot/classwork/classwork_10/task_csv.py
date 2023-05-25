# write csv data to docx

import csv
from mailmerge import MailMerge

with open('data.csv', 'rt', newline='') as file:
    csv_data = csv.DictReader(file)
    programmers = [{'name': row['Name'], 'date': row['Hire Date'],
                    'price': row['Salary'], 'days': row['Sick Days remaining']} for row in csv_data]
print(*programmers, sep='\n')


for data in programmers:
    template = MailMerge('template.docx')
    template.merge(**data)  # name='Sofia'
    template.write(f'results/document_{data["name"].replace(" ", "_")}.docx')


document_2 = MailMerge('template.docx')
document_2.merge_pages(programmers)
document_2.write('example2.docx')

