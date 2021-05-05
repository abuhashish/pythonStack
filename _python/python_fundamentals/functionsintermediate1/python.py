import random
def randInt(min=0   , max=100  ):
    num =min+ random.random()*max
    return num
print(randInt(0,50))