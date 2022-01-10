from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.contrib.auth.models import User
from django.views.generic.base import RedirectView
from django.http import JsonResponse
from django.core import serializers
import json
from main.forms import BookingForm
from main.models import BookingModel, BroadcastModel


# Create your views here.
@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    template = 'main/dashboard.html'

    def get(self, *args, **kwargs):
        bookings = BookingModel.objects.filter(user=self.request.user)
        broadcasts = BroadcastModel.objects.all()
        context={
            'title':'Dashboard',
            'bookings': bookings,
            'broadcasts': broadcasts
        }
        return render(self.request, self.template, context)

    def post(self, *args, **kwargs):
        form = BookingForm(self.request.POST)
        if form.is_valid():
            broadcast_id = form.cleaned_data.get('broadcast_id')
            remarks = form.cleaned_data.get('remarks')

            booking = BookingModel()
            booking.user = self.request.user
            booking.broadcast_id = broadcast_id
            booking.remarks = remarks
            booking.save()
        else:
            print(form.errors)
        return redirect("/")

@method_decorator(login_required, name='dispatch')
class EditBookingView(View):
    template = 'main/edit_booking.html'

    def get(self, *args, **kwargs):
        booking = BookingModel.objects.get(pk=self.kwargs['id'])
        broadcasts = BroadcastModel.objects.all()
        context={
            'title':'Edit Booking',
            'booking': booking,
            'broadcasts': broadcasts
        }
        return render(self.request, self.template, context)
    
    def post(self, *args, **kwargs):
        form = BookingForm(self.request.POST)
        if form.is_valid():
            broadcast_id = form.cleaned_data.get('broadcast_id')
            remarks = form.cleaned_data.get('remarks')

            booking = BookingModel.objects.get(pk=self.kwargs['id'])
            booking.broadcast_id = broadcast_id
            booking.remarks = remarks
            booking.save()
        else:
            print(form.errors)
        return redirect("/")
        
@login_required
def view_booking(request, id):
    if request.method == 'GET':
        booking = BookingModel.objects.filter(pk=id)
        data = serializers.serialize('json', booking)
        view_booking = json.loads(data)
        broadcast = BookingModel.objects.filter(pk=id)
        broadcast = {"video_url": broadcast[0].broadcast.video_url, "name": broadcast[0].broadcast.name}
        
    return JsonResponse({'status': 'Success', 'booking': view_booking, 'broadcast': broadcast})

@login_required
def delete_booking(request, id):
    if request.method == 'POST':
        booking = BookingModel.objects.get(pk=id)
        booking.delete()
    
    return redirect("/")

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template = 'main/profile.html'

    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        return render(request, self.template, {'title':'Profile', 'user': user })