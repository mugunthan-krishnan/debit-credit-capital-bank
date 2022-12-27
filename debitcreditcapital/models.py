# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    active_ind = models.BigIntegerField(blank=True, null=True)
    open_dt_tm = models.DateTimeField()
    acct_type = models.CharField(max_length=20)
    close_dt_tm = models.DateTimeField(blank=True, null=True)
    account_balance = models.FloatField()
    acct_no = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Branch(models.Model):
    mgr_ssn = models.ForeignKey('Employee', models.DO_NOTHING, db_column='mgr_ssn', related_name='mgr_e_ssn')
    asst_mgr_ssn = models.ForeignKey('Employee', models.DO_NOTHING, db_column='asst_mgr_ssn', related_name='asst_mgr_e_ssn')
    b_street_addr = models.CharField(max_length=255)
    b_county = models.CharField(max_length=255)
    b_city = models.CharField(max_length=255)
    b_state = models.CharField(max_length=255)
    b_country = models.CharField(max_length=255)
    b_zipcode = models.CharField(max_length=10)
    mgr_start_dt_tm = models.DateTimeField(blank=True, null=True)
    branch_id = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'branch'


class BranchCust(models.Model):
    c_ssn = models.OneToOneField('Customer', models.DO_NOTHING, db_column='c_ssn', primary_key=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'branch_cust'
        unique_together = (('c_ssn', 'branch'),)


class Cards(models.Model):
    active_ind = models.BigIntegerField()
    expire_dt_tm = models.DateTimeField()
    card_type = models.CharField(max_length=20)
    valid_from_dt_tm = models.DateTimeField()
    security_no = models.BigIntegerField()
    cardholder_name = models.CharField(max_length=255)
    acct_no = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='acct_no')
    card_no = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cards'


class Checking(models.Model):
    overdraaft_amt = models.FloatField()
    acct_no = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='acct_no', primary_key=True)

    class Meta:
        managed = False
        db_table = 'checking'


class CustEmployee(models.Model):
    c_ssn = models.OneToOneField('Customer', models.DO_NOTHING, db_column='c_ssn', primary_key=True)
    e_ssn = models.ForeignKey('Employee', models.DO_NOTHING, db_column='e_ssn')

    class Meta:
        managed = False
        db_table = 'cust_employee'
        unique_together = (('c_ssn', 'e_ssn'),)


class Customer(models.Model):
    c_first_name = models.CharField(max_length=255)
    c_last_name = models.CharField(max_length=255)
    c_middle_name = models.CharField(max_length=255)
    active_ind = models.BigIntegerField()
    c_street_addr = models.CharField(max_length=255)
    c_county = models.CharField(max_length=255, blank=True, null=True)
    c_city = models.CharField(max_length=255)
    c_state = models.CharField(max_length=255)
    c_country = models.CharField(max_length=255)
    c_zipcode = models.CharField(max_length=10)
    c_ssn = models.CharField(primary_key=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'customer'


class Dependents(models.Model):
    d_name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=40, blank=True, null=True)
    e_ssn = models.ForeignKey('Employee', models.DO_NOTHING, db_column='e_ssn')

    class Meta:
        managed = False
        db_table = 'dependents'


class Depositor(models.Model):
    access_dt_tm = models.DateTimeField(blank=True, null=True)
    c_ssn = models.OneToOneField(Customer, models.DO_NOTHING, db_column='c_ssn', primary_key=True)
    acct_no = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='acct_no')

    class Meta:
        managed = False
        db_table = 'depositor'
        unique_together = (('c_ssn', 'acct_no'),)


class Deposits(models.Model):
    active_ind = models.BigIntegerField()
    deposit_dt_tm = models.DateTimeField()
    deposit_type = models.CharField(max_length=20)
    maturity_dt_tm = models.DateTimeField()
    interest_freq = models.CharField(max_length=100)
    deposit_amount = models.FloatField()
    deposit_no = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'deposits'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DpstAcct(models.Model):
    deposit_no = models.OneToOneField(Deposits, models.DO_NOTHING, db_column='deposit_no', primary_key=True)
    acct_no = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='acct_no')

    class Meta:
        managed = False
        db_table = 'dpst_acct'
        unique_together = (('deposit_no', 'acct_no'),)


class Employee(models.Model):
    e_first_name = models.CharField(max_length=255, blank=True, null=True)
    e_last_name = models.CharField(max_length=255, blank=True, null=True)
    e_middle_name = models.CharField(max_length=255, blank=True, null=True)
    active_ind = models.BigIntegerField()
    e_street_addr = models.CharField(max_length=255, blank=True, null=True)
    e_county = models.CharField(max_length=255, blank=True, null=True)
    e_city = models.CharField(max_length=255, blank=True, null=True)
    e_state = models.CharField(max_length=255, blank=True, null=True)
    e_country = models.CharField(max_length=255, blank=True, null=True)
    e_zipcode = models.CharField(max_length=10, blank=True, null=True)
    e_designation = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    e_ssn = models.CharField(primary_key=True, max_length=11)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee'


class LoanTaken(models.Model):
    c_ssn = models.OneToOneField(Customer, models.DO_NOTHING, db_column='c_ssn', primary_key=True)
    loan_no = models.ForeignKey('Loans', models.DO_NOTHING, db_column='loan_no')

    class Meta:
        managed = False
        db_table = 'loan_taken'
        unique_together = (('c_ssn', 'loan_no'),)


class Loans(models.Model):
    loan_amt = models.BigIntegerField()
    loan_rpmt_amt = models.BigIntegerField()
    acct_no = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='acct_no')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    loan_no = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'loans'


class MoneyMarket(models.Model):
    interest_rate = models.FloatField()
    acct_no = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='acct_no', primary_key=True)

    class Meta:
        managed = False
        db_table = 'money_market'


class Prsnl(models.Model):
    ssn = models.CharField(primary_key=True, max_length=11)
    username = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    employee = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'prsnl'


class Savings(models.Model):
    interest_rate = models.FloatField()
    acct_no = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='acct_no', primary_key=True)

    class Meta:
        managed = False
        db_table = 'savings'


class TransactionsLog(models.Model):
    active_ind = models.BigIntegerField()
    trans_dt_tm = models.DateTimeField()
    trans_type = models.CharField(max_length=50)
    dr_cr_flag = models.CharField(max_length=50)
    trans_amount = models.BigIntegerField(blank=True, null=True)
    acct_no = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='acct_no')
    trans_code = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'transactions_log'
