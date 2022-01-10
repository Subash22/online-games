from django import forms


class BookingForm(forms.Form):
    broadcast_id = forms.IntegerField(required=False)
    remarks = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3
    }))