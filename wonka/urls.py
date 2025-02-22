from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    FriendListView,
    DeliveryDetailView,
    DeliveryStatusUpdateView,
    PrizePageView,
    NutritionalPageView
)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("friends/", FriendListView.as_view(), name="friend_list"),
    path("deliveries/<int:pk>/", DeliveryDetailView.as_view(), name="delivery_detail"),
    path('deliveries/<int:pk>/mark-delivered/', DeliveryStatusUpdateView.as_view(), name='mark_delivered'),
    path("prize/", PrizePageView.as_view(), name="prize"),
    path("about/nutritional-information/", NutritionalPageView.as_view(), name="nutritional")
]
