from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib import auth
import random
from .backends import *


#
# class SignupApi(APIView):
#     serializer_class    = CustomUserSerializer
#     queryset            = CustomUser.objects.all()
#     @csrf_exempt
#     def post(self, request):
#
#         data = request.data
#         print(data)
#         response = {}
#         username            =data.get('username')
#         password                = data.get('password')
#         mobile_number        = data.get('mobile_number')
#         email = data.get('email')
#
#         if data:
#             if User.objects.filter(Q(username=username) | Q(email=email)).exists():
#                 return Response({'result': 'username or email already exist'})
#             else:
#                 user_create = User.objects.create_user(username=username,email=email,password=password)
#                 custom_user = CustomUser.objects.create(user_id=user_create.id, username=username,email=email,mobile_number=mobile_number)
#                 response={'result': 'user register sucessfull'}
#                 return Response(response, status=status.HTTP_200_OK)
#
#
#         else:
#             response={'result': 'please enter all the required data'}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)
#



class SignupApi(APIView):
    serializer_class    = CustomUserSerializer
    queryset            = CustomUser.objects.all()
    @csrf_exempt
    def post(self, request):
        data = request.data
        print(data)
        response = {}
        username            =data.get('username')
        # fullname=data.get('fullname')
        password                = data.get('password')
        # dob=data.get('dob')
        # role=data.get('role')
        # terms=data.get('terms')

        # mobile_number        = data.get('mobile_number')
        # email = data.get('email')




        if data:

            if User.objects.filter(username=username).exists():
                return Response({'result': 'username or email taken'})

            else:

                user_create = User.objects.create_user(username=username,password=password)
                # custom_user = CustomUser.objects.create(user_id=user_create.id, username=username,fullname=fullname, dob=dob,role=role, terms=terms, email=email, mobile_number=mobile_number)

                response['result'] = 'Register Successfully'

                auth_token = jwt.encode(
                    {'user_id': user_create.id, 'username': user_create.username}, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+auth_token

                response_result = {}
                response_result['Result'] = {
                    'result': {'data': 'Register successful'}}
                response['Authorization'] = authorization
                # response['Token-Type']      =   'Bearer'
                response['status'] = status.HTTP_200_OK
                return Response(response_result['Result'], headers=response,status=status.HTTP_200_OK)

        else:
            return Response({'result': 'Please fill all the OPTIONS'})




#
# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         # data = request.data
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({
#                 'token': token.key,
#                 'user_id': user.pk,
#                 'username':user.username,
#
#                 'message':'Login Successful'
#             })
#         else:
#             response={'message':"invalid username or password"}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)
#
#
# # Application API


# # ?-------------------------  JWT   LOG-IN-------------------------------------------------------------------------------
from rest_framework.generics import GenericAPIView

class LoginView(GenericAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request):
        response = {}
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user_check = User.objects.filter(username= username)
        if user_check:
            user = auth.authenticate(username=username, password=password)
            if user:
                custom_user = User.objects.get(id=user.id)

                auth_token = jwt.encode(
                    {'user_id': user.id, 'username': user.username, 'email': user.email}, str(settings.JWT_SECRET_KEY), algorithm="HS256")

                serializer = CustomUserSerializer(user)
                authorization = 'Bearer'+' '+auth_token
                response_result = {}
                response_result['result'] = {
                    'detail': 'Login successfull',
                    'token':authorization,
                    'user_id':user.id,
                    'username':user.username,
                    # 'fullname':custom.fullname,
                    'email':user.email,
                    # 'mobile_number':custom_user.mobile_number,
                    'status': status.HTTP_200_OK}
                response['Authorization'] = authorization
                # response['Token-Type']      =   'Bearer'
                response['status'] = status.HTTP_200_OK
            else:
                header_response = {}
                response['error'] = {'error': {
                    'detail': 'Invalid credentials', 'status': status.HTTP_401_UNAUTHORIZED}}

                return Response(response['error'], headers=header_response,status= status.HTTP_401_UNAUTHORIZED)
            return Response(response_result, headers=response,status= status.HTTP_200_OK)
        else:
            response='Invalid username'
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RegistrationAPIView(APIView):

    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        user_id = data.get('user_id')
        fullname = data.get('fullname')
        email = data.get('email')
        mobile_number = data.get('mobile_number')
        dob = data.get('dob')
        role = data.get('role')
        terms=data.get('terms')


        if data:

            regcreate = CustomUser.objects.create(user_id=user_id,fullname=fullname, email=email,mobile_number=mobile_number, dob=dob,  role= role,  terms=terms)
            return Response("Data For Application, Added Sucessfully")

        else:
            return Response("Data Required For Application")










class VAppAPIView(APIView):

    # CheckAuth(request)

    def get(self, request):

        id =self.request.query_params.get('id')
        if id:
            appdata = VApp.objects.filter(id=id).values()
            return Response(appdata)
        else:

            appdata = VApp.objects.all().values()
            return Response(appdata)



    def post(self, request):
        data = request.data
        # application_id=data.get('application_id')
        file_no = data.get('file_no')
        case_no = data.get('case_no')
        case_code = data.get('case_code')
        case_id = data.get('case_id')
        case_status = data.get('case_status')
        loan_type = data.get('loan_type')
        owner_name=data.get('owner_name')
        owner_address=data.get('owner_address')
        owner_phone1=data.get('owner_phone1')
        owner_phone2 = data.get('owner_phone2')
        city = data.get('city')
        landmark = data.get('landmark')
        google_map = data.get('google_map')
        # user_id= data.get('user_id')
        bank_id=data.get('bank_id')


        if data:
            vappcreate=VApp.objects.create(file_no=file_no, case_no=case_no,case_code=case_code, case_id=case_id,case_status=case_status, loan_type=loan_type,   owner_name=owner_name, owner_address=owner_address,city=city,landmark=landmark, google_map=google_map ,owner_phone1=owner_phone1, owner_phone2=owner_phone2, bank_id=bank_id  )
            return Response("Data For Application, Added Sucessfully")

        else:
            return Response("Data Required For Application")


    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = VApp.objects.filter(id=id).update(file_no=data.get('file_no'),    case_no= data.get('case_no'), case_code=data.get('case_code'), case_id=data.get('case_id'), case_status=data.get('case_status'), loan_type=data.get('loan_type'),  owner_name=data.get('owner_name'), owner_address=data.get('owner_address'), owner_phone1=data.get('owner_phone1'), owner_phone2=data.get('owner_phone2'), city=data.get('city'), landmark=data.get('landmark'), google_map=data.get('google_map'), bank_id =data.get('bank_id') )

            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)


        else:
            return JsonResponse({'message': 'Id Required.'})



    def delete(self, request):


        id =self.request.query_params.get('id')
        item = VApp.objects.filter(id= id)

        if len(item) > 0:
            item.delete()
            return Response("data Deleted Sucessfully")
        else:
            return Response("Id Required.")




class RoleRefAPIView(APIView):

    def get(self, request):
        CheckAuth(request)
        page_no   = self.request.query_params.get('page_no')
        id =self.request.query_params.get('id')
        if id:
            roldata= RoleRef.objects.filter(id=id).values()
            return Response(roldata)
        else:

            all_values = CustomUser.objects.all().values()
            paginator = Paginator(all_values, 10)
            try:
                paginator_data = paginator.page(page_no)
            except PageNotAnInteger:
                paginator_data = paginator.page(1)
            except EmptyPage:
                print('except')
                paginator_data = paginator.page(paginator.num_pages)
            return JsonResponse({"Data": list(paginator_data)})





    def post(self, request):
        data = request.data
        # vapp_id=data.get('vapp_id')
        # site_visit_id = data.get('site_visit_id')
        user_id= data.get('user_id')
        user_role_name=data.get('user_role_name')



        rolecreate = RoleRef.objects.create( user_id=user_id,  user_role_name=user_role_name, )
        return Response("Data Added Sucessfully")



    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = RoleRef.objects.filter(id=id).update(user_id= data.get('user_id'),  user_role_name=data.get('user_role_name'),)

            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)


        else:
            return JsonResponse({'message': 'Id Required.'})



    def delete(self, request):


        id =self.request.query_params.get('id')
        item = RoleRef.objects.filter(id= id)

        if len(item) > 0:
            item.delete()
            return Response("Data Deleted Sucessfully")
        else:
            return Response("Id Required.")




class FieldReportAPIView(APIView):

    def get(self, request):
        CheckAuth(request)

        id =self.request.query_params.get('id')
        if id:
            reportdata = FieldReport.objects.filter(id=id).values()
            return Response(reportdata)
        else:

            reportdata = FieldReport.objects.all().values()
            return Response(reportdata)



    def post(self, request):
        data = request.data
        # vapp_id=data.get('vapp_id')
        sitevisit_id = data.get('sitevisit_id')
        user_id= data.get('user_id')
        # vapp_id= data.get('vapp_id')
        fieldreport_location=data.get('fieldreport_location')
        fieldreport_comment=data.get('fieldreport_comment')
        fieldreport_status=data.get('fieldreport_status')

        reportcreate = FieldReport.objects.create( user_id=user_id, sitevisit_id=sitevisit_id  , fieldreport_location=fieldreport_location, fieldreport_comment=fieldreport_comment, fieldreport_status=fieldreport_status )
        return Response("Data Added Sucessfully")



    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = FieldReport.objects.filter(id=id).update(user_id= data.get('user_id'), sitevisit_id=data.get('sitevisit_id'), fieldreport_location=data.get('fieldreport_location'), fieldreport_comment=data.get('fieldreport_comment'), fieldreport_status=data.get('fieldreport_status') )

            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)


        else:
            return JsonResponse({'message': 'Id Required.'})



    def delete(self, request):


        id =self.request.query_params.get('id')
        item = FieldReport.objects.filter(id= id)

        if len(item) > 0:
            item.delete()
            return Response("Data Deleted Sucessfully")
        else:
            return Response("Id Required.")




