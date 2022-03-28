from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from services.models import ServiceModel
from services.serializers import ServiceSerializer
from rest_framework.decorators import api_view

from .mockup import mockup_values


@api_view(['GET', 'POST', 'DELETE'])
def service_list(request):
    if request.method == 'GET':
        services = ServiceModel.objects.all()

        # Populate DB if empty with default values.
        if services.count() == 0:
            for service_json in mockup_values():
                service_serializer = ServiceSerializer(data=service_json)
                if service_serializer.is_valid():
                    service_serializer.save()
            services = ServiceModel.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            services = services.filter(title__icontains=title)

        services_serializer = ServiceSerializer(services, many=True)
        return JsonResponse(services_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        service_data = JSONParser().parse(request)
        service_serializer = ServiceSerializer(data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse(service_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = ServiceModel.objects.all().delete()
        return JsonResponse({'message': '{} Services were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, pk):
    # find service by pk (id)
    try:
        service = ServiceModel.objects.get(pk=pk)
    except ServiceModel.DoesNotExist:
        return JsonResponse({'message': 'The service does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        service_serializer = ServiceSerializer(service)
        return JsonResponse(service_serializer.data)

    elif request.method == 'PUT':
        service_data = JSONParser().parse(request)
        service_serializer = ServiceSerializer(service, data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse(service_serializer.data)
        return JsonResponse(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        service.delete()
        return JsonResponse({'message': 'Service was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# Search by fields

# @api_view(['GET'])
# def service_list_published(request):
#    services = ServiceModel.objects.filter(published=True)

#    if request.method == 'GET':
#        services_serializer = ServiceSerializer(services, many=True)
#        return JsonResponse(services_serializer.data, safe=False)
