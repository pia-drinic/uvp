# 1. naloga
def vsota_veckratnikov(n):
    vsota = 0
    for i in range (0, n):
        if i // 3 == 0 or i // 5 == 0:
            vsota += i
        return vsota