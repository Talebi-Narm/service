from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from Specialist.models import Specialist, SpecilistFields
from Ticket.models import ConversationModel, TicketModel, SupportTicketModel
from django.db.models import Count

from Ticket.serializers import ConversationSerializer, RateSerializer, TicketSerializer, CreateSupportTicketSerializer, GetSupportTicketSerializer
from Users.models import Member, NewUser

@api_view(['GET'])
def apiOverview(request):
    """See All Ticket API"""
    api_urls = {
        '(post) New Question Ticket With New Conversation':'/new-question-ticket/',
        '(post) New Question  Ticket With For Giver Conversation By ID':'/new-question-ticket/<str:pk>/',
        '(post) New Answer Ticket With For Giver Conversation By ID':'/new-answer-ticket/<str:pk>/',
        '(get) Get All Conversations':'/all-conversations/',
        '(get) Get All Tickets':'/all-tickets/',
        '(get) Get This Member Conversations':'/member-conversations/',
        '(get) Get This Specialist Conversation':'/specialist-conversations/',
        '(get) Get This Member Conversations':'/member-conversations/<str:pk>/',
        '(get) Get This Specialist Conversation':'/specialist-conversations/<str:pk>/',
        '(get) Get This Member Tickets':'/member-tickets/',
        '(get) Get This Specialist Tickets':'/specialist-tickets/',
        '(get) Get This Member Tickets':'/member-tickets/<str:pk>/',
        '(get) Get This Specialist Tickets':'/specialist-tickets/<str:pk>/',
        '(post) Done Specialist Tickets With ID':'/rate-conversation/<str:pk>/',
        '##################################':'',
        '(post) Create New Support Ticket':'/create-support-ticket/',
        '(get) Get All In Progress Tickets':'/inprogress-tickets/',
        '(get) Get This Specialist In Progress Tickets':'/specialist-inprogress-tickets/',
        '(get) Get This Specialist Accepted Tickets':'/specialist-accepted-tickets/',
        '(get) Get This Member All Tickets':'/member-support-tickets/',
        '(get) Get This Member In progress Tickets':'/member-support-tickets/',
        '(get) Get This Member Accepted Tickets':'/member-support-tickets/',
        
        
    }
    return Response(api_urls)


#######################
#------------ CRUD Support Ticket
#######################

#------- CREATE
###############

#Support Ticket Create For New Conversation
class SupportTicketCreate (generics.GenericAPIView):
    serializer_class = CreateSupportTicketSerializer
    def post(self, request, format='json'):
        """New Support For Sender User"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserOfConversation = request.user
        serializer = CreateSupportTicketSerializer(data=request.data)
        
        if serializer.is_valid():
            ticket = serializer.save()
            if ticket:
                ticket.ticket_author = UserOfConversation
                ticket.ticket_status = 'In progress'
                ticket.save()
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response("OOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- READ
###############

#Read All In progress Support Tickets
class AllInProgressSupportTickets(APIView):
    def get(self, request, format='json'):
        """Get All In Progress Tickets"""
        Tickets = SupportTicketModel.objects.filter(ticket_status= 'In progress')
        serializer = GetSupportTicketSerializer(Tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Read All This Specialist In progress Support Tickets
class SpecialistAllInProgressSupportTickets(APIView):
    serializer_class = GetSupportTicketSerializer
    def get(self, request, format='json'):
        """Read All This Specialist In progress Support Tickets"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.SPECIALIST:
            return Response("You're not a Specialist!", status=status.HTTP_403_FORBIDDEN)
        SpecialistToGet = request.user
        Tickets = SupportTicketModel.objects.filter(ticket_status= 'In progress', ticket_specialist=SpecialistToGet)
        serializer = GetSupportTicketSerializer(Tickets, many=True)
        return Response(serializer.data)