class BankAPIView(APIView):

    def get(self, request):
        CheckAuth(request)

        id =self.request.query_params.get('id')
        if id:
            bankdata = Bank.objects.filter(id=id).values()
            return Response(bankdata)
        else:

            bankdata = Bank.objects.all().values()
            return Response(bankdata)



    def post(self, request):
        data = request.data
        bank_city=data.get('bank_city')
        Bank_state = data.get('Bank_state')
        bank_name= data.get('bank_name')
        branch= data.get('branch')
        bank_address=data.get('bank_address')

        bankcreate = Bank.objects.create( bank_city=bank_city, Bank_state=Bank_state , bank_name=bank_name, branch=branch, bank_address=bank_address  )
        return Response("Data Added Sucessfully")



    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Bank.objects.filter(id=id).update(bank_city= data.get('bank_city'),  Bank_state=data.get('Bank_state'), bank_name=data.get('bank_name'),  branch=data.get('branch'),  bank_address=data.get('bank_address'), )

            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)


        else:
            return JsonResponse({'message': 'Id Required.'})



    def delete(self, request):


        id =self.request.query_params.get('id')
        item = Bank.objects.filter(id= id)

        if len(item) > 0:
            item.delete()
            return Response("Data Deleted Sucessfully")
        else:
            return Response("Id Required.")




