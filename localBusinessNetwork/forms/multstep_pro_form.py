from django import forms


class PersonalInformationForm(forms.Form):
    """Personal information form. This form is used to create a professional profile.

    Attributes:
        avatar: The avatar of the user.
        first_name: The first name of the user.
        last_name: The last name of the user.
        address: The address of the user.
        city: The city of the user.
        state: The state of the user.
        country: The country of the user.
        zipcode: The zipcode of the user.
        phone: The phone number of the user.
        email: The email address of the user.
    """
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zipcode = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class ProfessionalInformationForm(forms.Form):
    """Professional information form. This form is used to create a professional profile.

    Attributes:
        resume: The resume of the user.
        portfolio: The portfolio of the user.
        skills: The skills of the user.
        bio: The bio of the user.
    """
    resume = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    portfolio = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    skills = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))


# Step 3: Professional Information
class ExperienceEducationForm(forms.Form):
    """Experience and education form. This form is used to create a professional profile.

    Attributes:
        experience: The experience of the user.
        education: The education of the user.
        preferences: The preferences of the user.
    """
    experience = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    education = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    preferences = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

