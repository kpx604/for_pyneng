# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = '2A4F:0000:12FF'
MAC = MAC.lower()
mac_list = MAC.split(':')
mac_list = ''.join(mac_list)
mac_byte = '{:b}'.format(int(mac_list,16))
print(mac_list)
print(mac_byte)

