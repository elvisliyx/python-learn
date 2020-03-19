# -*- coding:utf-8 -*-

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Elvis',120),
]
shopinglist = []
salary = input("Input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("选择要买什么？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item =  product_list[user_choice]
                if p_item[1] <= salary:
                    shopinglist.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your curret balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print('余额只剩[%s]，买不了东西了'%salary)
            else:
                print('Product code [%s] is not exit!' %user_choice )
        elif user_choice == 'q':
            print("-------shopping list-------------")
            for p in shopinglist:
                print(p)
            print('Your current balance:',salary)
            exit()
        else:
            print('Invalid option')




