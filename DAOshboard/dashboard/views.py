from audioop import avg
from django.shortcuts import render
from django.http import HttpResponse
from . import covalent


def index(request):
    #have to maually input addresses to work with since the api is slow to call all DAO's 
    #can only call around 1000 inputs at once
    #in the future this project could just call the api and store it in the database and update the api every 
    #10 minutes for example, but i'm not able to afford database storage for a hackathon project atm
    (logo,address,ticker,name) = covalent.get_data()
    add1 = "0x0f5d2fb29fb7d3cfee444a200298f468908cc942"
    add2 = "0x6c2c026a61e0d70ccd1fe3e607ebe4df5a98f174"
    add3 = "0x1170ac7e37a7922e1ffc3c26e23c2afa8e313e87"
    add4 = "0x3e828ac5c480069d4765654fb4b8733b910b13b2"
    add5 = "0x7d2220fa4b36cfb02d5092c5a165356d2d585d87"
    add6 = "0x3472a5a71965499acd81997a54bba8d852c6e53d"
    newaddress = [add1,add2,add3,add4,add5,add6]
    newlogo = []
    newname = []
    transparency = []
    avg = 0
    for x in logo:
        newlogo.append(logo[x])
    for x in name:
        newname.append(name[x])
    #for x in newaddress:
        #transparency.append(covalent.get_transparency(x))
    #for i in range(6):
        #avg += ((transparency[i][newaddress[i]]))
    #avg = avg/(len(transparency))
    avg = 9/6
    context = {'logo':logo, 'address':address, 'ticker':ticker, 'name':name, 'avg':avg, 'transparency':
    transparency, 'newaddress':newaddress, 'add1':add1,'add2':add2, 'add3':add3, 'add4':add4, 'add5':add5,'add6':add6
    }
    return render(request, "dashboard/index.html", context)


def about(request):
    avg = 9/6
    data = {'avg':avg}
    return render(request, "dashboard/about.html", data)

def terms(request):
    avg = 9/6
    data = {'avg':avg}
    return render(request, "dashboard/terms.html", data)


