
from num2words import num2words
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from django.conf import settings
from email.MIMEText import MIMEText
from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives




html1= '''

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<style type="text/css">
	
.borderless td, .borderless th .borderless tr 
{
    border: none;
}

body 
{ 
  
  text-align: center;  
} 

#a1
{
	width:300px;text-align: left;font-size: 17px;border:2px solid black;
}
#a2
{
	width:100px;font-size: 17px;border:2px solid black;
}
#a3
{
	width:100px;font-size: 17px;border:2px solid black;text-align: right;
}
#a12
{
	width:100px;font-size: 17px;border:2px solid black;text-align: right;vertical-align:top;
}
#a4
{
	width:300px;height:100px;text-align: left;vertical-align:top;font-size: 17px;border:2px solid black;
}
#a5
{
	text-align: left;
}
#a6
{
	margin-bottom: 0px;
}
#a7
{
	height:2px;background-color:#000;margin-left:2px;margin-top:0px;width:805px;
}
#a8
{
	height:2px;background-color:#000;margin-left:2px;margin-top:0px;width:805px;margin-bottom: 0px
}
#a9
{
	width:320px;
}
#a10
{
	margin-left:185px;vertical-align:top;margin-top:10px;
}
#a11
{
	margin-right: 2px;
		margin-bottom: 10px;
		margin-left: 60px;
		margin-top: 90px;
}


</style>


</head>
<body id="a11">


<div class="row">

<table class="borderless">
<tr>
<td style="vertical-align:top;">
<img src="C:/Users/hello/Desktop/project/SFLOGO hd.jpg" height="90" width="150" >
</td>
<td id="a10"><h2><b>
DCART LOGISTICS PVT LTD</b><br></h2>
		<h4 ><b>Plot no.30,31,Journalist Colony,Sri Venkateshwara Hills Colony,<br/>&emsp;&emsp;<span style="margin-left:-40px";>Road No. 3,Banjara Hills,Hyderabad,Phone No. 040- 23351333</span></b></h4>

		<br>
		<align="center">
		<h4><b>Pay Slip For

'''


html2 = '''
<br></b></h5><h4><b>
'''

html3='''
</b></h4>




		


</td>
</tr>
</table>

</div>

<div ><hr id="a8"></div>

		<div >
			<table  class="borderless" style="font-size: 15px">
				<thead>
				<tr>
				<th>Employee ID  <th id="a9">:&emsp;
'''

html4='''
</th></th>
				<th >PF Account No.  &thinsp;&thinsp;&thinsp;     <th>:&emsp;
'''
html5='''
</th></th>
				</tr>
				<tr >
				<th>Department &thinsp;&thinsp;&thinsp;     <th id="a9">:&emsp;
'''

html6='''
</th></th>
				<th>EPF UAN No.   <th>:&emsp;
'''
html7='''
</th></th>
				</tr><tr>
				<th>Date Of Join<th id="a9">:&emsp;
'''
html8='''
</th></th>
				<th>ESIC No.      <th>:&emsp;
'''
html9='''
</th></th>

				</tr><tr>
				<th>Total Days       <th id="a9">:&emsp; 
'''
html10='''
</th></th>
				<th>Income Tax No.   <th>: &emsp;
'''
html11='''
</th></th>
				</tr><tr>
				<th>Designation  <th id="a9">:&emsp;
'''
html12='''
</th></th>
				<th>Bank Details,IFSC Code<th>:&emsp;
'''

html21='''
,
'''

html13='''
</th></th>

				</tr>
				<tr>
				
				</tr>
				</thead>
			</table>
		</div>

	

	
<div ><hr id="a7"></div>
<table id="a6">

<tr>
<td  id="a1">
<b>&ensp;Attendance Details</b>
</td>
<td id="a2"><b>Days</b></td>
</tr>
<tr>
<td id="a1">
&ensp;Present
</td>
<td id="a3">
'''

