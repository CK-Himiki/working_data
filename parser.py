with open('/Users/akulikov/Downloads/BAKUP.SPB', 'rb') as file: # вместо /Users/akulikov/Downloads/BAKUP.SPB свой путь до файла
    binary_data = file.read()
split=binary_data.split(b'\x08\x00\x08')[1:]
def tempo_reader2(binary_data):
    def to_u(bstr):
        try:
            unicode_str = bstr.decode('cp1251')
        except:
            unicode_str="ОШИБКА"
        return unicode_str
    
    record={"type":None,"formula":None,"name":None,"class":None,"mass":None}
    if binary_data[0]==12:
        record["type"]="Полимер"
    elif binary_data[0]==8:
        record["type"]="Мономер"
    elif binary_data[0]==24:
        record["type"]="Олигомер"
    else:
        record["type"]="неизвестно"
    offset=binary_data[4]
    record["formula"]=to_u(binary_data[5:5+offset])
    offset2=binary_data[5+offset]
    record["name"]=to_u(binary_data[6+offset:6+offset+offset2])
    offset3=binary_data[6+offset+offset2]
    record["class"]=to_u(binary_data[7+offset+offset2:7+offset+offset2+offset3])
    
    return record
import csv
with open('данные2.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in split:
        writer.writerow(list(tempo_reader2(row).values()))
