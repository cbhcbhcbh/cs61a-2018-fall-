import math  # 导入sqrt


name = str(input("请输入离子晶体的名称："))
N = int(input("请输入晶胞个数："))


def TrueorFalse(name, N):
    if name == 'NaCl':
        print(Madelung_NaCl(N))
    elif name == 'CsCl':
        print(Madelung_CsCl(N))
    else:
        print("╮(╯3╰)╭")


def Madelung_NaCl(N):
    result = 0
    for n1 in range(-N, N + 1):
        for n2 in range(-N, N + 1):
            for n3 in range(-N, N + 1):
                if math.sqrt(n1**2 + n2**2 + n3**2) != 0:
                    result -= ((-1)**(n1 + n2 + n3)) / \
                        (math.sqrt(n1**2 + n2**2 + n3**2))
    return result


def Madelung_CsCl(N):
    N = N + (N & 0x1)
    N2 = N * N
    negative = positive = 0

    for n1 in range(1, N, 2):
        # 体对角线: 1/6 × 1/√3 = √3/18 = C
        negative -=  0.09622504486493762 / n1
        n12 = n1 * n1
        for n2 in range(n1 + 2, N, 2):
            n22 = n2 * n2
            AB = n12 + n22
            # 在三棱锥面上的原子, 1/2
            negative -= 0.5 / math.sqrt(AB + n12)  # x = y, 1/2
            negative -= 0.5 / math.sqrt(AB + n22)  # y = z, 1/2
            # 三棱锥内部的原子
            for n3 in range(n2 + 2, N, 2):
                negative -= 1 / math.sqrt(AB + n3 * n3)

    for n1 in range(2, N, 2):
        # 坐标轴上: 1/8
        # 面对角线: 1/4 × 1/√2 = √2/8
        # 体对角线: 1/6 × 1/√3 = √3/18
        n12 = n1 * n1
        positive += 0.39800174016157447 / n1        # E = (1/8 + √2/8 + √3/18)
        positive += 0.125 / math.sqrt(2 * N2 + n12) # x = N, y = N, 1/8
        positive += 0.250 / math.sqrt(N2 + 2 * n12) # x = N, y = z, 1/4
        positive += 0.250 / math.sqrt(N2 + n12)     # x = N, z = 0, 1/4
        for n2 in range(n1 + 2, N, 2):
            n22 = n2 * n2
            AB = n12 + n22
            # 在三棱锥面上的原子, 1/2
            positive += 0.5 / math.sqrt(AB)       # z = 0, 1/2
            positive += 0.5 / math.sqrt(AB + N2)  # x = N, 1/2
            positive += 0.5 / math.sqrt(AB + n12)  # x = y, 1/2
            positive += 0.5 / math.sqrt(AB + n22)  # y = z, 1/2
            # 三棱锥内部的原子
            for n3 in range(n2 + 2, N, 2):
                positive += 1 / math.sqrt(AB + n3 * n3)

    # (1 + √2/2 + √3/9)/16
    positive += 0.11872230443227642 / N
    return -48 * (negative + positive)


TrueorFalse(name, N)
