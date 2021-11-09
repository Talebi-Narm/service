from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from Specialist.models import Specialist, SpecilistFields
from Ticket.models import ConversationModel, TicketModel
from django.db.models import Count

from Ticket.serializers import ConversationSerializer, RateSerializer, TicketSerializer
from Users.models import Member, NewUser

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        '(post) New Question Ticket With New Conversation':'/new-ticket/',
        '(post) New Question  Ticket With For Giver Conversation By ID':'/new-question-ticket/<str:pk>/',
        '(post) New Answer Ticket With For Giver Conversation By ID':'/new-question-ticket/<str:pk>/',
        '(get) Get All Conversations':'/all-conversations/',
        '(get) Get All Tickets':'/all-tickets/',
        '(get) Get This Member Conversations':'/member-conversations/',
        '(get) Get This Specialist Conversation':'/special-conversations/',
        '(get) Get This Member Conversations':'/member-conversations/<str:pk>/',
        '(get) Get This Specialist Conversation':'/special-conversations/<str:pk>/',
        '(get) Get This Member Tickets':'/member-tickets/',
        '(get) Get This Specialist Tickets':'/special-tickets/',
        '(get) Get This Member Tickes':'/member-tickets/<str:pk>/',
        '(get) Get This Specialist Tickets':'/special-tickets/<str:pk>/',
        '(get) Get Specialist Secondary Info By Id':'/secondary/<str:pk>/',
        '(post) Update this User Secondary Info (id_code, birth_date, degree, major, phone_number, about,address,is_online, rate)':'/update-secondary/',
        '(delete) Delete Specialist By Id (*id)':'/delete/',
    }
    return Response(api_urls)

#######################
#------------ CRUD Ticket And Conversation
#######################

#------- CREATE
###############

