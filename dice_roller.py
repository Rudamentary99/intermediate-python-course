import random

dice_amnt = int(input('how many dice you tossing?'))
dice_size = int(input('how many sides?'))


def getResponse(pRoll):
    try:
        responses = {1: "you rolled a 1. critical fail",
                     dice_size: "you rolled a critical success"}
        return responses[pRoll]
    except KeyError:
        return ''


def main():
    dice_sum = 0
    for i in range(0, dice_amnt):
        roll = random.randint(1, dice_size)
        dice_sum += roll
        resp = getResponse(roll)
        if resp:
            print(resp)
        else:
            print(f'You rolled a {roll}')
    print(f'\nrolls total: {dice_sum}')


if __name__ == "__main__":
    main()
