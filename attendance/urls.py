from django.urls import path
from . import views

urlpatterns = [
    path("mark/", views.mark_attendance, name="mark_attendance"),
    path("list/", views.attendance_list, name="attendance_list"),
    path("weekly/", views.weekly_summary, name="weekly_summary"),
    path("weekly/csv/", views.download_weekly_csv, name="download_weekly_csv"),
    path("weekly/excel/", views.download_weekly_excel, name="download_weekly_excel"),
    path("monthly/", views.monthly_summary, name="monthly_summary"),
    path("monthly/csv/", views.download_monthly_csv, name="download_monthly_csv"),
    path("monthly/excel/", views.download_monthly_excel, name="download_monthly_excel"),
    path('', views.home, name='home'),
]
