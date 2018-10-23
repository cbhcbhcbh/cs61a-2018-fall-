import math # 导入sqrt


name = str(input("请输入离子晶体的名称："))
n = 100


def TrueorFalse(name):
	if name == 'NaCl':
		Madelung_NaCl(name, n)
	elif name == 'CsCl':
		Madelung_CsCl(name, n)
	else:
		print("╮(╯3╰)╭")


def Madelung_NaCl(name, n):
	result = 0
	for n1 in range(-n, n+1):
		for n2 in range(-n, n+1):
			for n3 in range(-n, n+1):
				if math.sqrt(n1**2 + n2**2 + n3**2) != 0:
					result += ((-1)**(n1+n2+n3)) / (math.sqrt(n1**2 + n2**2 + n3**2))
	print(result)


# def Madelung_CsCl(name, n):

"""
def CsCl8(N):
    negative, positive = 0.0, 0.0
    N = N + (N & 0x1)
    N2 = N**2
    for n1 in range(1, N + 1, 2):
        n12 = n1**2
        for n2 in range(1, N + 1, 2):
            AB = n12 + n2**2
            for n3 in range(1, N + 1, 2):
                negative -= 1 / math.sqrt(AB + n3**2)
    for n1 in range(2, N, 2):
        n12 = n1**2
        positive += 0.75 / n1                    # 3条坐标轴
        positive += 0.75 / math.sqrt(n12 + 2*N2)  # 与坐标轴平行的3条棱
        positive += 1.5 / math.sqrt(n12 + N2)   # 与坐标轴垂直的6条棱
        for n2 in range(2, N, 2):
            AB = n12 + n2**2
            positive += 1.5 / math.sqrt(AB)      # 3个坐标面
            positive += 1.5 / math.sqrt(AB + N2)  # 与坐标轴垂直的3个面
            for n3 in range(2, N, 2):
                positive += 1 / math.sqrt(AB + n3**2)
    positive += (3 + 3 / math.sqrt(2) + 1 / math.sqrt(3)) / (8 * N)
    return -8 * (positive + negative)
"""



TrueorFalse(name)