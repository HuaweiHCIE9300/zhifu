def Address(address):
    if address.split(".")[1] == "8":
        ZF_Bigdata_InHost_List = ['10.8.28.0/24', '10.8.29.0/24', '10.8.30.0/24', '10.8.31.0/24',
                                  'ZF_Bigdata_InHost_List']
        Ansible_InHost_List = ['Ansible_InHost_List']
        Jumperserver_Inhost_List = ['Jumperserver_Inhost_List']
        DCYW_InHost_List = ['10.8.64.0/24', '10.8.65.0/24', '10.8.66.0/24', '10.8.67.0/24', '10.8.68.0/24',
                            '10.8.69.0/24',
                            '10.8.70.0/24', '10.8.71.0/24', '10.8.72.0/24', '10.8.73.0/24', '10.8.74.0/24',
                            '10.8.75.0/24',
                            '10.8.76.0/24', '10.8.77.0/24', '10.8.78.0/24', '10.8.79.0/24', 'DCYW_InHost_List']
        EXCW_InHost_List = ['10.8.32.0/24', '10.8.33.0/24', '10.8.34.0/24', '10.8.35.0/24', '10.8.36.0/24',
                            '10.8.37.0/24',
                            '10.8.38.0/24', '10.8.39.0/24', 'EXCW_InHost_List']
        ZFYW_InHost_List = ['10.8.96.0/24', '10.8.97.0/24', '10.8.98.0/24', '10.8.99.0/24', '10.8.100.0/24',
                            '10.8.101.0/24', '10.8.102.0/24', '10.8.103.0/24', '10.8.104.0/24', '10.8.105.0/24',
                            '10.8.106.0/24', '10.8.107.0/24', '10.8.108.0/24', '10.8.109.0/24', '10.8.110.0/24',
                            '10.8.111.0/24', '10.8.112.0/24', '10.8.113.0/24', '10.8.114.0/24', '10.8.115.0/24',
                            '10.8.116.0/24', '10.8.117.0/24', '10.8.118.0/24', '10.8.119.0/24', '10.8.120.0/24',
                            '10.8.121.0/24', '10.8.122.0/24', '10.8.123.0/24', 'ZFYW_InHost_List']
        ZFCW_InHost_List = ['10.8.160.0/24', '10.8.161.0/24', '10.8.162.0/24', '10.8.163.0/24', '10.8.164.0/24',
                            '10.8.165.0/24', '10.8.166.0/24', '10.8.167.0/24', '10.8.168.0/24', '10.8.169.0/24',
                            '10.8.170.0/24', '10.8.171.0/24', '10.8.172.0/24', '10.8.173.0/24', '10.8.174.0/24',
                            '10.8.175.0/24', '10.8.242.0/24','ZFCW_InHost_List ']
        DNSNTP_InHost_List = ['DNSNTP_InHost_List']
        all_address = (ZF_Bigdata_InHost_List, Ansible_InHost_List, Jumperserver_Inhost_List, DCYW_InHost_List,
                       EXCW_InHost_List, ZFYW_InHost_List, ZFCW_InHost_List, DNSNTP_InHost_List)
        address1 = address.split("/")[0].split(".")[0] + "." + address.split("/")[0].split(".")[1] + "." + \
                   address.split("/")[0].split(".")[2]
        for i in range(0, len(all_address)):
            for address in all_address[i]:
                if address1 in address:
                    return all_address[i][-1]
    elif address.split(".")[1] == "108":
        AnQiShi_InHost_List= ['AnQiShi_InHost_List']
        Alarm_InHost_List = ['Alarm_InHost_List']
        Ansible_InHost_List = ['Ansible_InHost_List']
        Jumperserver_Inhost_List = ['Jumperserver_Inhost_List']
        DCYW_InHost_List = ['DCYW_InHost_List', '10.108.64.0/24', '10.108.65.0/24', '10.108.66.0/24', '10.108.67.0/24',
                            '10.108.68.0/24', '10.108.69.0/24', '10.108.70.0/24', '10.108.71.0/24', '10.108.72.0/24',
                            '10.108.73.0/24', '10.108.74.0/24', '10.108.75.0/24', '10.108.76.0/24', '10.108.77.0/24',
                            '10.108.78.0/24', '10.108.79.0/24']
        EXCYW_InHost_List = ['EXCYW_InHost_List', '10.108.32.0/24', '10.108.33.0/24', '10.108.34.0/24',
                             '10.108.35.0/24', '10.108.36.0/24', '10.108.37.0/24', '10.108.38.0/24', '10.108.39.0/24']
        ZFYW_InHost_List = ['ZFYW_InHost_List', '10.108.96.0/24', '10.108.97.0/24', '10.108.98.0/24', '10.108.99.0/24',
                            '10.108.100.0/24', '10.108.101.0/24', '10.108.102.0/24', '10.108.103.0/24',
                            '10.108.104.0/24', '10.108.105.0/24', '10.108.106.0/24', '10.108.107.0/24',
                            '10.108.108.0/24', '10.108.109.0/24', '10.108.110.0/24', '10.108.111.0/24',
                            '10.108.112.0/24', '10.108.113.0/24', '10.108.114.0/24', '10.108.115.0/24',
                            '10.108.116.0/24', '10.108.117.0/24', '10.108.118.0/24', '10.108.119.0/24',
                            '10.108.120.0/24', '10.108.121.0/24', '10.108.122.0/24', '10.108.123.0/24',
                            '10.108.124.0/24']
        ZABBIX_InHost_List = ['ZABBIX_InHost_List']
        DNSNTP_InHost_List = ['DNSNTP_InHost_List']
        YWPlatformGitlab_InHost_List = ['YWPlatformGitlab_InHost_List']
        all_address = (AnQiShi_InHost_List, Ansible_InHost_List, Jumperserver_Inhost_List, DCYW_InHost_List,
                       EXCYW_InHost_List, ZFYW_InHost_List, ZABBIX_InHost_List, DNSNTP_InHost_List, Alarm_InHost_List,
                       YWPlatformGitlab_InHost_List)
        address1 = address.split("/")[0].split(".")[0] + "." + address.split("/")[0].split(".")[1] + "." + \
                   address.split("/")[0].split(".")[2]
        for i in range(0, len(all_address)):
            for address in all_address[i]:
                if address1 in address:
                    return all_address[i][0]
    else:
        pass


if __name__ == "__main__":
    add = input("Please input a ip address:")
    Address(add)
