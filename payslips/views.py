from django.shortcuts import render
import csv
import codecs
from api import excel_to_html,send_mail
from smtplib import SMTPException

import pdfkit
from num2words import num2words
import errno
import os
from datetime import datetime
from django.http import BadHeaderError


# Create your views here.
def load_data(request):

    if request.POST and request.FILES:


        try:
            
            csvfile = request.FILES['csv_file']
            
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect,delimiter=',')

            


            next(reader)
            
            mydir = os.path.join(os.getcwd(),'static',datetime.now().strftime('%Y-%m-%d'))
            
            try:
                os.makedirs(mydir)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise  # This was not a "directory exist" error..

            for row in reader:
                #print row
                a= excel_to_html(row)
                filename = str(row[0])+".pdf"
                filepath_name = os.path.join(mydir,filename)


                pdfkit.from_string(a, filepath_name)



                   
                
                if(len(row[26])!=0):
                    try:


                        send_mail(row[26],filepath_name,filename,row)

                    except SMTPException as e:

                        print('There was an error sending an email: ', e) 
                        pass

                else:
                    print "%s EMail is empty"%(row[2])

                        
        except:
            return render(request, "error.html", locals())  
    return render(request, "payslip-hello.html", locals())  

    



   
    



 
