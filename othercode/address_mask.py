def Mask(ip,y):
    y=int(y)
    if y==16:
        return ip +" 0.0.255.255"
    elif y==17:
        return ip +" 0.0.127.255"
    elif y == 17:
        return ip + " 0.0.127.255"
    elif y == 18:
        return ip + " 0.0.63.255"
    elif y == 19:
        return ip + " 0.0.31.255"
    elif y == 20:
        return ip + " 0.0.15.255"
    elif y == 21:
        return ip + " 0.0.7.255"
    elif y == 22:
        return ip + " 0.0.3.255"
    elif y == 23:
        return ip + " 0.0.1.255"
    elif y == 24:
        return ip + " 0.0.0.255"
    elif y == 25:
        return ip + " 0.0.0.127"
    elif y == 26:
        return ip + " 0.0.0.63"
    elif y == 27:
        return ip + " 0.0.0.31"
    elif y == 28:
        return ip + " 0.0.0.15"
    elif y == 29:
        return ip + " 0.0.0.7"
    elif y == 30:
        return ip + " 0.0.0.3"
    elif y == 31:
        return ip + " 0.0.0.1"
    elif y==32:
        return "host "+ip
    else:
        pass

if __name__=="__main__":
    Mask(ip,y)