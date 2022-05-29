#  -*-coding:utf8 -*-


def input_digital():
    number = 7
    guess = -1
    print("数字猜谜游戏!")
    while guess != number:
        guess = int(input("请输入你猜的数字："))

        if guess == number:
            print("恭喜，你猜对了！")
        elif guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")


if __name__ == '__main__':
    input_digital()
