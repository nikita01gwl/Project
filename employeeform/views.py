# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
import pdfkit
from django.http import HttpResponse
from .forms import employeeform,employeeform1
from django.utils.encoding import smart_str
from .models import employee
from django.db.models import get_model
import os
import errno
from wsgiref.util import FileWrapper
import mimetypes
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def emp_details(request):
    if request.method=="POST":
        emp=employeeform(request.POST or None)
        if emp.is_valid():
            instance=emp.save(commit=False)
            Name=emp.cleaned_data['Name']
            Adhaar =emp.cleaned_data['Adhaar']
            Licence_Number=emp.cleaned_data['Licence_Number']
            RC_Card_No=emp.cleaned_data['RC_Card_No']
            Mobile_No=emp.cleaned_data['Mobile_No']
            Current_Address=emp.cleaned_data['Current_Address']
            Permanent_Address=emp.cleaned_data['Permanent_Address']
            father_spouse_Name=emp.cleaned_data['Father_spouse_Name']
            Address=emp.cleaned_data['Address']

            Employee_Id=emp.cleaned_data['Employee_Id']
            Hub=emp.cleaned_data['Hub']
            Date_of_Joining=emp.cleaned_data['Date_of_Joining']
            Role=emp.cleaned_data['Role']

            instance.save()
            obj = employee.objects.get(Employee_Id=Employee_Id)

            mydir =os.path.join(settings.MEDIA_ROOT,obj.Employee_Id)

          
            try:
                os.makedirs(mydir)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise  # this was not a "directory exist" error..

            filename = "New Employee Form.pdf"
            filepath_name = os.path.join(mydir,filename)

            
            html = ''
            html += html1
            html+=obj.Name.title()
            html += html2
            html+=str(obj.Adhaar)
            html += html3
            html+=str(obj.Licence_Number)
            html += html4
            html+=str(obj.RC_Card_No)
            html += html5
            html+=str(obj.Mobile_No)
            html += html6
            html+=obj.Current_Address
            html += html7
            html+=obj.Permanent_Address
            html += html8
            html+=obj.Father_spouse_Name.title()
            html += html9
            html+=obj.Address
            html += html10
            html += html11
            html+=obj.Name.title()
            html += html12
            html+=str(obj.Mobile_No)
            html += html13
            html+=str(obj.Licence_Number)
            html += html14
            html+=obj.Employee_Id
            html += html15
            html+=obj.Hub.title()
            html += html16
            html+=str(obj.Date_of_Joining)
            html += html17
            html+=obj.Current_Address
            html += html18
            html+=obj.Permanent_Address
            html += html19
            html += html20

            



            pdfkit.from_string(html,filepath_name )

            

            return render(request,'thanks.html',{})
                
            
    else:
        emp=employeeform()

    context={
    "form1" : emp,
    }
    return render(request,"employee-form1.html",context)





def gen_pdf(request):
    if request.method=="POST":
        num=employeeform1(request.POST or None)
        if num.is_valid():
            
            
            
            Id=num.cleaned_data['Enter_Employee_Id']
            obj = employee.objects.get(Employee_Id=Id)
            
            return HttpResponseRedirect(obj.get_absolute_url())
            print 1

            
    else:
        num=employeeform1()

    context={
    "form2" : num,
    }
    return render(request,"employee-form2.html",context)


def download(request,Id=None):
    items = ['New Employee Form.pdf','New Employee Form1.pdf','New Employee Form2.pdf']
    
    file_path=os.path.join(settings.MEDIA_ROOT,Id,'New Employee Form.pdf')
    #file_path = settings.MEDIA_ROOT +'/'+ filepath_name1
    # fname="New Employee Form.pdf"
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = smart_str(file_path)
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s'%smart_str('New Employee Form.pdf') 
    #print type(response)
    #print response
    return response






html1='''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<style type="text/css">

.borderless td, .borderless td .borderless tr 
{
    border: none;
}
#a1
{
    
}
#a2
{
    font-size:22px;padding-top: 20px;height:80px;width:200px;
}
#a3
{
    font-size:22px;padding-top: 20px;height:80px;
}
#a4
{
    font-size:22px;height:80px;width:200px;
}
#a5
{
    font-size:22px;height:80px;

}
</style>
</head>
<body>
<center>
<h2><u><b>DCART Logistics PVT. LTD<br>New Employee Details Form</b></u></h2>
</center>
<br><br>
<div class="container">
<table  class="borderless" id="a1">
<thead>
<tr>
<td id="a4">Name</td><td id="a5">:</td><td id="a5"style="padding-left:40px;">
'''

html2='''
</td>
</tr>
<tr>
<td id="a2">Adhaar</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html3='''
</center></td>
</tr>
<tr>
<td id="a2">Licence Number</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html4='''
</center></td>
</tr>
<tr>
<td id="a2">RC Card No</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html5='''
</center></td>
</tr>
<tr>
<td id="a2">Mobile No</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html6='''
</center></td>
</tr>
<tr>
<td id="a2">Current Address</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html7='''
</center></td>
</tr>
<tr>
<td id="a2">Permanent Address</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html8='''
</center></td>
</tr>
<tr>
<td id="a2">father/spouse Name</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html9='''
</center></td>
</tr>
<tr>
<td id="a2">Address</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html10='''
</center></td>
</tr></table></div><center>
<br><br><br><br><br><br><br><br><br><br><br><br><br><b>Page 1 Of 2</b></center>
</body></html>

'''

