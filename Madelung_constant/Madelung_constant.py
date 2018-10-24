import math # 导入sqrt


name = str(input("请输入离子晶体的名称："))
n = 100


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


"""
    # 与中心离子相同
    for n₁ ∈ 2:2:N-2
        # 坐标轴上: 1/8
        # 面对角线: 1/4 × 1/√2 = √2/8
        # 体对角线: 1/6 × 1/√3 = √3/18
        n₁² = n₁^2
        positive += (1/8 + √2/8 + √3/18) / n₁
        positive += 1/8 / √(2N² + n₁²)  # x = N, y = N
        positive += 1/4 / √(N² + 2n₁²)  # x = N, y = z
        positive += 1/4 / √(N² + n₁²)   # x = N, z = 0
        for n₂ ∈ n₁+2:2:N-2
            n₂² = n₂^2
            AB = n₁² + n₂²
            # 在三棱锥面上的原子, 1/2
            positive += 1/2 / √(AB)        # z = 0
            positive += 1/2 / √(AB + N²)   # x = N
            positive += 1/2 / √(AB + n₁²)  # x = y
            positive += 1/2 / √(AB + n₂²)  # y = z
            # 三棱锥内部的原子
            for n₃ ∈ n₂+2:2:N-2
                positive += 1 / √(AB + n₃^2)
            end
        end
    end
    positive += (1 + √2/2 + √3/9)/16N
    return -48(negative + positive)
end
	"""

def Madelung_CsCl(n):
    negative, positive = 0, 0

    # 与中心离子相同
    for n1 in range(1, n+1, 2):
        # 线上的（4种）
        positive += (1/8) / n1
        
        
    # 与中心离子相反
    for n1 in range(1, n, 2):
        # 体对角线
        negative -= (math.sqrt(3)) / (18 * n1)
        # 面上离子
        for n2 in range(n1+2, n, 2):
            length = n1 ** 2 + n2 ** 2
            negative -= (1/2) / (math.sqrt(length + n2**2)) + (0.5) / (math.sqrt(length + n1**2))
            # 内部离子
            for n3 in range(n2+2, n, 2):
                negative -= 1 / (math.sqrt(length + n3**2))



TrueorFalse(name)