html14='''
&thinsp;</td>
</tr>
</table>


<table style="margin-top: -3px;">

<tr>
<td id="a1">
<b>&ensp;Earnings</b>
</td>
<td id="a2"><b>Amount</b></td>
<td id="a1"><b>&ensp;Deductions</b></td>
<td id="a2"><b>Amount</b></td>
</tr>
<tr style="margin-top: 0px">
<td id="a1">
&ensp;Basic<br/>
&ensp;HRA<br/>
&ensp;Conveyance<br/>
&ensp;Special Allowance<br/>
&ensp;Incentive<br/>
</td>
<td id="a3">
'''
html15='''
&thinsp;<br/>
'''
html16='''
&thinsp;<br/>
<td id="a4">
&ensp;Provident Fund<br/>
&ensp;ESI<br/>
&ensp;Professional Tax<br/>
&ensp;Salary Advance/others
</td>
<td id="a12">
'''
html17='''
&thinsp;
</td>
</tr>

<tr>
<td id="a1">
<b>&ensp;Total Earnings</b>
</td>
<td id="a3"><b>
'''
html18='''
&thinsp;</b></td>
<td id="a1">
<b>&ensp;Total Deductions</b>
</td>
<td id="a3">
<b>
'''

html19='''
&thinsp;</b>
</td>
</tr>
<tr>
<td id="a1">
<b></b>
</td>
<td id="a2"><b></b></td>


<td id="a1">
<b>&ensp;Net Amount</b>
</td>
<td id="a3"><b>
'''

html20='''
&thinsp;</b></td>
</tr>
</table>

<p id="a5">
<u>Amount (In Words):<br/></u>
'''

html22='''
rupees only </p>
<center>This is a computer generated slip</center>
		


</div>
</div></div>


</body>

'''
subject='''Payslip for the month'''


def excel_to_html(details):
    html = ''
    html += html1
    html+= details[3].title()
    html += html2
    html+= details[2].title()
    html += html3
    html+= details[0]
    html += html4
    html+= details[7]
    html += html5
    html+= details[1]
    html+= html6
    html+= details[8]
    html+= html7
    html+= details[4]
    html+= html8
    html+= details[9]
    html+= html9
    html+= details[5]
    html+= html10
    html+= details[10]
    html+= html11
    html+= details[6]
    html+= html12
    html+= details[11]
    html+= html21
    html+= details[12]
    html+= html13
    html+= details[13]
    html+= html14
    html+= details[14]
    html+= html15
    html+= details[15]
    html+= html15
    html+= details[16]
    html+= html15
    html+= details[17]
    html+= html15
    html+= details[18]
    html+= html16

    html+= details[19]
    html+= html15
    html+= details[20]
    html+= html15
    html+= details[21]
    html+= html15
    html+= details[22]
    html+= html17

    html+= details[23]
    html+= html18
    html+= details[24]
    html+= html19
    html+= details[25]
    html+= html20
    html+= num2words(float(details[25])).title()
    html+= html22
    return html

def send_mail(email_id,file_path,filename,details):

	me = settings.EMAIL_HOST_USER
	my_password = settings.EMAIL_HOST_PASSWORD
	you = email_id
	text="Dear %s,\n\n\nPlease find the attachment(s) below."%details[2].title()

	# text_content = 'This is an important message.'
	# html_content = '<p>This is an <strong>important</strong> message.</p>'

	# msg = EmailMultiAlternatives(subject, text_content, me, [you])
	# msg.attach_alternative(html_content, "text/html")
	
	
	msg = MIMEMultipart('mixed')
	msg['Subject'] = "DCart Pay Slip for the month of %s"%details[3]
	msg['From'] = settings.EMAIL_HOST_USER
	msg['To'] = you

	msg.attach( MIMEText(text) )

	

	part = MIMEBase('application', "octet-stream")
	fp = open(file_path, "rb")
	part.set_payload(fp.read())
	fp.close()
	
	
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename=%s'%filename)
	
	msg.attach(part)

	
	s = smtplib.SMTP_SSL('smtp.gmail.com')
	
	s.login(me, my_password)

	s.sendmail(me, you, msg.as_string())
	s.quit()

 

