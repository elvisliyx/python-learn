# -*- coding:utf-8 -*-

# username = input("username:")
# password = input("password:")

name = input("name:")
age = int(input("age:"))
print(type(age),type(str(age)))
job = input("job:")
salary = input("salary:")

info = '''
------info of %s --------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (name,name,age,job,salary)



info2 = '''
-----info of {_name}--------
Name:{_name}
Age:{_age}
Job:(_job}
Salary:{_salary}
''' .format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)

info3 = '''
------info of {0}--------
Name:{0}
Age:{1}
Job:(2}
Salary:{3}
''' .format(name,age,job,salary)

print(info)
print(info2)
print(info3)


