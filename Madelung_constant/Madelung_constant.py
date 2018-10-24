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
					result += ((-1)**(n1+n2+n3)) / (math.sqrt(n1**2 + n2**2 + n3**2))
	print(result)


def Madelung_CsCl(n):
	"""
	function CsCl48(N::Int64)
    N = N + (N & 0x1)
    negative, positive, N² = 0.0, 0.0, N^2
    for n₁ ∈ 1:2:N
        # 体对角线: 1/6 × 1/√3 = √3/18
        negative -= √3/18 / n₁
        n₁² = n₁^2
        for n₂ ∈ n₁+2:2:N
            n₂² = n₂^2
            AB = n₁² + n₂²
            # 在三棱锥面上的原子, 1/2
            negative -= 1/2 / √(AB + n₁²)  # x = y
            negative -= 1/2 / √(AB + n₂²)  # y = z
            # 三棱锥内部的原子
            for n₃ ∈ n₂+2:2:N
                negative -= 1 / √(AB + n₃^2)
            end
        end
    end
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

TrueorFalse(name)