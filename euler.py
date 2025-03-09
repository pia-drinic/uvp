# 1. naloga
def vsota_veckratnikov(n):
    vsota = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            vsota += i
    return vsota

print(vsota_veckratnikov(10))
print(vsota_veckratnikov(1000))