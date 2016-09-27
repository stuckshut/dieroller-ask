from random import SystemRandom

numbergen = SystemRandom()

def rolldie(sides):
    roll = numbergen.randint(1,sides)
    return roll


def rolldice(num, sides):
    rolls = [rolldie(sides) for x in range(num)]
    return rolls


def sumdice(num, sides, drop=None, drop_num=0):
    if drop_num > num:
        return 0
    rolls = rolldice(num, sides)
    if drop=='highest' and drop_num > 0:
        for _ in range(drop_num):
           rolls.remove(max(rolls))
    elif drop=='lowest' and drop_num > 0:
        for _ in range(drop_num):
            rolls.remove(min(rolls))

    return sum(rolls)


def moddice(num, sides, mod='None', mod_num='0'):
    roll = sumdice(num, sides)
    if mod == 'add':
        roll = roll + mod_num
    elif mod == 'sub':
        roll = roll - mod_num

    return roll
