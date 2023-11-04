import re


def main():
   #Tạo đối tượng biểu thức chính quy bằng cách sử dụng tính năng xem trước và xem lại để đảm bảo rằng không có số nào trước hoặc sau số điện thoại di động.
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
     Những điều quan trọng đã được nói 8130123456789. Số điện thoại di động của tôi là số này 13512346789.
     Không phải 15600998765 mà cũng là 110 hoặc 119. Số điện thoại di động của Wang Dachui là 15600998765.
     '''
    # Tìm tất cả các kết quả phù hợp và lưu vào danh sách
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------Dải ngăn cách--------')
    # Lấy đối tượng phù hợp thông qua iterator và lấy nội dung phù hợp
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('---------Dải ngăn cách--------')
    # Chỉ định vị trí tìm kiếm thông qua chức năng tìm kiếm để tìm tất cả kết quả phù hợp
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()