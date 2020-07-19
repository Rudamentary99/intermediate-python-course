import random


def main():
    dice_amnt = 2
    dice_sum = 0
    for i in range(0, dice_amnt):
        roll = random.randint(1, 20)
        dice_sum += roll
        print(f'You rolled a {roll}')
    print(f'rolls total: {dice_sum}')


if __name__ == "__main__":
    main()
