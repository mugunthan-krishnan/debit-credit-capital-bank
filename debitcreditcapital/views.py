from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from .models import Prsnl, Accounts, Depositor, Loans, Deposits, DpstAcct, Cards

# Create your views here.

def landingpage(request):
  template = loader.get_template('LandingPage.html')
  return HttpResponse(template.render({},request))

def loginvalidation(request):
  if request.method == 'POST':
    un = request.POST.get('username')
    password = request.POST.get('password')
    emp = request.POST.get('employee')
    if emp == None:
      emp = 0
    else:
      emp = 1

    users = Prsnl.objects.filter(username=un,passwd=password, employee=emp).values()
    if users and emp == 0:
      return customer(request, users, un)
    elif users and emp == 1:
      return addcustomer(request, users, un)
    else:
      error = 'invalidlogin'
      context = {
      'errors': error
      }
      return render(request, 'LandingPage.html', context=context)

def customer(request, users, un):
  if request.method == 'POST':
    if users:
      curuser = users[0]['ssn']
      curusername = un
      curuser_acct = Depositor.objects.filter(c_ssn=curuser).values()
      accounts = Accounts.objects.filter(acct_no=curuser_acct[0]['acct_no_id']).values()
      loans = Loans.objects.filter(acct_no=curuser_acct[0]['acct_no_id']).values()
      if not loans:
        loanmessage = "No active loan accounts."
      
      dpst_acct = DpstAcct.objects.filter(acct_no=curuser_acct[0]['acct_no_id']).values()
      deposits = Deposits.objects.filter(deposit_no=dpst_acct[0]['deposit_no_id']).values()
      if not deposits:
        depositmessage = "No active deposit accounts."
      else:
        depositmessage = ""

      cards = Cards.objects.filter(acct_no=curuser_acct[0]['acct_no_id']).values()
      if not cards:
        cardmessage = "No active cards issued."
      else:
        cardmessage = ""

      context = {
      'user': users,
      'accounts': accounts,
      'loans': loans,
      'deposits': deposits,
      'cards': cards,
      'username': curusername,
      'loanmessage': loanmessage,
      'depositmessage': depositmessage,
      'cardmessage': cardmessage,
      }
      template = loader.get_template('CustomerView.html')
      return HttpResponse(template.render(context, request))

def logout(request):
  template = loader.get_template('LogoutPage.html')
  return HttpResponse(template.render({}, request))

def addcustomer(request, users, un):
  template = loader.get_template('AddCustomer.html')
  if users:
    context = {
    'empusername': un
    }
    if request.method == 'POST':
      firstname = request.POST.get('firstname')
      middlename = request.POST.get('middlename')
      lastname = request.POST.get('lastname')
      ssn = request.POST.get('ssn')
      streetaddr = request.POST.get('streetaddr')
      city = request.POST.get('city')
      state = request.POST.get('state')
      country = request.POST.get('country')
      zipcode = request.POST.get('zipcode')

      if firstname and lastname and middlename and ssn and streetaddr and city and country and state and zipcode:
        insertQuery = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        parameters = (firstname,lastname,middlename,1,streetaddr,"ZZCounty",city,state,country,zipcode,ssn)
        with connection.cursor() as cursor:
          cursor.execute(insertQuery, parameters)
          cursor.execute("commit")

    return HttpResponse(template.render(context, request))

def addconfirmation(request):
  template = loader.get_template('Confirmation.html')
  return HttpResponse(template.render({}, request))