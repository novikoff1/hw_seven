from django import forms


class Triangle(forms.Form):
    cath1 = forms.DecimalField()
    cath2 = forms.DecimalField()

    def clean_cath1(self):
        cath1 = self.cleaned_data.get('cath1')
        if cath1 < 0:
            raise forms.ValidationError('Invalid value')
        else:
            return cath1

    def clean_cath2(self):
        cath2 = self.cleaned_data.get('cath2')
        if cath2 < 0:
            raise forms.ValidationError('Invalid value')
        else:
            return cath2
