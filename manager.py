from student import Student

ds = []

while True:
    print(f'''\n
    0. Thoát Chương trình
    1. Thêm Sinh Viên
    2. Cập nhật thông tin sinh viên
    3. Xóa sinh viên
    4. Xem thông tin tất cả sinh viên
    5. Xem Thông tin sinh viên
    6. Tìm sinh viên theo Tên
    7. Số lượng Sinh viên
    ''')
    select = input("Mời chọn chức năng:  ")

    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            id = input("Nhập Id Sinh viên:  ")
            name = input("Nhập Tên Sinh viên:  ")
            sv = Student(id , name)
            ds.append(sv)

        elif select == 2:
            id = input("Nhập Id sinh Viên bạn cần sửa :  ")
            for i in ds:
                if i.get_id() == id:
                    i.set_Name( input("Nhập vào tên mới:  ") )
                    i.show_info()

        elif select == 4:
            if len(ds) == 0:
                print("\n hiện không có sinh viên . Bạn vui lòng thêm sinh viên mói vào danh sách !")
            else:
                print(f"\nHiện có {len(ds)} Sinh viên ")
                for i in ds:
                    i.show_info()

        elif select == 3:
            id = input("Nhập Id Sinh viên cần xóa :  ")
            for i in ds:
                if i.get_id() == id:
                    ds.remove(i)
                    print("Bạn đã xóa sinh viên thành công ")
                    continue

        elif select == 5:
            id = input("Nhập Id Sinh Viên cần xem thông tin :  ")
            for i in ds:
                if i.get_id() == id:
                    i.show_info()
                    continue

        elif select == 6:
            ten = input("Nhập Tên Sinh Viên cần tìm :  ")
            for i in ds:
                if i.get_Name() == ten:
                    i.show_info()

        elif select == 7:
            print(f"\nHiện có { len(ds) } Sinh Viên \n")
    else:
        print("\nBạn phải nhập số. Vui Lòng nhập lại !")