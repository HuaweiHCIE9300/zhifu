def jisuan(vv):
    vv=int(vv)
    qujian=[]
    for v in range(1, 9):
        for i in range(0, 257):
            if v == vv == 1 and i % 128 == 0:
                k = [i - 128, i]
                qujian.append(k)
            elif v == vv == 2 and i % 64 == 0:
                k = [i - 64, i]
                qujian.append(k)
            elif v == vv == 3 and i % 32 == 0:
                k = [i - 32, i]
                qujian.append(k)
            elif v == vv == 4 and i % 16 == 0:
                k = [i - 16, i]
                qujian.append(k)
            elif v == vv == 5 and i % 8 == 0:
                k = [i - 8, i]
                qujian.append(k)
            elif v == vv == 6 and i % 4 == 0:
                k = [i - 4, i]
                qujian.append(k)
            elif v == vv == 7 and i % 2 == 0:
                k = [i - 2, i]
                qujian.append(k)
            elif v == vv == 8:
                if i==256:
                    pass
                else:
                    qujian.append(i)
    return qujian
if __name__=="__main__":
    jisuan(vv)