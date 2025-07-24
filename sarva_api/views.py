from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecificationForm
from .serializers import WheelSpecificationFormSerializer

@api_view(['GET', 'POST'])
def wheel_specifications(request):
    if request.method == 'POST':
        serializer = WheelSpecificationFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": serializer.data
            }, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'GET':
        form_number = request.GET.get('formNumber')
        submitted_by = request.GET.get('submittedBy')
        submitted_date = request.GET.get('submittedDate')

        filters = {}
        if form_number:
            filters['form_number'] = form_number
        if submitted_by:
            filters['submitted_by'] = submitted_by
        if submitted_date:
            filters['submitted_date'] = submitted_date

        queryset = WheelSpecificationForm.objects.filter(**filters)
        serializer = WheelSpecificationFormSerializer(queryset, many=True)

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        }, status=200)


