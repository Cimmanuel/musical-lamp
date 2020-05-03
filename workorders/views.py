from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from .models import Worker, WorkOrder
from .serializers import WorkerSerializer, WorkOrderSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given worker.

    list:
    Return a list of all the existing workers.

    create:
    Create a new worker instance.
    """
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkOrderViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given work order.

    list:
    Return a list of all the existing work orders.

    create:
    Create a new work order instance.
    """
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

class WorkOrderByWorkerList(generics.ListAPIView):
    """
    Return a list of all work orders corresponding to a worker.
    """
    def get_queryset(self):
        queryset = Worker.objects.get(id=self.kwargs["pk"]).assignees.all().order_by('deadline')
        return queryset
    serializer_class = WorkOrderSerializer


# class WorkerListCreate(generics.ListCreateAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer

# class WorkerRetrieveDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer

# class WorkOrderListCreate(generics.ListCreateAPIView):
#     queryset = WorkOrder.objects.all()
#     serializer_class = WorkOrderSerializer

# class WorkOrderRetrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = WorkOrder.objects.all()
#     serializer_class = WorkOrderSerializer