html11='''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<style type="text/css">

.borderless td, .borderless td .borderless tr 
{
    border: none;
}
#a1
{
    
}
#a2
{
    font-size:22px;padding-top: 20px;height:80px;width:200px;
}
#a3
{
    font-size:22px;padding-top: 20px;height:80px;
}
#a4
{
    font-size:22px;height:80px;width:200px;
}
#a5
{
    font-size:22px;height:80px;

}
#a6
{
    font-size:22px;
}
#a7
{
    font-size:22px;
}
#a8
{
    margin-left: 150px;
}
#a9
{
    height:40px;
}
#a10
{
    margin-top:110px;
}
</style>
</head>
<body>
<center>
<font size="6px"><u><b>SENDFAST Employee Detail Form</b></u></font>
</center>
<br><br>
<div class="container">
<table  class="borderless" id="a1" >
<thead>
<tr id="a9">
<td id="a4">Name&ensp;</td><td id="a5">:</td><td id="a5"style="padding-left:40px;">
'''

html12='''
</center></td>
</tr>
<tr>
<td id="a2">Mobile Number</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html13='''
</center></td>
</tr>
<tr>
<td id="a2">Licence Number</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html14='''
</center></td>
</tr>
<tr>
<td id="a2">Employee Id</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html15='''
</center></td>
</tr>
<tr>
<td id="a2">Hub</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html16='''
</center></td>
</tr>
<tr>
<td id="a2">Date Of Joining</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html17='''
</center></td>
</tr>
<tr>
<td id="a2">Current Address</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html18='''
</center></td>
</tr>
<tr>
<td id="a2">Permanent Address</td><td id="a3">:</td><td id="a3"style="padding-left:40px;">
'''

html19='''
</center></td>
</tr></thead>
</table></div><br><br><br><br>
<div class="container">
<table  class="borderless" id="a1"><thead>
<tr>

<td id="a2"style="width:600px;">
DCART Logistics Private Limited
<br>
Hyderabad
</td>
<td id="a2">
Name
<br>
Signature
</tr>
</table><br><br>
<div id="a10">
<hr style="height:2px;background-color:black;">

<center>
<font size="4px">Corporate Office:H No:-8-2-248/A/5/30&31,Venkateshwara Hills Colony Road No. 3 <br>Banajara Hills,Hyderabad

Office Number:040 23351333
<br/>www.sendfast.in

</b></div>
</body></html>
'''

html20='''

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<style type="text/css">
.borderless td, .borderless td .borderless tr 
{
    border: none;
}
#a1
{
    
}
#a2
{
    
}
#a3
{
    
}
#a4
{
    margin-top: 30px;
}





</style>
</head>
<body>
<center><h3><b>DCART Logistics PVT. LTD</b>
<br></h3></center><br><br>
<div class="container"><p>
As an Employee at DCART LOGISTICS PVT. LTD. I shall abide by the below mentioned rules:<br/></p>
<ul >
<li >

 I will wear a proper uniform at all times i.e a Denim, shoes, Helmet along with the T-shirt/Over

Coat provided to me by DCART.</li>
<li >
I will not misbehave with any individual involved with DCART as a Merchant, Customer, or

Employee.</li>
<li >

 I will not be engaged in any illegal or indecent activity that might bring bad repute to the firm.
</li><li>
 I will Responsibly keep any inventory provided by DCART or their clients (MOBILE, TSHIRT, BAG or

anything as such) and boot cash in good care.
</li><li>
 DCART will not be responsible for any activity during my non-working hours and is not liable for

scrutiny.
</li><li>
 I will be an an obedient and sincere employee of DCART and I shall not be part of any unions.
</li><li>
 DCART reserves the right to cut the incentives of any particular date if I am found dressed

inappropriately.
</li><li>
 I am completely responsible for the loss of any valuable item given to me for delivery. the amount
of which can be deducted from my salary. Incase of suspicion, I can be produced in the nearest

police station.
</li><li>
 If i am found guilty/suspected of conducting any illegal activity, i am solely responsible for it, all

other employees of DCART shall be treated as innocent

unless they are involved in the activity and I can be deported at the nearest police station.</li>

</ul><center>Upon failing to obey the above rules, the management can relieve me of my duties with

immediate effect and can claim for loss of inventory and money.</center>

<br>
<br>

<table class="borderless" id="a3"  >

<tr><td>

Name</td><td>:&ensp;</td></td><td><hr id="a4" style="height:2px;background-color:black;width:300px;"></td>
<tr><td>

Signature</td><td>:&ensp;</td></td><td><hr id="a4" style="height:2px;background-color:black;width:300px;"></td>

<tr><td>
Date</td><td>:&ensp;</td></td><td><hr id="a4" style="height:2px;background-color:black;width:300px;"></td></tr>
</div></b></body></html>

'''


