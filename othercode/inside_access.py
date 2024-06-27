
from othercode import address_mask
def Inside(sip1,dip1,svlan1,dvlan1,dport1,sip2,dip2,svlan2,dvlan2,dport2,sip3,dip3,svlan3,dvlan3,dport3,sip4,dip4,svlan4,dvlan4,dport4):
    zf01=zf02=416
    bb=[]
    g1=[sip1,dip1,svlan1,dvlan1,dport1]
    bb.append(g1)
    g2=[sip2,dip2,svlan2,dvlan2,dport2]
    if g2[2]==None:
        pass
    else:
        bb.append(g2)
    g3=[sip3,dip3,svlan3,dvlan3,dport3]
    if g3[2]==None:
        pass
    else:
        bb.append(g3)
    g4=[sip4,dip4,svlan4,dvlan4,dport4]
    if g4[2]==None:
        pass
    else:
        bb.append(g4)
    aa=[]
    cc=[]
    for i in bb:
        S_Vlan = i[2]
        D_Vlan = i[3]
        x = i[0].split("/")[0]
        y = i[0].split("/")[1]
        xx = i[1].split("/")[0]
        yy = i[1].split("/")[1]
        S_ip = address_mask.Mask(x, y)
        D_ip = address_mask.Mask(xx, yy)
        if bool(i[-1]) is False:
            D_port = "0"
        else:
            D_port = i[-1]
        if D_port == "0":
            if S_ip.split(".")[1] == "8" and D_ip.split(".")[1] == "8":
                a="===============ZF01-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + S_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf01)+" permit tcp " + S_ip + " " + D_ip
                zf01=zf01+1
                aa.append(a)
                # ============================================================
                a = "===============ZF01-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + D_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf01)+" permit tcp " + D_ip + " " + S_ip
                zf01=zf01+1
                aa.append(a)
            elif S_ip.split(".")[1] == "108" and D_ip.split(".")[1] == "108":

                a="===============ZF02-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + S_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf02)+" permit tcp " + S_ip + " " + D_ip
                zf02=zf02+1
                aa.append(a)
                a = "===============ZF02-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + D_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf02)+" permit tcp " + D_ip + " " + S_ip
                zf02=zf02+1
                aa.append(a)
            elif S_ip.split(".")[1] == "8" and D_ip.split(".")[1] == "108":
                a="===============ZF01-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + S_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf01)+" permit tcp " + S_ip + " " + D_ip
                zf01=zf01+1
                aa.append(a)
                # =========================================================
                a="===============ZF02-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + D_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf02)+" permit tcp " + D_ip + " " + S_ip
                zf02=zf02+1
                aa.append(a)
                # =============================================================
                a="===============ZF01-LINK-AS-01/02==============="
                aa.append(a)
                a="ip access-list extended  ZF01-TWIDC-OUT"
                aa.append(a)
                a="    permit tcp " + S_ip + " " + D_ip
                aa.append(a)
                # ==============================================================
                a="===============ZF02-LINK-AS-01/02==============="
                aa.append(a)
                a="ip access-list extended  ZF02-JPIDC-OUT"
                aa.append(a)
                a="    permit tcp " + D_ip + " " + S_ip
                aa.append(a)
            elif S_ip.split(".")[1] == "108" and D_ip.split(".")[1] == "8":

                a="===============ZF02-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + S_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf02)+" permit tcp " + S_ip + " " + D_ip
                zf02=zf02+1
                aa.append(a)
                # ===================================================================
                a="===============ZF01-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + D_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf01)+" permit tcp " + D_ip + " " + S_ip
                zf01=zf01+1
                aa.append(a)
                # =============================================================
                a="===============ZF01-LINK-AS-01/02==============="
                aa.append(a)
                a="ip access-list extended  ZF01-TWIDC-OUT"
                aa.append(a)
                a="   permit tcp " + D_ip + " " + S_ip
                aa.append(a)
                # ==============================================================
                a="===============ZF02-LINK-AS-01/02==============="
                aa.append(a)
                a="ip access-list extended  ZF02-JPIDC-OUT"
                aa.append(a)
                a="   permit tcp " + S_ip + " " + D_ip
                aa.append(a)
            else:
                aa.append("输入IP地址错误！！！！！！！！！！！！！！！")
        else:
            if S_ip.split(".")[1] == "8" and D_ip.split(".")[1] == "8":
                a="===============ZF01-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + S_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf01)+" permit tcp " + S_ip + " " + D_ip + " eq " + D_port
                zf01=zf01+1
                aa.append(a)
                # ============================================================
                a = "===============ZF01-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + D_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf01)+" permit tcp " + D_ip + " eq " + D_port + " " + S_ip
                zf01=zf01+1
                aa.append(a)
            elif S_ip.split(".")[1] == "108" and D_ip.split(".")[1] == "108":
                a="===============ZF02-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + S_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf02)+" permit tcp " + S_ip + " " + D_ip + " eq " + D_port
                zf02=zf02+1
                aa.append(a)
                a = "===============ZF02-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + D_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf02)+" permit tcp " + D_ip + " eq " + D_port + " " + S_ip
                zf02=zf02+1
                aa.append(a)
            elif S_ip.split(".")[1] == "8" and D_ip.split(".")[1] == "108":
                b="===============ZF01-N9K-CS01/02==============="
                aa.append(b)
                b="ip access-list VLAN" + S_Vlan + "-ACL"
                aa.append(b)
                b=     str(zf01)+" permit tcp " + S_ip + " " + D_ip + " eq " + D_port
                zf01=zf01+1
                aa.append(b)
                # =========================================================
                a="===============ZF02-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + D_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf02)+" permit tcp " + D_ip + " eq " + D_port + " " + S_ip
                zf02=zf02+1
                aa.append(a)
                # =============================================================
                a="===============ZF01-LINK-AS-01/02==============="
                aa.append(a)
                a="ip access-list extended  ZF01-TWIDC-OUT"
                aa.append(a)
                a="    permit tcp " + S_ip + " " + D_ip + " eq " + D_port
                aa.append(a)
                # ==============================================================
                a="===============ZF02-LINK-AS-01/02==============="
                aa.append(a)
                a="ip access-list extended  ZF02-JPIDC-OUT"
                aa.append(a)
                a="    permit tcp " + D_ip + " eq " + D_port + " " + S_ip
                aa.append(a)

            elif S_ip.split(".")[1] == "108" and D_ip.split(".")[1] == "8":

                a="===============ZF02-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + S_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf02)+" permit tcp " + S_ip + " " + D_ip + " eq " + D_port
                zf02=zf02+1
                aa.append(a)
                # ===================================================================
                a="===============ZF01-N9K-CS01/02==============="
                aa.append(a)
                a="ip access-list VLAN" + D_Vlan + "-ACL"
                aa.append(a)
                a=     str(zf01)+" permit tcp " + D_ip + " eq " + D_port + " " + S_ip
                zf01=zf01+1
                aa.append(a)
                # =============================================================
                a="===============ZF01-LINK-AS-01/02==============="
                aa.append(a)
                a="ip access-list extended  ZF01-TWIDC-OUT"
                aa.append(a)
                a="    permit tcp " + D_ip + " eq " + D_port + " " + S_ip
                aa.append(a)
                # ==============================================================
                a="===============ZF02-LINK-AS-01/02==============="
                aa.append(a)
                a="ip access-list extended  ZF02-JPIDC-OUT"
                aa.append(a)
                a="    permit tcp " + S_ip + " " + D_ip + " eq " + D_port
                aa.append(a)
            else:
                aa.append("输入IP地址错误！！！！！！！！！！！！！！！")
    def weizhi(lst=None,item=''):
        return [i for i in range(len(lst)) if lst[i]==item]
    cs01="===============ZF01-N9K-CS01/02==============="
    cs02="===============ZF02-N9K-CS01/02==============="
    zf1link="===============ZF01-LINK-AS-01/02==============="
    zf2link="===============ZF02-LINK-AS-01/02==============="
    cs01_wz=weizhi(aa,cs01)
    cs02_wz=weizhi(aa,cs02)
    zf1link_wz=weizhi(aa,zf1link)
    zf2link_wz=weizhi(aa,zf2link)
    p=0
    for c01 in cs01_wz:
        if p==0:
            cc.append(aa[c01])
        p=p+1
        cc.append(aa[c01+1])
        cc.append(aa[c01 + 2])
    q=0
    for c02 in cs02_wz:
        if q==0:
            cc.append(aa[c02])
        q=q+1
        cc.append(aa[c02+1])
        cc.append(aa[c02 + 2])
    # cc.append("="*15)
    f=0
    for zf1l in zf1link_wz:
        if f==0:
            cc.append(aa[zf1l])
        f=f+1
        cc.append(aa[zf1l+1])
        cc.append(aa[zf1l + 2])
    # cc.append("="*15)
    v=0
    for zf2l in zf2link_wz:
        if v==0:
            cc.append(aa[zf2l])
        v=v+1
        cc.append(aa[zf2l+1])
        cc.append(aa[zf2l + 2])
    return cc
if __name__ == "__main__":
    Inside(sip1,dip1,svlan1,dvlan1,dport1,sip2,dip2,svlan2,dvlan2,dport2,sip3,dip3,svlan3,dvlan3,dport3,sip4,dip4,svlan4,dvlan4,dport4)
