from django.forms import ModelForm
from .models import Stay


class StayForm(ModelForm):
    class Meta:
            model = Stay
            fields = [
                'location',
                'adults',
                'children',
                'date_begin',
                'date_end',
            ]
