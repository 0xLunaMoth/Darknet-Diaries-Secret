deci_list = [97, 50, 32, 97, 51, 32, 97, 52, 32, 98, 49, 32, 98, 53, 32, 99, 49, 32, 99, 53, 32, 100, 50, 32, 100, 52]
code = []
for i in deci_list:
	ascii_value = chr(i)
	#print(ascii_value)
	code.append(ascii_value)

print("".join(code).upper())