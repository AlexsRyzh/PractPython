import uuid

l = {}

id = uuid.uuid4()
n = 0

while id not in l and n < 10000000:
    l[str(id)] = True
    id = uuid.uuid4()
    n += 1


print(id, n)
