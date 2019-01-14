# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
cmd1 = command1.split()
cmd2 = command2.split()
vlan1 = cmd1[-1].split(',')
vlan2 = cmd2[-1].split(',')
set1 = set(vlan1)
set2 = set(vlan2)
set3 = set1 & set2
result = list(set3)
print(type(set3))
print(set3)
print(result)

