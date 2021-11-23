from django.shortcuts import render
from . import serializers
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . models import TeamModel, BetModel, UpcomingMatche
import json
from django.shortcuts import get_object_or_404

class TeamAPI(APIView):
    serializer_class = serializers.TeamSerializers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        list = TeamModel.objects.get(id=pk)
        serializer = serializers.TeamSerializers(list, many=False)
        return Response(serializer.data)


class BettingSystemAPI(ListCreateAPIView):
    queryset = BetModel.objects.all()
    serializer_class = serializers.Betserializers
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            print(json.dumps(str(serializer.data), sort_keys=True, indent=4))
            return Response({"status": True,
                            "message": "Bet Placed!!",
                            "data": serializer.data},
                            status=status.HTTP_201_CREATED, headers=headers)
        else:
            headers = self.get_success_headers(serializer.data)
            print(request.data)
            return Response({"status": False,
                            "message": "Something went wrong.",
                            "data": serializer.data},
                            status=status.HTTP_401_UNAUTHORIZED, headers=headers)

class UpcomingMatchesAPI(APIView):
    serializer_class = serializers.UpcomingMatchesSerializers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        list = get_object_or_404(UpcomingMatche, id=pk)
        print(list)
        serializer = serializers.UpcomingMatchesSerializers(list, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class AddUpcomingMatchAPI(ListCreateAPIView):
    queryset = UpcomingMatche.objects.all()
    serializer_class = serializers.UpcomingMatchesSerializers
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            print(json.dumps(serializer.data))
            return Response({"status": True,
                            "message": "Bet Placed!!",
                            "data": serializer.data},
                            status=status.HTTP_201_CREATED, headers=headers)
        else:
            headers = self.get_success_headers(serializer.data)
            return Response({"status": False,
                            "message": "Something went wrong.",
                            "data": serializer.data},
                            status=status.HTTP_401_UNAUTHORIZED, headers=headers)