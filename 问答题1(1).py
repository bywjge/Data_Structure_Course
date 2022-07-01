def GetNext(t, next):
    j, k = 0, -1
    next[0] = -1
    while j < len(t) - 1:
        if k == -1 or t[j] == t[k]:
            j, k = j+1, k+1
            next[j] = k
        else:
            k = next[k]
    print("next数组为： ", next)

def GetNextval(t, nextval):
    j, k = 0, -1
    nextval[0] = -1
    while j < len(t) - 1:
        if k == -1 or t[j] == t[k]:
            j, k = j+1, k+1
            if t[j] != t[k]:
                nextval[j] = k
            else:
                nextval[j] = nextval[k]
        else:
            k = nextval[k]
    print("nextval数组为： ", nextval)

if __name__ == "__main__":
    t = "ababaabab"
    next = [None] * len(t)
    nextval = [None] * len(t)
    GetNext(t, next)
    GetNextval(t, nextval)

