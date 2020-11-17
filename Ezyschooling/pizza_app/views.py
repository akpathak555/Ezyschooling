from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import traceback
from pizza_app.models import Pizza
from pizza_app.serializers import PizzaSerializer
from django.db.models import Q

class PizzaView(viewsets.ModelViewSet):
    def create(self, request):
        try:
            data = request.data
            serializer = PizzaSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Pizza added successfully.", "data": serializer.data, "success": True}, status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({'message': str(error), 'success': False}, status=status.HTTP_200_OK)

    def list(self, request):
        try:
            pizza_size = request.GET.get('size')
            pizza_type = request.GET.get('type')
            if pizza_size and pizza_type:
                pizza_obj = Pizza.objects.filter(Q(pizza_size=pizza_size) & Q(pizza_type=pizza_type))   
            elif pizza_size:
                pizza_obj = Pizza.objects.filter(pizza_size=pizza_size)
            elif pizza_type:
                pizza_obj = Pizza.objects.filter(pizza_type=pizza_type)
            else:
                pizza_obj = Pizza.objects.all()
            serializer = PizzaSerializer(instance=pizza_obj, many=True)
            return Response({"data": serializer.data, "success": True}, status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({'message': str(error), 'success': False}, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        try:
            pizza_obj = Pizza.objects.get(id=pk)
            pizza_obj.delete()
            return Response({"message": "Data deleted successfully.", "success": True}, status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({'message': str(error), 'success': False}, status=status.HTTP_200_OK)