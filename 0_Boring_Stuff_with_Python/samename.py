def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    egg = 'bacosn local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)