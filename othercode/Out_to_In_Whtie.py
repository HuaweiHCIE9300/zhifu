from othercode import insideip_group

Internet_port = None
def White(times,Internet_address,Intranet_address,allport):
    global  Internet_port
    yongjiu=[]
    if times=="1":
        yongjiu.append("object-group network ServerTemp-To-Internet")
        if Intranet_address.split("/")[-1] == "24":
            yongjiu.append("  network-object " + Intranet_address.split("/")[0] + " 255.255.255.0")
        elif Intranet_address.split("/")[-1] == "32":
            yongjiu.append("  network-object host " + Intranet_address.split("/")[0])
        else:
            yongjiu.append("  network-object host " + Intranet_address)
    else:
        Intranet_address_group_name = insideip_group.Address(Intranet_address)
        if bool(allport) is False:
            Internet_port = "1"
        else:
            all_port = allport.split("/")
        Internet_white_name = Intranet_address_group_name.split("_")[0] + "_Domain_List"
        Internet_port_name = Intranet_address_group_name.split("_")[0] + "_Domain_Port"

        if Internet_address.split(".")[-1] in ["com","net","site","org","co","cn","vip"]:
            yongjiu.append("object network "+Internet_address)
            yongjiu.append("   fqdn "+Internet_address)
            yongjiu.append("object-group network " + Internet_white_name)
            yongjiu.append("  network-object object " + Internet_address)
        else:
            yongjiu.append("object-group network " + Internet_white_name)
            if Internet_address.split("/")[-1] == "24":
                yongjiu.append("  network-object " + Internet_address.split("/")[0] + " 0.0.0.255")
            elif Internet_address.split("/")[-1] == "32":
                yongjiu.append("  network-object host " + Internet_address.split("/")[0])
            else:
                yongjiu.append("  network-object host " + Internet_address)
        if Intranet_address == "1":
            pass
        else:
            yongjiu.append("object-group network " + Intranet_address_group_name)
            if Intranet_address.split("/")[-1] == "24":
                yongjiu.append("  network-object " + Intranet_address.split("/")[0] + " 255.255.255.0")
            elif Intranet_address.split("/")[-1] == "32":
                yongjiu.append("  network-object host " + Intranet_address.split("/")[0])
            else:
                yongjiu.append("  network-object host " + Intranet_address)
        if Internet_port == "1":
            pass
        else:
            yongjiu.append("object-group service " + Internet_port_name + " tcp")
            for port in all_port:
                yongjiu.append("    port-object eq " + port)
        if times == "2":
            yongjiu.append("object-group network Server-To-Internet")
            if Intranet_address.split("/")[-1] == "24":
                yongjiu.append("  network-object " + Intranet_address.split("/")[0] + " 255.255.255.0")
            elif Intranet_address.split("/")[-1] == "32":
                yongjiu.append("  network-object host " + Intranet_address.split("/")[0])
            else:
                yongjiu.append("  network-object host " + Intranet_address)
    return yongjiu

if __name__ == "__main__":
    White(times,internetip,insideip,allport)

