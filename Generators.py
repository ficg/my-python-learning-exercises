def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)


def countdown(i):
    while i > 0:
        yield i
        i -= 1


for i in countdown(i):
    print(list(countdown(5)))

for i in countdown(5):
    print(list(countdown(5)))

for i in countdown(5):
    print(list(countdown(i)))
