from django import forms

from .validators import validate_url
# , validate_dot_com
class SubmitUrlForm(forms.Form):
    url = forms.CharField(label = 'Submit URL',validators=[validate_url],
                            widget = forms.TextInput(
                            attrs = {
                                "placeholder" : "URL to be shortened",
                                "class" : "form-control"
                            }
                            ))

#    def clean(self):
#        cleaned_data = super(SubmitUrlForm, self).clean()
#        url = cleaned_data['url']
#        print(url)


#    def clean_url(self):
##        if "http" in url:
##        return "http://" +url
