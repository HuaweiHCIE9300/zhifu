from django.shortcuts import redirect, render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from othercode import inside_access
from othercode import Out_to_In_Whtie
from othercode import ipaddress,nat,acl_panduan


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        pass


def Test(request):
    return render(request,"test.html")

def Acl(request):
    if request.method == "GET":
        return render(request, "acl.html")
    elif request.method == "POST":
        sip1 = request.POST.get("sip1")
        dip1 = request.POST.get("dip1")
        dport1 = request.POST.get("sport1")
        if bool(dport1) is False:
            dport1=str(0)
        else:
            dport1=dport1
        #=================================
        sip2 = request.POST.get("sip2")
        dip2=request.POST.get("dip2")
        dport2 = request.POST.get("dport1")
        if bool(dport2) is False:
            dport2=str(0)
        else:
            dport2=dport2
        allacl=request.POST.get("aclall")
        if bool(sip1) is True and bool(dip1) is True and bool(dport1) is True:
            qianport=sip1+","+dport1+","+dip1
            houport=None
        elif bool(sip2) is True and bool(dip2) is True and bool(dport2) is True:
            houport=sip2+","+dip2+","+dport2
            qianport=None
        allpanduan=acl_panduan.aclpanduan(qianport,houport,allacl)
        if bool(allpanduan) is True:
            return render(request,"acl.html",locals())
        elif bool(allpanduan) is False:
            allpanduan="ACL条目中不存在你所要检测的源目IP以及端口信息，需要手动将信息增加到ACL中！！！"
            return render(request,"acl.html",locals())



def Ipsu(request):
    if request.method == "GET":
        return render(request, "ipsu.html")
    elif request.method == "POST":
        ipinfo = request.POST.get("ipinfo")
        if ipinfo.split("/")[-1]=="32":
            lastip=ipinfo.split("/")[0]
            firstip=ipinfo.split("/")[0]
            networkhao=ipinfo.split("/")[0]
            broadcastip=ipinfo.split("/")[0]
            mask=ipinfo.split("/")[-1]
            countip=1
        else:
            allip = ipaddress.Ipsu(ipinfo)
            firstip=allip[1]
            networkhao=allip[0]
            broadcastip=allip[-1]
            if ipinfo.split("/")[-1]!="31":
                lastip=allip[-2]
                firstip=allip[1]
                countip=len(allip)-2
                mask=ipinfo.split("/")[-1]

            else:
                mask=ipinfo.split("/")[-1]
                lastip=allip[-1]
                firstip=allip[0]
                countip=2

        return render(request, "ipsu.html", locals())


def Nat(request):
    if request.method == "GET":
        return render(request, "nat.html")
    else:
        gcp=request.POST.get("gcp")
        tw1=request.POST.get("tw1")
        tw2=request.POST.get("tw2")
        tw3=request.POST.get("tw3")
        jp1=request.POST.get("jp1")
        jp2=request.POST.get("jp2")
        insideip=request.POST.get("insideip")
        insideport=request.POST.get("insideport")
        outsideport=request.POST.get("outsideport")
        fwgroupname=request.POST.get("fwgroupname")
        epxuhao=request.POST.get("epxuhao")
        infoall=nat.Nat(gcp,tw1,tw2,tw3,jp1,jp2,insideip,insideport,outsideport,fwgroupname,epxuhao)

        return render(request,"nat.html",locals())


def White(request):
    if request.method == "GET":
        return render(request, "white.html")
    else:
        times = request.POST.get("optradio")
        internetip = request.POST.get("internetip")
        insideip = request.POST.get("insideip")
        allport = request.POST.get("allport")
        whitec = Out_to_In_Whtie.White(times, internetip, insideip, allport)
        return render(request, "white.html", locals())


def Insideaccess(request):
    if request.method == "GET":
        return render(request, "insideaccess.html")
    else:
        svlan1 = request.POST.get("svlan1")
        dvlan1 = request.POST.get("dvlan1")
        sip1 = request.POST.get("sip1")
        dip1 = request.POST.get("dip1")
        dport1 = request.POST.get("dport1")
        # ===============
        svlan2 = request.POST.get("svlan2")
        if bool(svlan2) is True:
            dvlan2 = request.POST.get("dvlan2")
            sip2 = request.POST.get("sip2")
            dip2 = request.POST.get("dip2")
            dport2 = request.POST.get("dport2")
        else:
            sip2 = dip2 = svlan2 = dvlan2 = dport2 = None
        # ===============
        svlan3 = request.POST.get("svlan3")
        if bool(svlan3) is True:
            dvlan3 = request.POST.get("dvlan3")
            sip3 = request.POST.get("sip3")
            dip3 = request.POST.get("dip3")
            dport3 = request.POST.get("dport3")
        else:
            sip3 = dip3 = svlan3 = dvlan3 = dport3 = None
        # ===============
        svlan4 = request.POST.get("svlan4")
        if bool(svlan4) is True:
            dvlan4 = request.POST.get("dvlan4")
            sip4 = request.POST.get("sip4")
            dip4 = request.POST.get("dip4")
            dport4 = request.POST.get("dport4")
        else:
            sip4 = dip4 = svlan4 = dvlan4 = dport4 = None

        cc = inside_access.Inside(sip1, dip1, svlan1, dvlan1, dport1, sip2, dip2, svlan2, dvlan2, dport2, sip3, dip3,
                                  svlan3, dvlan3, dport3, sip4, dip4, svlan4, dvlan4, dport4)
        return render(request, "insideaccess.html", locals())