#Read All This Specialist Accepted Support Tickets
class SpecialistAllAcceptedSupportTickets(APIView):
    serializer_class = GetSupportTicketSerializer
    def get(self, request, format='json'):
        """Read All This Specialist Accepted Support Tickets"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.SPECIALIST:
            return Response("You're not a Specialist!", status=status.HTTP_403_FORBIDDEN)
        SpecialistToGet = request.user
        Tickets = SupportTicketModel.objects.filter(ticket_status= 'Accepted', ticket_specialist=SpecialistToGet)
        serializer = GetSupportTicketSerializer(Tickets, many=True)
        return Response(serializer.data)

#Read All This Member All Support Tickets
class MemberAllSupportTickets(APIView):
    serializer_class = GetSupportTicketSerializer
    def get(self, request, format='json'):
        """Read All This Member In progress Support Tickets"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.MEMBER:
            return Response("You're not a Member!", status=status.HTTP_403_FORBIDDEN)
        SpecialistToGet = request.user
        Tickets = SupportTicketModel.objects.filter(ticket_author=SpecialistToGet)
        serializer = GetSupportTicketSerializer(Tickets, many=True)
        return Response(serializer.data)

#Read All This Member In progress Support Tickets
class MemberAllInProgressSupportTickets(APIView):
    serializer_class = GetSupportTicketSerializer
    def get(self, request, format='json'):
        """Read All This Member In progress Support Tickets"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.MEMBER:
            return Response("You're not a Member!", status=status.HTTP_403_FORBIDDEN)
        SpecialistToGet = request.user
        Tickets = SupportTicketModel.objects.filter(ticket_status= 'In progress', ticket_author=SpecialistToGet)
        serializer = GetSupportTicketSerializer(Tickets, many=True)
        return Response(serializer.data)

#Read All This Specialist Accepted Support Tickets
class MemberAllAcceptedSupportTickets(APIView):
    serializer_class = GetSupportTicketSerializer
    def get(self, request, format='json'):
        """Read All This Member Accepted Support Tickets"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.MEMBER:
            return Response("You're not a Member!", status=status.HTTP_403_FORBIDDEN)
        SpecialistToGet = request.user
        Tickets = SupportTicketModel.objects.filter(ticket_status= 'Accepted', ticket_author=SpecialistToGet)
        serializer = GetSupportTicketSerializer(Tickets, many=True)
        return Response(serializer.data)




#######################
#------------ CRUD Ticket And Conversation
#######################

#------- CREATE
###############

#Question Ticket Create For New Conversation
class QuestionTicketCreateForNewConversation(generics.GenericAPIView):
    serializer_class = TicketSerializer
    def post(self, request, format='json'):
        """New Question Ticket With New Conversation"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserOfConversation = request.user
        serializer = TicketSerializer(data=request.data)
        
        if serializer.is_valid():
            ticket = serializer.save()
            if ticket:
                #Assign Specialist
                ticket.author = UserOfConversation
                SpecialistToAssign = Specialist.objects.filter(type=NewUser.Types.SPECIALIST).first()
                IdSpecialistToAssign = ConversationModel.objects.all().values('specialist').annotate(total=Count('specialist')).order_by('-total').values('specialist').first()
                print(IdSpecialistToAssign)
                if IdSpecialistToAssign != None:
                    SpecialistToAssign = Specialist.objects.get(id=IdSpecialistToAssign['specialist'])
                newConversation = ConversationModel.objects.create(member=UserOfConversation, specialist=SpecialistToAssign)
                ticket.save()
                newConversation.question_tickect.add(ticket)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Question Ticket Create For Given Conversation With ID
class QuestionTicketCreateForGivenConversation(APIView):
    serializer_class = TicketSerializer
    def post(self, request, pk, format='json'):
        """New Question  Ticket With For Giver Conversation By ID"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if ConversationModel.objects.filter(id=pk).exists() == False:
            return Response("No Conversation With This Id Found!", status=status.HTTP_404_NOT_FOUND)
        UserOfConversation = request.user
        thisConversation = ConversationModel.objects.get(id = pk)
        if thisConversation.member != UserOfConversation:
            return Response("Access Denied! This is NOT Your Conversation!", status=status.HTTP_403_FORBIDDEN)
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save()
            if ticket:
                ticket.author = UserOfConversation
                ticket.save()
                thisConversation.question_tickect.add(ticket)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Answer Ticket Create For Given onversation With ID
