# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

route_string_split = ospf_route.split()
route_string_split.pop(route_string_split.index('via'))


route_dict = {
		'Protocol': {
		'O':'OSPF',
		'S':'STATIC'
		}	
}

route_dict['Prefix'] = route_string_split[1]
route_dict['AD/Metric'] = route_string_split[2].strip('[]')
route_dict['Next-Hop'] = route_string_split[3].strip(',')	
route_dict['Last update'] = route_string_split[4]
route_dict['Outbound Interface'] = route_string_split[5]

print(route_dict['Protocol'][route_string_split[0]])


'''proto_dict = {
		'O':'OSPF',
		'S':'STATIC'
}
print(proto_dict['O'])'''