#SITEVISIT API

class SiteVisitAPIView(APIView):

    def get(self, request):
        CheckAuth(request)

        id =self.request.query_params.get('id')
        if id:
            sitedata = SiteVisit.objects.filter(id=id).values()
            return Response(sitedata)
        else:

            sitedata = SiteVisit.objects.all().values()
            return Response(sitedata)



    def post(self, request):
        data = request.data
        vapp_id=data.get('vapp_id')
        # site_visit_id = data.get('site_visit_id')
        user_id= data.get('user_id')
        site_visit_comments=data.get('site_visit_comments')
        site_visit_status=data.get('site_visit_status')


        sitecreate = SiteVisit.objects.create(vapp_id=vapp_id, user_id=user_id,  site_visit_comments=site_visit_comments, site_visit_status=site_visit_status )
        return Response("Data Added Sucessfully")



    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = SiteVisit.objects.filter(id=id).update(vapp_id = data.get('vapp_id'),user_id= data.get('user_id'),  site_visit_comments=data.get('site_visit_comments'), site_visit_status=data.get('site_visit_status') )

            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)


        else:
            return JsonResponse({'message': 'Id Required.'})



    def delete(self, request):


        id =self.request.query_params.get('id')
        item = SiteVisit.objects.filter(id= id)

        if len(item) > 0:
            item.delete()
            return Response("Data Deleted Sucessfully")
        else:
            return Response("Id Required.")




