# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
cfg = CONFIG.split()
vlans = cfg[-1].split(',')
print(CONFIG)
print(cfg)
print(type(cfg))
print(cfg[-1])
print(type(cfg[-1]))
print(vlans)
print(type(vlans))
