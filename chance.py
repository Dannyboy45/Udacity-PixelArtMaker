import random

def coin_flip():
    return random.choice(['heads', 'tails'])

#print coin_flip()

r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))

r2 = random.choice(['zamboni', 'motorcycle', 'tank'])
print("Random choice % s" % (r2))

def die_roll():
    return random.randint(1, 6)