class IssueAPIView(APIView):

    def get(self, request):

        id =self.request.query_params.get('id')
        if id:
            issuedata = Issue.objects.filter(id=id).values()
            return Response(issuedata)
        else:

            issuedata = Issue.objects.all().values()
            return Response(issuedata)



    def post(self, request):
        data = request.data
        # vapp_id=data.get('vapp_id')
        field_id = data.get('field_id')
        # user_id= data.get('user_id')

        issue_name= data.get('issue_name')
        # banksubmission_id=data.get('banksubmission_id')
        issue_comments= data.get('issue_comments')

        if data:

            issuecreate = Issue.objects.create(  field_id=field_id,   issue_name=issue_name,   issue_comments=issue_comments)
            return Response("Data For issue, Added Sucessfully")

        else:
            return Response("invalid data")


    def put(self, request):
        data = request.data
        id = data.get('id')
        if id:
            data = Issue.objects.filter(id=id).update( field_id=data.get('field_id'), issue_name= data.get('issue_name'), issue_comments=data.get('issue_comments'), )

            if data:
                    return JsonResponse({'message': 'data Updated Sucessfully.'})
            else:
                response={'message':"Invalid id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)


        else:
            return JsonResponse({'message': 'Id Required.'})



    def delete(self, request):


        id =self.request.query_params.get('id')
        item = Issue.objects.filter(id= id)

        if len(item) > 0:
            item.delete()
            return Response("Data Deleted Sucessfully")
        else:
            return Response("Id Required.")







from tablib import Dataset
from .resources import ExcelsheetDataResource
class UploadExcel(APIView):
    def post(self, request):
            person_resource = ExcelsheetDataResource()
            dataset = Dataset()
            excel_file = request.FILES['excel_file']

            imported_data = dataset.load(excel_file.read(),format='xlsx')
            for i in imported_data:
                value = ExcelsheetData(
                    i[0], i[1], i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12]
                )
                value.save()
            return  Response({'result': {'message': 'file uploaded successfully'}})







from datetime import datetime
from datetime import timedelta
from datetime import datetime,date,time
import time
from datetime import date


class VAppShowAPIView(APIView):
    def post(self, request):
        # today = date.today()
        data = request.data
        from_date=data.get('from_date')
        to_date=data.get('to_date')


        if from_date and to_date:

            countdata =VApp.objects.filter(Q(created__gte=from_date)&Q( created__lte=to_date)).values()

            return Response(countdata)

        else:
            vdata = VApp.objects.all().values()
            return Response(vdata)




class SiteVisitShowAPIView(APIView):
    def post(self, request):

        # today = date.today()
        data = request.data
        from_date=data.get('from_date')
        to_date=data.get('to_date')


        if from_date and to_date:

            countdata =SiteVisit.objects.filter(Q(created__gte=from_date)&Q( created__lte=to_date)).values()

            return Response(countdata)

        else:
            vdata = SiteVisit.objects.all().values()
            return Response(vdata)




class FieldReportShowAPIView(APIView):
    def post(self, request):

        # today = date.today()
        data = request.data
        from_date=data.get('from_date')
        to_date=data.get('to_date')


        if from_date and to_date:

            countdata =FieldReport.objects.filter(Q(created__gte=from_date)&Q( created__lte=to_date)).values()

            return Response(countdata)

        else:
            vdata = FieldReport.objects.all().values()
            return Response(vdata)




class IssueShowAPIView(APIView):
    def post(self, request):

        # today = date.today()
        data = request.data
        fdate=data.get('fdate')
        tdate=data.get('tdate')


        if fdate and tdate:

            showdata =Issue.objects.filter(Q(created__gte=from_date)&Q( created__lte=to_date)).values()

            return Response(showdata)

        else:
            vdata = Issue.objects.all().values()
            return Response(vdata)




from datetime import datetime
from datetime import timedelta
from datetime import datetime,date,time
import time
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date

class VAppTATAPIView(APIView):
    def get(self,request):
        today = date.today()
        id = request.query_params.get('id')
        print(today)
        countdata =VApp.objects.filter(id=id)
        for i in countdata:
            D1_cal=today- (i.created).date()
            days = D1_cal.days
            # seconds = D1_cal.seconds
            # hours = seconds//3600
            # minutes = (seconds//60)%60
            # seconds %= 60

            # D1_data=[days,'days']
            if int(days) == 1:
                return Response('1 days')
            if int(days) == 2:
                return Response('2 days')
            if int(days) == 3:
                return Response('3 days')
            if int(days) > 3:
                return Response('More then 3')










#
# class VAppCountAPIView(APIView):
#     def get (self,request):
#         vappcount=VApp.objects.all().count()
#         return Response(vappcount)
#
#
#
#
# class SiteVisitCountAPIView(APIView):
#     def get (self,request):
#         sitecount=SiteVisit.objects.all().count()
#         return Response(sitecount)
#
#
#


