from django.conf import settings
from .forms import employeeform
import pdfkit
from django.shortcuts import render

html1='''
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
#a1
{
	margin-left: 150px;
}
#a2
{
	font-size:22px;
}
</style>
</head>
<body>
<center><h3>DCART Logistics PVT. LTD</h3>
<br>
<h2><u>DCART Logistics PVT. LTD<br>New Employee Details Form</u></h2>
</center>
<br><br>
<div class="container">
<table  class="borderless" id="a1">

<tr>
<td id="a2"><b>Name:</b></td><td>
'''

html2='''
</td>
</tr>
<tr>
<td id="a2"><b>Adhaar:</b></td><td>
'''

html3='''
</td>
</tr>
<tr>
<td id="a2"><b>Licence_Number:</b></td><td>
'''

html4='''
</td>
</tr>
<tr>
<td id="a2"><b>RC_Card_No:</b></td><td>
'''

html5='''
</td>
</tr>
<tr>
<td id="a2"><b>Mobile_No:</b></td><td>
'''

html6='''
</td>
</tr>
<tr>
<td id="a2"><b>Current_Address:</b></td><td>
'''

html7='''
</td>
</tr>
<tr>
<td id="a2"><b>Permanent_Address:</b></td><td>
'''

html8='''
</td>
</tr>
<tr>
<td id="a2"><b>Father_spouse_Name:</b></td><td>
'''

html9='''
</td>
</tr>
<tr>
<td id="a2"><b>Address:</b></td><td>
'''

html10='''
</td>
</tr>

</body></html>

'''














