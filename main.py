from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("honebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# создаем новый пустой список
new_list = []
for value in contacts_list:

    str = value[0] + ' ' + value[1] + ' ' + value[2]
   
    new_str = str.split()
    
    if len(new_str) < 3:
      for lenght in range(3 - len(new_str)):
        new_str.append("")
    new_str.append(value[3] if value[3] else "")
    new_str.append(value[4] if value[4] else "")
    if value[5]:
      pattern = r"((?:8|\+7))[\s(]*(\d{1,3})[\s)-]*(\d{2,3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(?(\доб.)*\s*(\d*)(\))?"
      replace = r"+7(\2)\3-\4-\5 \6\7"
      phone = re.sub(pattern, replace, value[5])
      new_str.append(phone)
    else:
      new_str.append("")
    new_str.append(value[6] if value[6] else "")
    
    new_list.append(new_str)

# создаем словарь для группировки
grouped_data = {}

# Группируем по первым двум значениям
for item in new_list:
    key = (item[0], item[1])
    if key not in grouped_data:
        grouped_data[key] = item 
        
    else:
        for i in range(2, len(item)):
            if item[i] and item[i] not in grouped_data[key][i]:
                grouped_data[key][i] += f'{item[i]}'

result = list(grouped_data.values())


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список
  datawriter.writerows(result)
