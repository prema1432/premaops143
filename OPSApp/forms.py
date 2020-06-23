from django import forms

from .models import Student, pupload


class StudentOTRForm(forms.ModelForm):
    class Meta:
        model =Student
        fields = '__all__'


class puploadForm(forms.ModelForm):
    class Meta:
        model =pupload
        exclude=('user','gustatus','hostatus','gucomments','hocomments','rating','pdate')

# class gstatusviewForm(forms.ModelForm):
#     class Meta:
#         model = gstatus
#         fields = '__all__'

class gapproveroject(forms.ModelForm):
    class Meta:
        model = pupload
        fields=('gustatus','gucomments','rating')


class happroveform(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = pupload

        # specify fields to be used
        fields = [
            "hocomments",
            "hostatus",
        ]