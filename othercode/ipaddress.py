from othercode import ipjisuan
ipall=[]
def Ipsu(ipaddr):
    ipall=[]
    ip = ipaddr.split("/")[0]
    mask = ipaddr.split("/")[-1]
    if 8 < int(mask) <=16:
        kk=ipjisuan.jiange(mask)
        for i in kk:
            if mask=="16":
                for q in range(0,256):
                    ipall.append(ip.split(".")[0]+"."+ip.split(".")[1]+"."+str(i)+"."+str(q))
            elif int(ip.split(".")[0]) in range(i[0],i[-1]):
                for v in range(i[0],i[-1]):
                    for w in range(0,256):
                        for q in range(0,256):
                            ipall.append(ip.split(".")[0]+"."+str(v)+"."+str(w)+"."+str(q))
    elif 16 < int(mask) <=24:
        kk=ipjisuan.jiange(mask)
        if mask=="24":
            for i in kk:
                ipall.append(ip.split(".")[0] + "." + ip.split(".")[1] + "." + ip.split(".")[2] + "." + str(i))
        else:
            for i in kk:
                if int(ip.split(".")[2]) in range(i[0],i[-1]) :
                    for w in range(i[0],i[-1]):
                        for q in range(0,256):
                            ipall.append(ip.split(".")[0] + "." + ip.split(".")[1]+ "." + str(w) + "." + str(q))
    elif 24 < int(mask) <=32:
        kk=ipjisuan.jiange(mask)
        if mask=="32":
            ipall.append(ip.split(".")[0] + "." + ip.split(".")[1] + "." + ip.split(".")[2] + "." + ip.split(".")[3])
        for i in kk:
            if int(ip.split(".")[3]) in range(i[0],i[-1]):
                for q in range(i[0],i[-1]):
                    ipall.append(ip.split(".")[0] + "." + ip.split(".")[1] + "." + ip.split(".")[2] + "." + str(q))
    else:
        pass
    return ipall
if __name__=="__main__":
    Ipsu(ip)


