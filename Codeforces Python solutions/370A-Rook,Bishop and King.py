# 370A-Rook,Bishop and King

r1, c1, r2, c2 = map(int, input().split())
def rook(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2:
        return 1
    else:
        return 2


def bishop(r1, c1, r2, c2):
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        return 0
    else:
        if r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2:
            return 1
        else:
            return 2


def king(r1, c1, r2, c2):
    return max(abs(r1 - r2), abs(c1 - c2))


r = rook(r1, c1, r2, c2)
b = bishop(r1, c1, r2, c2)
k = king(r1, c1, r2, c2)
print(r, b, k)