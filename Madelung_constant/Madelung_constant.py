import math # 导入sqrt


name = str(input("请输入离子晶体的名称："))
n = int(input("请输入晶胞个数："))


def TrueorFalse(name):
	if name == 'NaCl':
		Madelung_NaCl( n)
	elif name == 'CsCl':
		Madelung_CsCl(n)
	else:
		print("╮(╯3╰)╭")


def Madelung_NaCl(n):
	result = 0
	for n1 in range(-n, n+1):
		for n2 in range(-n, n+1):
			for n3 in range(-n, n+1):
				if math.sqrt(n1**2 + n2**2 + n3**2) != 0:
					result -= ((-1)**(n1+n2+n3)) / (math.sqrt(n1**2 + n2**2 + n3**2))
	print(result)



def Madelung_CsCl(n):
    negative, positive = 0, 0
    n = n + (n & 0x1)

    # 与中心离子相反
    for n1 in range(1, n, 2):
        # 体对角线
        negative -= (math.sqrt(3)/18) / n1
        # 面上离子
        for n2 in range(n1+2, n, 2):
            length1 = n1 ** 2 + n2 ** 2
            negative -= (1/2) / (math.sqrt(length1 + n2**2)) 
            negative -= (1/2) / (math.sqrt(length1 + n1**2))
            # 内部离子
            for n3 in range(n2+2, n, 2):
                negative -= 1 / (math.sqrt(length1 + n3**2))

    # 与中心离子相同
    for n1 in range(1, n-2, 2):
        # 线上的（4种）
        positive += (1/8 + math.sqrt(2)/8 + math.sqrt(3)/18) / n1
        positive += 1/8 / (math.sqrt(2 * n**2 + n1**2))
        positive += 1/4 / (math.sqrt(n**2 + n1**2))
        positive += 1/4 / (math.sqrt(n**2 + 2 * n1**2))
        # 面上
        for n2 in range(n1+2, n-2, 2):
            length2 = n1**2 + n2**2
            positive += 1/2 / (math.sqrt(length2))
            positive += 1/2 / (math.sqrt(length2 + n**2))
            positive += 1/2 / (math.sqrt(length2 + n1**2))
            positive += 1/2 / (math.sqrt(length2 + n2**2))
            #内部
            for n3 in range(n2+2, n-2, 2):
                positive += 1 / (math.sqrt(length2 + n3**2))
    positive += (1 + math.sqrt(2)/2 + math.sqrt(3)/9) / 16*n
    
    result = (negative + positive) * (48)
    print(result)


TrueorFalse(name)