class AnswerTicketCreateForGivenConversation(generics.GenericAPIView):
    serializer_class = TicketSerializer
    def post(self, request, pk, format='json'):
        """New Answer Ticket With For Giver Conversation By ID"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type == NewUser.Types.MEMBER:
            return Response("You're not a Specialist!", status=status.HTTP_403_FORBIDDEN)
        if ConversationModel.objects.filter(id = pk).exists() == False:
            return Response("No Conversation With This Id Found!", status=status.HTTP_404_NOT_FOUND)
        UserOfConversation = request.user
        thisConversation = ConversationModel.objects.get(id = pk)
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save()
            if ticket:
                ticket.author = UserOfConversation
                ticket.save()
                thisConversation.answer_tickect.add(ticket)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- READ
###############

#Get All Conversations
class GetAllConversations(APIView):
    serializer_class = ConversationSerializer
    def get(self, request, format='json'):
        """Get All Conversations"""
        ConversatrionsInfo = ConversationModel.objects.all()
        serializer = ConversationSerializer(ConversatrionsInfo, many=True)
        return Response(serializer.data)

#Get All Tickects
class GetAllTickects(APIView):
    serializer_class = ConversationSerializer
    def get(self, request, format='json'):
        """Get All Tickets"""
        TicketsInfo = TicketModel.objects.all()
        serializer = ConversationSerializer(TicketsInfo, many=True)
        return Response(serializer.data)

#Get This User Conversations
class GetThisUserConversations(APIView):
    serializer_class = ConversationSerializer
    def get(self, request, format='json'):
        """Get This Member Conversations"""
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
    serializer_class = ConversationSerializer
    def get(self, request, format='json'):
        """Get This Specialist Conversation"""
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
    serializer_class = ConversationSerializer
    def get(self, request, pk, format='json'):
        """Get This Member Conversations"""
        if NewUser.objects.filter(id=pk).exists() == False:
            return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        UserToGet = NewUser.objects.get(id=pk)
        ConversatrionsInfo = ConversationModel.objects.filter(member = UserToGet)
        serializer = ConversationSerializer(ConversatrionsInfo, many=True)
        return Response(serializer.data)

#Get Specialist Converdsations With ID
class GetSpecialistConversations(APIView):
    serializer_class = ConversationSerializer
    def get(self, request, pk, format='json'):
        """Get This Specialist Conversation"""
        if Specialist.objects.filter(id=pk).exists() == False:
            return Response("This Specialist Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        SpecialistToGet = NewUser.objects.get(id=pk)
        ConversatrionsInfo = ConversationModel.objects.filter(specialist = SpecialistToGet)
        serializer = ConversationSerializer(ConversatrionsInfo, many=True)
        return Response(serializer.data)

#Get This User Tickets
class GetThisUserTickets(APIView):
    serializer_class = TicketSerializer
    def get(self, request, format='json'):
        """Get This Member Tickets"""
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
    serializer_class = TicketSerializer
    def get(self, request, format='json'):
        """Get This Specialist Tickets"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type != NewUser.Types.SPECIALIST:
            return Response("You're not a Specialist!", status=status.HTTP_403_FORBIDDEN)
        SpecialistToGet = request.user
        TicketsInfo = TicketModel.objects.filter(author = SpecialistToGet)
        serializer = TicketSerializer(TicketsInfo, many=True)
        return Response(serializer.data)

#Get User Tickets With ID
class GetUserTickets(APIView):
    serializer_class = TicketSerializer
    def get(self, request, pk, format='json'):
        """Get Member Tickets With ID"""
        if NewUser.objects.filter(id=pk).exists() == False:
            return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        UserToGet = NewUser.objects.get(id=pk)
        TicketsInfo = TicketModel.objects.filter(author = UserToGet)
        serializer = TicketSerializer(TicketsInfo, many=True)
        return Response(serializer.data)

#Get Specialist Tickets With ID
class GetSpecialistTickets(APIView):
    serializer_class = TicketSerializer
    def get(self, request, pk, format='json'):
        """Get Specialist Tickets With ID"""
        if Specialist.objects.filter(id=pk).exists() == False:
            return Response("This Specialist Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        SpecialistToGet = NewUser.objects.get(id=pk)
        TicketsInfo = TicketModel.objects.filter(author = SpecialistToGet)
        serializer = TicketSerializer(TicketsInfo, many=True)
        return Response(serializer.data)


#------- UPDATE
###############

#Done Specialist Tickets With ID
class DoneTheConverstion(generics.GenericAPIView):
    serializer_class = RateSerializer
    def post(self, request, format='json'):
        """Done Specialist Tickets With ID"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserOfConversation = request.user
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            if ConversationModel.objects.filter(id = serializer.data['id']).exists() == False:
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
