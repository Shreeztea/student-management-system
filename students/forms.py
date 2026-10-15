
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'address', 'course', 'document', 'profile_picture']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_age(self):
        age = self.cleaned_data['age']
        if age > 30:
            raise forms.ValidationError("Age cannot be greater than 30.")
        return age

    def clean(self):
        cleaned_data = super().clean()

        age = cleaned_data.get("age")
        address = cleaned_data.get("address").lower() if cleaned_data.get("address") else None

        if age and age < 18 and address != "kathmandu":
            raise forms.ValidationError(
                "Students under 18 should be in Kathmandu to study."
            )

        return cleaned_data