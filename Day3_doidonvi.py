value = float(input('Nhập độ dài: '))
unit = input('Nhập đơn vị: ')
if unit == 'in' or unit == 'inch':
    print('%finch = %fcm' % (value, value * 2.54))
elif unit == 'cm' or unit == 'centimet':
    print('%fcm = %finch' % (value, value / 2.54))
else:
    print('Vui lòng nhập đơn vị hợp lệ')