#Question Ticket Create For New Conversation
class QuestionTicketCreateForNewConversation(APIView):
    def post(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserOfConversation = request.user
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save()
            if ticket:
                #Assign Specialist
                IdSpecialistToAssign = ConversationModel.objects.all().values('specialist').annotate(total=Count('specialist')).order_by('-total').values('specialist').first()
                SpecialistToAssign = Specialist.objects.get(id=IdSpecialistToAssign)
                newConversation = ConversationModel.objects.create(member=UserOfConversation, specialist=SpecialistToAssign)
                newConversation.question_tickect.set(ticket)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Question Ticket Create For Given Conversation With ID
class QuestionTicketCreateForGivenConversation(APIView):
    def post(self, request, pk, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if ConversationModel.objects.exists(id = pk) == False:
            return Response("No Conversation With This Id Found!", status=status.HTTP_404_NOT_FOUND)
        UserOfConversation = request.user
        thisConversation = ConversationModel.objects.get(id = pk)
        if thisConversation.member != UserOfConversation:
            return Response("Access Denied! This is NOT Your Conversation!", status=status.HTTP_403_FORBIDDEN)
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save()
            if ticket:
                thisConversation.question_tickect.set(ticket)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Answer Ticket Create For Given onversation With ID
class AnswerTicketCreateForGivenConversation(APIView):
    def post(self, request, pk, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type == NewUser.Types.MEMBER:
            return Response("You're not a Specialist!", status=status.HTTP_403_FORBIDDEN)
        if ConversationModel.objects.exists(id = pk) == False:
            return Response("No Conversation With This Id Found!", status=status.HTTP_404_NOT_FOUND)
        UserOfConversation = request.user
        thisConversation = ConversationModel.objects.get(id = pk)
        if thisConversation.member != UserOfConversation:
            return Response("Access Denied! This is NOT Your Conversation!", status=status.HTTP_403_FORBIDDEN)
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save()
            if ticket:
                thisConversation.answer_tickect.set(ticket)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- READ
###############

#Get All Conversations
class GetAllConversations(APIView):
    def get(self, request, format='json'):
        ConversatrionsInfo = ConversationModel.objects.all()
        serializer = ConversationSerializer(ConversatrionsInfo, many=True)
        return Response(serializer.data)

#Get All Tickects
class GetAllTickects(APIView):
    def get(self, request, format='json'):
        TicketsInfo = TicketModel.objects.all()
        serializer = ConversationSerializer(TicketsInfo, many=True)
        return Response(serializer.data)

#Get This User Conversations
class GetThisUserConversations(APIView):
    def get(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.MEMBER:
            return Response("You're not a Member!", status=status.HTTP_403_FORBIDDEN)
        UserToGet = request.user
        ConversatrionsInfo = ConversationModel.objects.filter(member = UserToGet)
        serializer = ConversationSerializer(ConversatrionsInfo, many=True)
        return Response(serializer.data)

#Get This Specialist Conversations
class GetThisSpecialistConversations(APIView):
    def get(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.SPECIALIST:
            return Response("You're not a Specialist!", status=status.HTTP_403_FORBIDDEN)
        SpecialistToGet = request.user
        ConversatrionsInfo = ConversationModel.objects.filter(specialist = SpecialistToGet)
        serializer = ConversationSerializer(ConversatrionsInfo, many=True)
        return Response(serializer.data)

#Get User Conversations With ID
class GetUserConversations(APIView):
    def get(self, request, pk, format='json'):
        if NewUser.objects.exists(id=pk) == False:
            return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        UserToGet = NewUser.objects.get(id=pk)
        ConversatrionsInfo = ConversationModel.objects.filter(member = UserToGet)
        serializer = ConversationSerializer(ConversatrionsInfo, many=True)
        return Response(serializer.data)

#Get Specialist Converdsations With ID
class GetSpecialistConversations(APIView):
    def get(self, request, pk, format='json'):
        if Specialist.objects.exists(id=pk) == False:
            return Response("This Specialist Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        SpecialistToGet = NewUser.objects.get(id=pk)
        ConversatrionsInfo = ConversationModel.objects.filter(specialist = SpecialistToGet)
        serializer = ConversationSerializer(ConversatrionsInfo, many=True)
        return Response(serializer.data)

#Get This User Tickets
class GetThisUserTickets(APIView):
    def get(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.MEMBER:
            return Response("You're not a Member!", status=status.HTTP_403_FORBIDDEN)
        UserToGet = request.user
        TicketsInfo = TicketModel.objects.filter(author = UserToGet)
        serializer = TicketSerializer(TicketsInfo, many=True)
        return Response(serializer.data)

#Get This Specialist Tickets
class GetThisSpecialistTickets(APIView):
    def get(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.SPECIALIST:
            return Response("You're not a Specialist!", status=status.HTTP_403_FORBIDDEN)
        SpecialistToGet = request.user
        TicketsInfo = TicketModel.objects.filter(author = SpecialistToGet)
        serializer = TicketSerializer(TicketsInfo, many=True)
        return Response(serializer.data)

#Get User Tickets With ID
class GetThisUserTickets(APIView):
    def get(self, request, pk, format='json'):
        if NewUser.objects.exists(id=pk) == False:
            return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        UserToGet = NewUser.objects.get(id=pk)
        TicketsInfo = TicketModel.objects.filter(author = UserToGet)
        serializer = TicketSerializer(TicketsInfo, many=True)
        return Response(serializer.data)

#Get Specialist Tickets With ID
class GetThisSpecialistTickets(APIView):
    def get(self, request, pk, format='json'):
        if Specialist.objects.exists(id=pk) == False:
            return Response("This Specialist Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        SpecialistToGet = NewUser.objects.get(id=pk)
        TicketsInfo = TicketModel.objects.filter(author = SpecialistToGet)
        serializer = TicketSerializer(TicketsInfo, many=True)
        return Response(serializer.data)


#------- UPDATE
###############

#Done Specialist Tickets With ID
class DoneTheConverstion(APIView):
    def post(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserOfConversation = request.user
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            if ConversationModel.objects.exists(id = serializer.data['id']) == False:
                return Response("No Conversation With This Id Found!", status=status.HTTP_404_NOT_FOUND)
            thisConversation = ConversationModel.objects.get(id = serializer.data['id'])
            if thisConversation.member != UserOfConversation:
                return Response("Access Denied! This is NOT Your Conversation!", status=status.HTTP_403_FORBIDDEN)
            thisConversation.rate = serializer.data['rate']
            ThisConversationSpecialist = Specialist.objects.get(id=thisConversation.specialist)
            CountSpecialist = ConversationModel.objects.filter(specialist=ThisConversationSpecialist,done=True).count()
            SpecialistInfo = SpecilistFields.objects.get(user=ThisConversationSpecialist)
            oldrate = SpecialistInfo.rate
            newrate = ((oldrate * CountSpecialist) + serializer.data['rate'])/(CountSpecialist + 1)
            SpecialistInfo.rate = newrate
            thisConversation.done = True
            return Response("Thank you! Your score was recorded", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
