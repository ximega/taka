x = input("")
x = x.split(', ')
res = []
for _ in x:
    res.append(f"{_}={_}")
print(', '.join(res))