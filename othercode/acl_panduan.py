import time

from othercode import ipaddress
import re

def aclpanduan(qianport,houport,allacl):
    all_data=[]
    b=allacl.splitlines()
    allchange=[]
    allchangelast=[]
    quwww=[]
    for ii in b:
        kk=re.findall(r'(\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+0\.\d{1,3}\.\d{1,3}\.\d{1,3})',ii)
        allfmask={"0.0.0.7":"/29","0.0.0.255":"/24","0.0.0.63":"/26","0.0.0.1":"/31","0.0.0.15":"/28","0.0.0.3":"/30","0.0.31.255":"/19","0.0.255.255":"/16","0.0.0.127":"/25","0.0.0.0":"/32"}
        if bool(kk) is True:
            if len(kk)==1:
                for key,value in allfmask.items():
                    if kk[0].strip().split(" ")[-1] == key:
                        ww=" "+kk[0].strip().split(" ")[0]+value
                        ii=ii.replace(kk[0],ww)
                        # all_data.append(ii)
                        allchange.append(ii)
            elif len(kk)==2:
                for key,value in allfmask.items():
                    if kk[0].strip().split(" ")[-1] == key:
                        ww=" "+kk[0].strip().split(" ")[0]+value
                        ii=ii.replace(kk[0],ww)
                        for key,value in allfmask.items():
                            if kk[1].strip().split(" ")[-1] == key:
                                ww=" "+kk[1].strip().split(" ")[0]+value
                                ii=ii.replace(kk[1],ww)
                                # all_data.append(ii)
                                allchange.append(ii)
        else:
            # all_data.append(ii)
            allchange.append(ii)
    #以上循环实现完成非host的网段的转换，比如“0.0.0.1”装换为31
    for kk in allchange:
        hostkk=re.findall(r'(host\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',kk)
        if len(hostkk)==1:
            ww=hostkk[0].split(" ")[-1]+"/32"
            kk=kk.replace(hostkk[0],ww)
            allchangelast.append(kk)
        elif len(hostkk)==2:
            ww=hostkk[0].split(" ")[-1]+"/32"
            kk=kk.replace(hostkk[0],ww)
            ww=hostkk[1].split(" ")[-1]+"/32"
            kk=kk.replace(hostkk[1],ww)
            allchangelast.append(kk)
        else:
            allchangelast.append(kk)
    # 以上循环实现完成host的地址，比如“host 1.1.1.1”装换为1.1.1.1/32
    for vv in allchangelast:
        www=re.findall(r'\s+(www)',vv)
        if bool(www) is True:
            kk="80"
            vv=vv.replace(www[0],kk)
            quwww.append(vv)
        else:
            quwww.append(vv)

    queq=[]
    for vvv in quwww:
        port_qian=re.findall(r'\s+(eq(\s+\d{2,5})+)\s+10',vvv)
        port_hou=re.findall(r'\s+(eq(\s+\d{2,5})+)$',vvv)
        if bool(port_qian) is True and len(port_qian[0][0].split(" ")) >=3:
            for qian_port in port_qian[0][0].split(" ")[1:]:
                new_port="eq"+" "+qian_port
                ccc=vvv
                vvv=vvv.replace(port_qian[0][0],new_port)
                queq.append(vvv)
                vvv=ccc
        elif bool(port_hou) is True and len(port_hou[0][0].split(" ")) >=3:
            for hou_port in port_hou[0][0].split(" ")[1:]:
                new_port = "eq" + " " + hou_port
                ccc = vvv
                vvv = vvv.replace(port_hou[0][0], new_port)
                queq.append(vvv)
                vvv = ccc
        else:
            queq.append(vvv)
    # qurange=[]
    # for vvvv in queq:
    #     range1=re.findall(r'(range\s+\d{2,5}\s+\d{2,5})',vvvv)
    #     if bool(range1) is True:
    #         first=range1[0].split(" ")[1]
    #         second=range1[0].split(" ")[2]
    #         for seq in range(int(first),int(second)+1):
    #             new_eq="eq "+str(seq)
    #             cccc=vvvv
    #             vvvv=vvvv.replace(range1[0],new_eq)
    #             qurange.append(vvvv)
    #             vvvv=cccc
    #     else:
    #         qurange.append(vvvv)

    b=queq
    if bool(houport) is True:
        try:
            usip = houport.split(",")[0]
            dsip = houport.split(",")[1]
            dport = houport.split(",")[2]
        except Exception as e:
            dport=str(0)
        for i in b:
            if "IP access" in i or bool(i) is False or "permit ip any any" in i or "deny ip any" in i or "udp" in i or "ospf" in i or "icmp" in i or "tcp any any" in i:
                pass
            elif i.strip().split(" ")[2] == "ip":
                data = i.strip().split(" ")
                dst1=ipaddress.Ipsu(dsip)
                src1=ipaddress.Ipsu(usip)
                if data[3] == "any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False:
                    all_data.append("存在其中于第"+data[0]+"条中")
                    all_data.append(i.strip())
                    break
                elif data[4] == "any" and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False:
                    all_data.append("存在其中于第"+data[0]+"条中")
                    all_data.append(i)
                    break
                elif data[3]!="any" and data[4]!="any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False:
                    all_data.append("存在其中于第"+data[0]+"条中")
                    all_data.append(i)
                    break
                else:
                    pass
            elif i.strip().split(" ")[2] == "tcp":
                data = i.strip().split(" ")
                dst1 = ipaddress.Ipsu(dsip)
                src1 = ipaddress.Ipsu(usip)
                if len(data) == 5:
                    if data[3] == "any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False:
                        all_data.append("存在其中于第"+data[0]+"条中")
                        all_data.append(i)
                        break
                    elif data[4] == "any" and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False:
                        all_data.append("存在其中于第"+data[0]+"条中")
                        all_data.append(i)
                        break
                    elif data[3]!="any" and data[4]!="any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False:
                        all_data.append("存在其中于第"+data[0]+"条中")
                        all_data.append(i)
                        break
                    else:
                        pass
                elif len(data) == 7:
                    if data[-2] == "eq":
                        if data[3] == "any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False and data[-1] == dport:
                            all_data.append("存在其中于第"+data[0]+"条中")
                            all_data.append(i)
                            break
                        elif  data[4] == "any" and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False and data[-1] == dport:
                            all_data.append("存在其中于第"+data[0]+"条中")
                            all_data.append(i)
                            break
                        elif data[3]!="any" and data[4]!="any" and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False and dport == data[-1]:
                            all_data.append("存在其中于第"+data[0]+"条中")
                            all_data.append(i)
                            break
                    else:
                        pass
                elif len(data)==8:
                    range1=re.findall(r'(range\s+\d{2,5}\s+\d{2,5})',i)
                    if bool(range1) is True and data[-3]=="range":
                        first=range1[0].split(" ")[1]
                        second=range1[0].split(" ")[2]
                        if bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False and first <= dport <= second:
                            all_data.append("存在其中于第"+data[0]+"条中")
                            all_data.append(i)
                            break
                    elif bool(range1) is True and data[4]=="range":
                        first=range1[0].split(" ")[1]
                        second=range1[0].split(" ")[2]
                        if bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[-1])]) is False and first <= dport <= second:
                            all_data.append("存在其中于第"+data[0]+"条中")
                            all_data.append(i)
                            break
                    else:
                        pass

    elif bool(qianport) is True:
        try:
            usip = qianport.split(",")[0]
            dport = qianport.split(",")[1]
            dsip = qianport.split(",")[2]
        except Exception as e:
            dport = str(0)
        for i in b:
            if "IP access" in i or bool(i) is False or "permit ip any any" in i or "deny ip any" in i or "udp" in i or "ospf" in i or "icmp" in i or "tcp any any" in i:
                pass
            elif i.strip().split(" ")[2] == "ip":
                data = i.strip().split(" ")
                src1=ipaddress.Ipsu(usip)
                dst1=ipaddress.Ipsu(dsip)
                if data[3] == "any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False:
                    all_data.append("存在其中于第" + data[0] + "条中")
                    all_data.append(i)
                    break
                elif data[4]=="any" and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False:
                    all_data.append("存在其中于第" + data[0] + "条中")
                    all_data.append(i)
                    break
                elif data[3] != "any" and data[4]!="any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False:
                    all_data.append("存在其中于第" + data[0] + "条中")
                    all_data.append(i)
                    break
                else:
                    pass
            elif i.strip().split(" ")[2] == "tcp":
                data = i.strip().split(" ")
                src1 = ipaddress.Ipsu(usip)
                dst1 = ipaddress.Ipsu(dsip)
                if len(data) == 5:
                    if data[3] == "any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[-1])]) is False:
                        all_data.append("存在其中于第" + data[0] + "条中")
                        all_data.append(i)
                        break
                    elif data[4] == "any" and data[3] != "any" and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False:
                        all_data.append("存在其中于第" + data[0] + "条中")
                        all_data.append(i)
                        break
                    elif data[3]!="any" and data[4]!="any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[-1])]) is False and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False:
                        all_data.append("存在其中于第" + data[0] + "条中")
                        all_data.append(i)
                        break
                    else:
                        pass
                elif len(data) == 7:
                    if data[4] == "eq":
                        if data[3] == "any" and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[-1])]) is False and data[-2] == dport:
                            all_data.append("存在其中于第" + data[0] + "条中")
                            all_data.append(i)
                            break
                        elif data[4]=="any" and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False and data[-2] == dport:
                            all_data.append("存在其中于第" + data[0] + "条中")
                            all_data.append(i)
                            break
                        elif data[3]!="any" and data[4]!="any" and bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[-1])]) is False and data[-2] == dport:
                            all_data.append("存在其中于第" + data[0] + "条中")
                            all_data.append(i)
                            break
                    else:
                        pass

                elif len(data)==8:
                    range1=re.findall(r'(range\s+\d{2,5}\s+\d{2,5})',i)
                    if bool(range1) is True and data[-3]=="range":
                        first=range1[0].split(" ")[1]
                        second=range1[0].split(" ")[2]
                        if bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[4])]) is False and first <= dport <= second:
                            all_data.append("存在其中于第"+data[0]+"条中")
                            all_data.append(i)
                            break
                    elif bool(range1) is True and data[4]=="range":
                        first=range1[0].split(" ")[1]
                        second=range1[0].split(" ")[2]
                        if bool([i for i in src1 if i not in ipaddress.Ipsu(data[3])]) is False and bool([i for i in dst1 if i not in ipaddress.Ipsu(data[-1])]) is False and first <= dport <= second:
                            all_data.append("存在其中于第"+data[0]+"条中")
                            all_data.append(i)
                            break
                    else:
                        pass
    return all_data
if __name__=="__main__":
    aclpanduan(qianport,houport,allacl)