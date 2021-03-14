from django import forms

class ChangeStatusForm(forms.Form):
    status = forms.IntegerField()
    todoId = forms.IntegerField()

class AddForm(forms.Form):
    name = forms.CharField(max_length=30)
    memo = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}))