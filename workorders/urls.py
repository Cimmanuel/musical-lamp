from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from django.urls import path
# from .views import WorkerListCreate, WorkerRetrieveDestroy, WorkOrderListCreate, WorkOrderRetrieveDestroy
from .views import WorkerViewSet, WorkOrderViewSet, WorkOrderByWorkerList

router = DefaultRouter()
router.register('workers', WorkerViewSet, base_name='workers')
router.register('workorder', WorkOrderViewSet, base_name='workorder')

urlpatterns = [
    path('worker/<int:pk>/workorders/', WorkOrderByWorkerList.as_view(), name='workorder_by_worker_list'),
    path('docs/', include_docs_urls(title="Work Orders Documentation"))
]

urlpatterns += router.urls
