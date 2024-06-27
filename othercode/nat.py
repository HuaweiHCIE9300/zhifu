def Nat(gcp, tw1, tw2, tw3, jp1, jp2, insideip, insideport, outsideport, fwgroupname, epxuhao):
    infoall = []
    if bool(tw1) is True and bool(tw2) is True and bool(tw3) is True:
        Area = "1"
        jp1=0
    elif bool(jp1) is True and bool(jp2) is True:
        Area="2"
    else:
        Area="1"
    GCP = gcp
    if Area == "1":
        ISP1 = tw1
        ISP2 = tw2
        ISP4 = tw3
        Inside_address = insideip
        Inside_port = insideport
        Outside_port = outsideport
        Out_Object_group_name = fwgroupname
        seq11 = epxuhao
        infoall.append("object network obj-" + Inside_address + "-" + Inside_port + "-ISP1")
        infoall.append("   host " + Inside_address)
        infoall.append("   nat (inside,ISP1) static " + ISP1 + " service tcp " + Inside_port + " " + Outside_port)

        infoall.append("object network obj-" + Inside_address + "-" + Inside_port + "-ISP2")
        infoall.append("   host " + Inside_address)
        infoall.append("   nat (inside,ISP2) static " + ISP2 + " service tcp " + Inside_port + " " + Outside_port)

        infoall.append("object network obj-" + Inside_address + "-" + Inside_port + "-ISP3")
        infoall.append("   host " + Inside_address)
        infoall.append("   nat (inside,ISP3) static " + ISP4 + " service tcp " + Inside_port + " " + Outside_port)
        infoall.append(
            "access-list OUT-TO-IN extended permit tcp object-group " + Out_Object_group_name + " host " + Inside_address + " eq " + Inside_port)
        if GCP == "1":
            infoall.append("==========================C_TWIDC_EP_DS01_C38-DS01/02===================================")
            infoall.append("ip route vrf GCP " + Inside_address + " 255.255.255.255 10.251.104.4 name TO-ZF01")
            infoall.append("ip prefix-list Static_to_OSPF200 seq " + seq11 + " permit " + Inside_address + "/32")
            infoall.append("==========================TWIDC_EP_FW_01/02_FRP4110-MGT===================================")
            infoall.append("object-group network ZF-InHost-WhiteList")
            infoall.append("   network-object host " + Inside_address)
        else:
            pass
    else:
        ISP1 = jp1
        ISP2 = jp2
        Inside_address = insideip
        Inside_port = insideport
        Outside_port = outsideport
        Out_Object_group_name = fwgroupname
        seq11 = epxuhao
        infoall.append("object network obj-" + Inside_address + "-" + Inside_port + "-ISP1")
        infoall.append("   host " + Inside_address)
        infoall.append("   nat (inside,ISP1) static " + ISP1 + " service tcp " + Inside_port + " " + Outside_port)

        infoall.append("object network obj-" + Inside_address + "-" + Inside_port + "-ISP2")
        infoall.append("   host " + Inside_address)
        infoall.append("   nat (inside,ISP2) static " + ISP2 + " service tcp " + Inside_port + " " + Outside_port)

        infoall.append(
            "access-list OUT-TO-IN extended permit tcp object-group " + Out_Object_group_name + " host " + Inside_address + " eq " + Inside_port)
        if GCP == "1":
            infoall.append("==========================C_JPIDC_EP_DS01_C93-DS01/02===================================")
            infoall.append(
                "ip route vrf GCP " + Inside_address + " 255.255.255.255  10.251.114.4 name TO-ZF02-JPIDC-API")
            infoall.append("ip prefix-list Static_to_OSPF200 seq " + seq11 + " permit " + Inside_address + "/32")
            infoall.append("==========================JPIDC_EP_FW_01/02_FRP4110-MGT===================================")
            infoall.append("object-group network ZF-InHost-WhiteList")
            infoall.append("   network-object host " + Inside_address)
        else:
            pass
    return infoall

if __name__ == "__main__":
    Nat(gcp, tw1, tw2, tw3, jp1, jp2, insideip, insideport, outsideport, fwgroupname, epxuhao)
