from django import forms

g=[['MALE','MALE'],['FEMALE','FEMALE']]
c=[['PYTHON','PYTHON'],['DJANGO','DJANGO'],['SQL','SQL']]

class NameForm(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #gender=forms.ChoiceField(choices=g)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
 