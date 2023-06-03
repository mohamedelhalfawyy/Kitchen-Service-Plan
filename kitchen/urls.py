from django.urls import path

from kitchen import views

urlpatterns = [
    # Other existing URL patterns

    # Endpoint to remove an employee
    path('employee/remove/<int:employee_id>/', views.RemoveEmployeeView.as_view(), name='remove-employee'),

    # Endpoint to add a new employee
    path('employee/add/', views.AddEmployeeView.as_view(), name='add-employee'),

    # Endpoint for the kitchen service plan
    path('service-plan/<int:year>/<int:month>/<int:day>/', views.KitchenServicePlanView.as_view(), name='service-plan'),
]
