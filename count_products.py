def count_products(data):
	da = []
	for d in data:
		da.append(d.split())    # create lists in a list
	print(da)
	data_dic = {}
	for d in da:
		if d[0] in data_dic:    # say if first, or it will replace milk_tea 2
			data_dic[d[0]] += int(d[1])
		else:
			data_dic[d[0]] = int(d[1])
	print(data_dic)


data = ['milk_tea 2', 'rice 1', 'coco 10', 'milk_tea 1']
count_products(data)