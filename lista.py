#!/usr/bin/env python3

# Listo vulnerabilidades
cve_list = ['CVE-2023-1435', 'CVE-2022-45761', 'CVE-2023']

print(cve_list)

cve_list.remove('CVE-2023')

print(cve_list)

# Listo puertos
puertos_tcp = [21, 22, 25, 80, 443, 8080, 445, 69]

puertos_tcp.append(1337)

puertos_tcp.sort()

print(puertos_tcp)

# Listo ataques
attacks = ['Phishing', 'DDos', 'SQL Injection', 'Man In The Middle', 'Cross-Site Scripting']

print(attacks)

attacks.reverse()

print(attacks)

names = ["S4vitar", "Hackermate", "Lobotec", "Hackavis"]
edades = [27, 45, 13, 20]

for name, edad in zip(names, edades):
    print(f"{name} tienes {edad}")
