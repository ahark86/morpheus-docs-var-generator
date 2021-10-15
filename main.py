import csv

with open('534nav.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    var_list = []
    for row in csv_reader:
        var_name = f'{row[0][0:3]}{row[1][0:3]}{row[2][0:3]}'
        if row[1] == "":
            var_item = f'{row[0]}'
        elif row[1] != "" and row[2] == "":
            var_item = f'{row[0]} > {row[1]}'
        else:
            var_item = f'{row[0]} > {row[1]} > {row[2]}'
        var_list.append([var_name, var_item, f'.. |{var_name}| replace:: {var_item}'])

with open('534vars.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for item in var_list:
        csv_writer.writerow(item)