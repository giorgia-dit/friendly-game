from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import TemplateView, DetailView, ListView
from .models import Friend, Delivery


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"



class FriendListView(LoginRequiredMixin, ListView):
    model = Friend
    template_name = "friend/friend_list.html"
    context_object_name = "friends"

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'shuffle' in self.request.GET:  
            return queryset.exclude(pk=34).order_by('?') 
        return queryset.exclude(pk=34).order_by('first_name')


class DeliveryDetailView(LoginRequiredMixin, DetailView):
    model = Delivery
    template_name = "delivery/delivery_detail.html"
    context_object_name = "delivery"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.friend.user != request.user:
            raise Http404("You do not have permission to view this delivery.")
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Delivery._meta.get_field('status').choices
        return context
    

class PrizePageView(LoginRequiredMixin, TemplateView):
    template_name = "prize.html"


class NutritionalPageView(LoginRequiredMixin, TemplateView):
    template_name = "nutritional.html"