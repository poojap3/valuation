from django.db import models
from django.contrib.auth.models import User



class RoleRef(models.Model):
    user = models.ForeignKey(User,null=True, on_delete= models.CASCADE)
    user_role_name=models.CharField(max_length=50, null=True, blank=True)
    created_timestamp =   models.DateTimeField(auto_now_add=True,verbose_name="Created_Timestamp",blank=True,null=True)

    last_update_timestamp =   models.DateTimeField(auto_now_add=True,verbose_name="Last_Update_Timestamp_Timestamp",blank=True,null=True)




class CustomUser(models.Model):
    user = models.ForeignKey(User,null=True, on_delete= models.CASCADE)
    roleref = models.ForeignKey(RoleRef,null=True, on_delete= models.CASCADE)
    username=models.CharField(max_length=50, null=True, blank=True)
    fullname=models.CharField(max_length=50, null=True, blank=True)
    email= models.EmailField(max_length=50, null=True, blank=True)
    mobile_number= models.CharField(max_length=20, null=True, blank=True)
    dob=models.DateTimeField(auto_now_add=False,verbose_name="Created",blank=True,null=True)
    role=models.CharField(max_length=20, null=True, blank=True)
    terms=models.CharField(max_length=20, null=True, blank=True)

    created_timestamp =   models.DateTimeField(auto_now_add=True,verbose_name="Created_Timestamp",blank=True,null=True)

    last_update_timestamp =   models.DateTimeField(auto_now_add=True,verbose_name= "Last_Update_Timestamp_Timestamp",blank=True,null=True)
     # ^^ this line last update






class Bank(models.Model):
    bank_name=models.CharField(max_length=50, null=True, blank=True)
    branch=models.CharField(max_length=50, null=True, blank=True)
    bank_address=models.CharField(max_length=50, null=True, blank=True)
    bank_city=models.CharField(max_length=50, null=True, blank=True)
    Bank_state=models.CharField(max_length=50, null=True, blank=True)




class VApp(models.Model):
    user=models.ForeignKey(User,null=True, on_delete= models.CASCADE)
    bank=models.ForeignKey(Bank,null=True, on_delete= models.CASCADE)
    case_no=models.CharField(max_length=100, null=True, blank=True)
    case_code=models.CharField(max_length=100, null=True, blank=True)
    case_id=models.CharField(max_length=100, null=True, blank=True)
    case_status=models.CharField(max_length=100, null=True, blank=True)
    loan_type=   models.CharField(max_length=100, null=True, blank=True)
    file_no=models.CharField(max_length=50, null=True, blank=True)
    owner_name=models.CharField(max_length=100, null=True, blank=True)
    owner_phone1=models.CharField(max_length=20, null=True, blank=True)
    owner_phone2=models.CharField(max_length=20, null=True, blank=True)
    owner_address=models.CharField(max_length=100, null=True, blank=True)
    city=models.CharField(max_length=100, null=True, blank=True)
    landmark=models.CharField(max_length=100, null=True, blank=True)
    # googlemapfield
    google_map=models.CharField(max_length=100, null=True, blank=True)

    created =   models.DateTimeField(auto_now_add=True,verbose_name="Created",blank=True,null=True)

    last_update_timestamp =   models.DateTimeField(auto_now_add=True,verbose_name="Last_Update_Timestamp_Timestamp",blank=True,null=True)










class SiteVisit(models.Model):
    user = models.ForeignKey(User,null=True, on_delete= models.CASCADE)
    vapp=models.ForeignKey(VApp,null=True, on_delete= models.CASCADE)
    # issue=models.ForeignKey(Issue,null=True, on_delete= models.CASCADE)
    site_visit_comments=models.CharField(max_length=2000, null=True, blank=True)
    site_visit_status=models.CharField(max_length=20, null=True, blank=True)

    created =   models.DateTimeField(auto_now_add=True,verbose_name="Created",blank=True,null=True)

    last_update_timestamp =   models.DateTimeField(auto_now_add=True,verbose_name="Last_Update_Timestamp_Timestamp",blank=True,null=True)




class FieldReport(models.Model):
    user = models.ForeignKey(User,null=True, on_delete= models.CASCADE)
    # vapp=models.ForeignKey(VApp,null=True, on_delete= models.CASCADE)
    sitevisit=models.ForeignKey(SiteVisit,null=True, on_delete= models.CASCADE)

    fieldreport_location=models.CharField(max_length=2000, null=True, blank=True)
    fieldreport_comment=models.CharField(max_length=2000, null=True, blank=True)
    fieldreport_status=models.CharField(max_length=20, null=True, blank=True)
    Submission_TimeStamp=models.DateTimeField(auto_now_add=False,verbose_name="Created",blank=True,null=True)
    created =   models.DateTimeField(auto_now_add=True,verbose_name="Created",blank=True,null=True)

    last_update_timestamp =   models.DateTimeField(auto_now_add=True,verbose_name="Last_Update_Timestamp_Timestamp",blank=True,null=True)




class Issue(models.Model):
    # user = models.ForeignKey(User,null=True, on_delete= models.CASCADE)
    # vapp=models.ForeignKey(VApp,null=True, on_delete= models.CASCADE)
    field=models.ForeignKey(FieldReport,null=True, on_delete= models.CASCADE)
    issue_name=models.CharField(max_length=200, null=True, blank=True)
    issue_comments=models.CharField(max_length=2000, null=True, blank=True)




#
# class BankSubmission(models.Model):
#     user = models.ForeignKey(User,null=True, on_delete= models.CASCADE)
#     vapp=models.ForeignKey(VApp,null=True, on_delete= models.CASCADE)
#     banksubmission_comments=models.CharField(max_length=2000, null=True, blank=True)
#     created =   models.DateTimeField(auto_now_add=True,verbose_name="Created",blank=True,null=True)
#
#     last_update_timestamp =   models.DateTimeField(auto_now_add=True,verbose_name="Last_Update_Timestamp_Timestamp",blank=True,null=True)
#






class ExcelsheetData(models.Model):
    case_no=models.CharField(max_length=2000, null=True, blank=True)
    case_code=models.CharField(max_length=2000, null=True, blank=True)
    file_no=models.CharField(max_length=2000, null=True, blank=True)
    case_id=models.CharField(max_length=2000, null=True, blank=True)
    case_status=models.CharField(max_length=2000, null=True, blank=True)
    loan_type=models.CharField(max_length=2000, null=True, blank=True)
    name=models.CharField(max_length=2000, null=True, blank=True)
    address=models.CharField(max_length=2000, null=True, blank=True)
    city=models.CharField(max_length=2000, null=True, blank=True)

    phone1=models.CharField(max_length=2000, null=True, blank=True)
    phone2=models.CharField(max_length=2000, null=True, blank=True)
    landmark=models.CharField(max_length=2000, null=True, blank=True)
    # loan_type=models.CharField(max_length=2000, null=True, blank=True)
    # loan_type=models.CharField(max_length=2000, null=True, blank=True)


    class Meta:
        db_table="ExcelsheetData"
