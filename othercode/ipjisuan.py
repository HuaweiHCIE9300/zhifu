from othercode import jisuanjiange

def jiange(vv):
    if int(vv)==8 or int(vv)==16 or int(vv)==24:
        alljiange=jisuanjiange.jisuan(8)
    elif 8<int(vv) <= 15:
        vv = int(vv) - 8
        alljiange=jisuanjiange.jisuan(vv)
    elif 16<int(vv)<=23:
        vv=int(vv)-16
        alljiange=jisuanjiange.jisuan(vv)
    elif 24<int(vv)<=31:
        vv=int(vv) - 24
        alljiange=jisuanjiange.jisuan(vv)
    else:
        alljiange=jisuanjiange.jisuan(vv)
    return alljiange
if __name__=="__main__":
    jiange(vv)