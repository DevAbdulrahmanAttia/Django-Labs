from django import forms

from .models import Trainee


class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'age', 'email', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['course'].required = False
        self.fields['course'].widget.attrs['class'] = 'form-select'

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Name is required.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise forms.ValidationError('Email is required.')
        return email

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            return age
        if age <= 0:
            raise forms.ValidationError('Age must be a positive number.')
        return age
