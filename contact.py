class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr


    def print_info(self):
        print("name : " + self.name)
        print("phone_number : " + self.phone_number)
        print("e_mail : " + self.e_mail)
        print("addr : " + self.addr)

def set_contact():
    name = input("name : ")
    phone = input("phone : ")
    e_mail = input("e_mail : ")
    addr = input("addr : ")
    contact = Contact(name, phone, e_mail, addr)
    return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def find_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            contact_list[i].print_info()

def print_menu():
    print("1. 연락처 입력 : ")
    print("2. 연락처 출력 : ")
    print("3. 연락처 삭제 : ")
    print("4. 연락처 검색 : ")
    print("5. 종료: ")
    menu = input("메뉴 선택 : ")
    return int(menu)


def run():
    contact_list = []
    contact_list.append(Contact("jjh", "010 - 1111- 1112", "kcj3054@naver.com", "대구"))
    contact_list.append(Contact("chaeyoung", "010 - 112- 119", "chaeyoun@naver.com", "부산"))
    contact_list.append(Contact("jjh", "010 - 9876- 1112", "kcj@naver.com", "경기"))
    while 1:
        menu = print_menu()
        if menu == 1:
           contact =  set_contact()
           contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name to delete : ")
            delete_contact(contact_list, name)
        elif menu == 4:
            name = input("Name to find : ")
            find_contact(contact_list, name)
        elif menu == 5:
            break

if __name__ == "__main__":
    run()