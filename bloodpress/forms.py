from django import forms
from .models import Response


class SurveyForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in questions:
            self.fields[str(question.id)] = forms.CharField(
                label=question.question_text,
                widget=forms.TextInput(attrs={'class': 'form-control'})
            )


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['pressure_result']
        labels = {
            'pressure_result': 'Wynik ciśnienia (mmHg)',
        }
        widgets = {
            'pressure_result': forms.NumberInput(attrs={'class': 'form-control'}),
        }
