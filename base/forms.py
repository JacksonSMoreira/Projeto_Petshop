from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=11)
    mensagem = forms.CharField(widget=forms.Textarea)