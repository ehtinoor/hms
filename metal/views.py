# metal/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Metal
from .serializers import MetalSerializer

@api_view(['GET', 'POST'])
def metal_list(request):
    if request.method == 'GET':
        metals = Metal.objects.all()
        serializer = MetalSerializer(metals, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MetalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE'])
def metal_detail(request, pk):
    try:
        metal = Metal.objects.get(pk=pk)
    except Metal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = MetalSerializer(metal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        metal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
