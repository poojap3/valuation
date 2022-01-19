from django.urls import path, include
from ValuationApp.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views




app_name = 'ValuationApp'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),


    path('signup/', SignupApi.as_view()),
    path('login/', LoginView.as_view(), name="LOGIN"),
    path('vapp/', VAppAPIView.as_view(), name="VALUATIONAPPLICATION"),
    path('sitevisit/', SiteVisitAPIView.as_view(), name="SITEVISIT"),
    path('roleref/', RoleRefAPIView.as_view(), name="ROLEREF"),
    path('fieldreport/', FieldReportAPIView.as_view(), name="FIELDREPORT"),
    path('register/', RegistrationAPIView.as_view(), name="REGISTER"),


    path('bank/', BankAPIView.as_view(), name="BANK"),

    path('issue/', IssueAPIView.as_view(), name="ISSUE"),

    path('change_password/', ChangePassword.as_view()),
    # path('vappTAT/', VAppTATAPIView.as_view(), name="BANK"),
    # path('vappcount/', VAppCountAPIView.as_view(), name="VAPPCOUNT"),
    #
    # path('sitevisitecount/', SiteVisitCountAPIView.as_view(), name="SITEVISITECOUNT"),
    #


    path('forgot_password_otp/',ForgotPassword_send_otp.as_view()),
    path('otp_Verification_forgot/',OTP_Verification_forgotpassAPIView.as_view()),
    path('forgot_password_update/', ForgotPasswordUpdate.as_view()),
    path('logout/',LogoutAPIView.as_view()),
    path('excel/',UploadExcel.as_view()),
    path('profile',ProfileAPIView.as_view()),
    path('vappshow/',   VAppShowAPIView.as_view()),
    path('sitevisitshow/',   SiteVisitShowAPIView.as_view()),
    path('fieldreportshow/',   FieldReportShowAPIView.as_view()),
    path('issueshow/',   IssueShowAPIView.as_view()),
    path('vapTAT/',   VAppTATAPIView.as_view()),
    path('profile/',   ProfileAPIView.as_view()),







]
