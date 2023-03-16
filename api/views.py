from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from medicine.models import Medicine
from medicine.serializers import MedicineSerializer
from django.db.models import Q
from rest_framework.views import APIView

# Create your views here.

def update(medicine, data):
    medicine.type=data['type'],
    medicine.name=data['name'],
    # medicine.price=float(data['price']),
    medicine.therauptic_category=data['therauptic_category'],
    medicine.disease=data['disease'],
    medicine.description=data['description']


@api_view(['GET'])
def getEndpoints(request):
    routes = [
        {
            'url' : 'api/medicines',
            'methods' : ['GET', 'POST']
        },
        {
            'url' : 'api/medicine/:id',
            'methods' : ['GET', 'PUT', 'DELETE']
        },
    ]
    return Response(routes)



class MedicineList(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query == None:
            query = ''
        medicines = Medicine.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data)
    def post(self, request):
        medicine = Medicine.objects.create(
            type=request.data['type'],
            name=request.data['name'],
            price=request.data['price'],
            therauptic_category=request.data['therauptic_category'],
            disease=request.data['disease'],
            description=request.data['description'],
        )
        return redirect('medicine-detail', medicine.id)


class MedicineDetail(APIView):
    def get_object(self, id):
        try:
            return Medicine.objects.get(id=id)
        except Medicine.DoesNotExist:
            return Http404
    def get(self, request, id):
        medicine = self.get_object(id)
        serializer = MedicineSerializer(medicine, many=False)
        return Response(serializer.data)
    def post(self, request, id):
        medicine = self.get_object(id)
        update(medicine, request.data)
        medicine.save()
        return Response({"success" : "true"})
    def delete(self, request, id):
        medicine = self.get_object(id)
        medicine.delete()
        return Response({"success" : "true"})