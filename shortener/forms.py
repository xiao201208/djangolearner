from django import forms

from .validators import validate_url,validate_dot_com

class SubmitUrlForm(forms.Form):
	url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])

	# def clean(self):
	# 	cleaned_data = super(SubmitUrlForm, self).clean()
	# 	print(cleaned_data)
	# 	url = cleaned_data.get('url')
	# 	url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URl for this field")
	# 	return url
	# 	url = cleaned_data['url']

	# def clean_url(self):
	# 	url = self.cleaned_data['url']
	# 	if not "com" in url:
	# 		raise forms.ValidationError("This is no .com")
	# 	url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URl for this field")
	# 	return url