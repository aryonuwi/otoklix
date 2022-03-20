from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework import status


from  otoKlixTestApp.models import otoCrud
from  otoKlixTestApp.serializers import otoCrudSerializer


#@csrf_exempt

class OtoKlixView(APIView):

    def post(self, request):
        serializer = otoCrudSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        
        if id:
            get_object_or_404(otoCrud, id=id)

            item = otoCrud.objects.get(id=id)
            serializer = otoCrudSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        items = otoCrud.objects.all()
        serializer = otoCrudSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        item = otoCrud.objects.get(id=id)
        serializer = otoCrudSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id=None):
        item = get_object_or_404(otoCrud, id=id)
        items = otoCrud.objects.get(id=id)
        serializer = otoCrudSerializer(items)
        item.delete()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
