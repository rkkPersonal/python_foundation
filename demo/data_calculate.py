# https://www.runoob.com/python3/python3-basic-operators.html
def calculate_all_symbol():
    a = 21
    b = 10
    c = 0

    c = a + b
    print("1 - c ��ֵΪ��", c)

    c = a - b
    print("2 - c ��ֵΪ��", c)

    c = a * b
    print("3 - c ��ֵΪ��", c)

    c = a / b
    print("4 - c ��ֵΪ��", c)

    c = a % b
    print("5 - c ��ֵΪ��", c)

    # �޸ı��� a ��b ��c
    a = 2
    b = 3
    c = a ** b
    print("6 - c ��ֵΪ��", c)

    a = 10
    b = 5
    c = a // b
    print("7 - c ��ֵΪ��", c)


def calculate_compare():
    a = 21
    b = 10
    c = 0

    if (a == b):
        print("1 - a ���� b")
    else:
        print("1 - a ������ b")

    if (a != b):
        print("2 - a ������ b")
    else:
        print("2 - a ���� b")

    if (a < b):
        print("3 - a С�� b")
    else:
        print("3 - a ���ڵ��� b")

    if (a > b):
        print("4 - a ���� b")
    else:
        print("4 - a С�ڵ��� b")

    # �޸ı��� a �� b ��ֵ
    a = 5
    b = 20
    if (a <= b):
        print("5 - a С�ڵ��� b")
    else:
        print("5 - a ����  b")

    if (b >= a):
        print("6 - b ���ڵ��� a")
    else:
        print("6 - b С�� a")


def calculate_evaluation():
    a = 21
    b = 10
    c = 0

    if (a == b):
        print("1 - a ���� b")
    else:
        print("1 - a ������ b")

    if (a != b):
        print("2 - a ������ b")
    else:
        print("2 - a ���� b")

    if (a < b):
        print("3 - a С�� b")
    else:
        print("3 - a ���ڵ��� b")

    if (a > b):
        print("4 - a ���� b")
    else:
        print("4 - a С�ڵ��� b")

    # �޸ı��� a �� b ��ֵ
    a = 5
    b = 20
    if (a <= b):
        print("5 - a С�ڵ��� b")
    else:
        print("5 - a ����  b")

    if (b >= a):
        print("6 - b ���ڵ��� a")
    else:
        print("6 - b С�� a")


def logic_calculate_operation():
    a = 10
    b = 20

    if (a and b):
        print("1 - ���� a �� b ��Ϊ true")
    else:
        print("1 - ���� a �� b ��һ����Ϊ true")

    if (a or b):
        print("2 - ���� a �� b ��Ϊ true��������һ������Ϊ true")
    else:
        print("2 - ���� a �� b ����Ϊ true")

    # �޸ı��� a ��ֵ
    a = 0
    if (a and b):
        print("3 - ���� a �� b ��Ϊ true")
    else:
        print("3 - ���� a �� b ��һ����Ϊ true")

    if (a or b):
        print("4 - ���� a �� b ��Ϊ true��������һ������Ϊ true")
    else:
        print("4 - ���� a �� b ����Ϊ true")

    if not (a and b):
        print("5 - ���� a �� b ��Ϊ false��������һ������Ϊ false")
    else:
        print("5 - ���� a �� b ��Ϊ true")


def member_calculate():
    a = 10
    b = 20
    list = [1, 2, 3, 4, 5]

    if (a in list):
        print("1 - ���� a �ڸ������б��� list ��")
    else:
        print("1 - ���� a ���ڸ������б��� list ��")

    if (b not in list):
        print("2 - ���� b ���ڸ������б��� list ��")
    else:
        print("2 - ���� b �ڸ������б��� list ��")

    # �޸ı��� a ��ֵ
    a = 2
    if (a in list):
        print("3 - ���� a �ڸ������б��� list ��")
    else:
        print("3 - ���� a ���ڸ������б��� list ��")

