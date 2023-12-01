# This algorithm combines 3 first number form an list of ip address and save it into another list

ip = ["198.123.xx.xx", "177.123.xx.xx",
      "199.123.xx.xx", "166.123.xx.xx", "165.123.xx.xx"]
new_list = []

for i in ip:
    new_list.append(i[0:3])

print(new_list)