from django.contrib.auth import authenticate
class ChangePassword(APIView):

    def post(self, request):

        data = request.data


        user_id = data.get('user_id')
        old_password = data.get('old_password')
        password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        user_check = User.objects.filter(id= user_id)
        for j in user_check:

            if old_password:
                print(old_password,'old')
                user = auth.authenticate(username=j.username, password=old_password)

                if user:
                    if password and confirm_password:
                        if password == confirm_password:
                            if user_check:

                                user_data = User.objects.get(id= user_id)
                                user_data.set_password(password)
                                user_data.save()

                                response="Password Updated Sucessfully"
                                return Response(response, status=status.HTTP_200_OK)

                            else:
                                response="Please Enter user-ID"
                                return Response(response, status=status.HTTP_400_BAD_REQUEST)

                        else:
                            response="Password did not matched"
                            return Response(response, status=status.HTTP_400_BAD_REQUEST)

                    else:
                        response="New password and confirm password required"
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)

                else:
                    response="Invalid old password"
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

            else:
                response="Old Password required"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)




from django.contrib.auth import authenticate
from django.core.mail import message, send_mail, EmailMessage
import inspect

otpsss= random.randint(100000, 999999)
forgotpass_otps=otpsss
class ForgotPassword_send_otp(APIView):

    def post(self, request):
        data = request.data

        username = data.get('username')

        user_check=User.objects.filter(username=username)
        for i in user_check:
            emails=i.email
        if user_check:
            message = inspect.cleandoc('''Hello,\n%s is your OTP to Forgot Password to your jobportal.\nWith Warm Regards,\njobportal,
                                   ''' % (otpsss))
            send_mail(
                'Greetings from jobportal', message
                ,
                'gunjan.kr518@gmail.com',
                [emails],

            )
            data_dict = {}
            data_dict["Otp"] = otpsss
            return JsonResponse(data_dict, safe=False)

        else:
            response="Invalid username"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class OTP_Verification_forgotpassAPIView(APIView):


    def post(self, request):
        data = request.data
        otp = data.get('otp')
        print(forgotpass_otps,'ori')
        print(otp,'ori')
        if otp:
            if int(otp)==int(forgotpass_otps):
                response="OTP matcheds successfully"
                return Response(response, status=status.HTTP_200_OK)
            else:
                response="Invalid otp"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response="otp required"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordUpdate(APIView):

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        user_check = CustomUser.objects.filter(username= username)

        if password == confirm_password:
            if user_check:
                user_data = User.objects.get(username= username)
                user_data.set_password(password)
                user_data.save()

                message= 'Hello!\nYour password has been updated sucessfully. '
                subject= 'Password Updated Sucessfully '

                email = EmailMessage(subject, message, to=[user_data.email])
                email.send()
                response="Password Updated Sucessfully"
                return Response(response, status=status.HTTP_200_OK)

            else:
                response="Please Enter Valid username"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response="Password did not matched"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)





class LogoutAPIView(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ProfileAPIView(APIView):
    # queryset = Custom_User.objects.all().values()
    def get(self,request):
        id = self.request.query_params.get('id')
        page_no   = self.request.query_params.get('page_no')

        if id:
            all_values = CustomUser.objects.filter(id=id).values()

            return Response(all_values)
        else:

            all_values = CustomUser.objects.all().values()
            paginator = Paginator(all_values, 10)
            try:
                paginator_data = paginator.page(page_no)
            except PageNotAnInteger:
                paginator_data = paginator.page(1)
            except EmptyPage:
                print('except')
                paginator_data = paginator.page(paginator.num_pages)
            return JsonResponse({"Data": list(paginator_data)})

            # return Response(all_values)

    def post(self,request):
        data = request.data
        username=data.get('username')
        # fullname=
        mobile_number=data.get('mobile_number')
        email=data.get('email')
        # roleref_id=data.get('roleref_id')
        terms=data.get('terms')
        fullname        =data.get('fullname')

        dob=data.get('dob')



        if User.objects.filter(username=username,email=email).exists():
            return Response({'result':'username/Email exists'})
        else:
            user_create = User.objects.create_user(username=username,email=email)
            custom_user = CustomUser.objects.create(user_id=user_create.id,username=username, fullname=fullname,mobile_number=mobile_number,email=email,dob=dob, terms=terms)



            return Response({'result':'Created'})


    def put(self,request):

        data = request.data

        id=data.get('id')
        user_id=data.get('user_id')
        #
        mobile_number=data.get('mobile_number')

        # roleref_id=data.get('roleref_id')
        terms=data.get('terms')
        fullname        =data.get('fullname')

        dob=data.get('dob')



        data= CustomUser.objects.filter(id=id).update(fullname=fullname, dob=dob, terms=terms,    mobile_number=mobile_number)


        return Response({'result':'Updated'})

    def delete(self,request):
        all_values = CustomUser.objects.get(id=id)
        del_user=User.objects.filter(id=all_values.user_id).delete()
        return Response({'result':'Deleted'})
