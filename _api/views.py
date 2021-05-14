from _db import models
from . import serializers
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


class HouseList(generics.ListAPIView):
    model = models.House
    queryset = models.House.objects.all()
    serializer_class = serializers.HouseSerializer


class HouseDetail(generics.RetrieveAPIView):
    model = models.House
    queryset = models.House.objects.all()
    serializer_class = serializers.HouseSerializer


class SectionList(generics.ListAPIView):
    model = models.House
    serializer_class = serializers.SectionSerializer

    def get_queryset(self):
        queryset = models.Section.objects.all()
        house = self.request.query_params.get('house')
        if house is not None:
            queryset = queryset.filter(house=house)
        return queryset


class SectionDetail(generics.RetrieveAPIView):
    model = models.Section
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer


class FloorList(generics.ListAPIView):
    model = models.Floor
    serializer_class = serializers.FloorSerializer

    def get_queryset(self):
        queryset = models.Floor.objects.all()
        section = self.request.query_params.get('section')
        if section is not None:
            queryset = queryset.filter(section=section)
        return queryset


class FloorDetail(generics.RetrieveAPIView):
    model = models.Floor
    queryset = models.Floor.objects.all()
    serializer_class = serializers.FloorSerializer


class ApartmentList(generics.ListAPIView):
    model = models.Apartment
    serializer_class = serializers.ApartmentSerializer

    def get_queryset(self):
        queryset = models.Apartment.objects.all()
        apartment = self.request.query_params.get('apartment')
        if apartment is not None:
            queryset = queryset.filter(apartment=apartment)
        return queryset


class ApartmentDetail(generics.RetrieveAPIView):
    model = models.Apartment
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer
