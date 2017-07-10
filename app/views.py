# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from app.forms import riderform1,zoneform,msgform,riderform2,msgform1
from django.db import models
from .models import riders,Zone,adm
from django.core.mail import send_mail
from django.conf import settings
from django.template import RequestContext
import csv
import codecs
import json
import urllib2
from django.core.exceptions import ValidationError
from django.contrib import messages
#from tablib import Dataset




# Create your views here.
def hello(request):
   
    return render(request,"index1.html",{})

def empl(request):
   
    return render(request,"format.html",{})



def riderinfo(request):
    rider=riderform1()
    if request.method=="POST":
        rider=riderform1(request.POST or None)
        if rider.is_valid():
            instance=rider.save(commit=False)
            name=rider.cleaned_data['name']
            phone=rider.cleaned_data['phone']
            zone=rider.cleaned_data['zone']

            instance.save()
            
            print rider
            return render(request,'thanks.html',{})
    else:
        rider=riderform1()

    context={
    "form3" : rider,
    }
    return render(request,"addriders.html",context)


  
def bulkriderinfo(request):
        if request.POST and request.FILES:
            csvfile = request.FILES['csv_file']
            dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
            csvfile.open()
            reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=str(u';'), dialect=dialect)
            next(reader,None)

            for row in reader:

                print row
                row1 = row[0].split(',')
                if(len((row1[1]))==10):
                    name = riders.objects.create(name=row1[0],phone=int(row1[1]))
                    print name
                    Zone1 = Zone.objects.get(name=row1[2])
                    name.zone = Zone1
                    name.save()

                else:
                    raise ValidationError("Invalid Phone Number")
                    #messages.error(request,"Error!")

        return render(request, "bulkriders.html", locals())    

def send_sms(request):
    msg=msgform()
    if request.method=="POST":
        msg=msgform(request.POST or None)
        if msg.is_valid():
            
            subject=msg.cleaned_data['message']
            phonenumber_list=[]
            Zone=msg.cleaned_data['Zone']
            if not request.POST.get('Select_All_Zones', None) == None:
                for rider in riders.objects.all():
                    #phonenumber_list.append('91'+str(rider.phone))
                    response_json_data = send_sms1(phone_number='91'+str(rider.phone),sms=subject)
                    print response_json_data

            
            
            else:
                for rider in riders.objects.filter(zone=Zone):
                    #phonenumber_list.append('91'+str(rider.phone)) 
                    response_json_data = send_sms1(phone_number='91'+str(rider.phone),sms=subject)
                    print response_json_data
            




            #response_json_data = send_sms1(phone_number=9989817488,sms=subject)
            #print response_json_data
            return render(request,'thanks.html',{})   
          

            

    
        
    context={
    "form4" : msg,
    }
    return render(request,"sendmsg.html",context)


def send_sms1(phone_number, sms):
    if not settings.SEND_SMS:
        return
    '''
    request_params = {'GSM': phone_number,
                      'sender': 'SNDFST',
                      'SMSText': sms,
                      'user': SMS_USER_ID,
                      'password': SMS_PASSWORD
                   }
    '''
    request_body = {}
    authentication ={}
    authentication['username']='dcartlog'
    authentication['password'] = 'PnnqKfP4'
    request_body['authentication']=authentication
    messages = []
    msg_body = {}
    msg_body['sender']='SNDFST'
    msg_body['text'] = sms
    recipients =[]
    recipient_body ={}
    
    #for phone in phone_number:
    recipient_body['gsm'] = phone_number
    recipients.append(recipient_body)
    msg_body['recipients']=recipients
    messages.append(msg_body)
    request_body['messages']=messages
    print request_body
    method='POST'
    url = 'http://193.105.74.159/api/v3/sendsms/json'
   # url = url + urllib.urlencode(request_params)
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url,data=json.dumps(request_body))
    request.add_header("Content-Type", 'application/json')
    # overload the get method function with a small anonymous function...
    request.get_method = lambda: method
    try:
        #response = opener.open(request)
        #response_json_data = json.loads(response.read())
        #return response_json_data
        return True
    except Exception as e:
        return False
        

def send_sms2(request):
    msg=msgform1()
    if request.method=="POST":
        msg=msgform1(request.POST or None)
        if msg.is_valid():
            
            subject=msg.cleaned_data['message']
            phonenumber_list=[]
            for ph in adm.objects.all():
                response_json_data = send_sms1(phone_number='91'+str(ph.phone),sms=subject)
                print response_json_data

            
            
           



            #response_json_data = send_sms1(phone_number=9989817488,sms=subject)
            #print response_json_data
            return render(request,'thanks.html',{})  
    context={
    "form5" : msg,
    }
    return render(request,"sendmsg1.html",context) 