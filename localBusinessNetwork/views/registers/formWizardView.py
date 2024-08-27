from formtools.wizard.views import SessionWizardView
from localBusinessNetwork.forms.multstep_pro_form import (
    PersonalInformationForm, ProfessionalInformationForm, ExperienceEducationForm)
from django.shortcuts import redirect
from django.utils import timezone
from localBusinessNetwork.models.professional_profile import ProfessionalProfile
from localBusinessNetwork.models.users import LbnUser
from django.core.files.storage import default_storage


FORMS = [("personal", PersonalInformationForm),
         ("professional", ProfessionalInformationForm),
         ("experience_education", ExperienceEducationForm)]

TEMPLATES = {
    "personal": "registers/personal_information.html",
    "professional": "registers/professional_information.html",
    "experience_education": "registers/experience_education.html",
}



class ProfileWizard(SessionWizardView):
    """This class is used to create a professional profile using a wizard form.

    Attributes:
        form_list: The list of forms to be used in the wizard.
        template_name: The name of the template to be used for the wizard.
    """
    form_list = FORMS
    template_name = "registers/form_wizard.html"

    file_storage = default_storage

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        # Collect data from all the forms
        personal_data = form_list[0].cleaned_data  # Data from PersonalInformationForm
        professional_data = form_list[1].cleaned_data  # Data from ProfessionalInformationForm
        experience_education_data = form_list[2].cleaned_data  # Data from ExperienceEducationForm

        # Combine all the data
        combined_data = {**personal_data, **professional_data, **experience_education_data}

        # Get the current user (assuming user is authenticated)
        user = self.request.user

        # Create or update the ProfessionalProfile instance
        profile, created = ProfessionalProfile.objects.update_or_create(
            jobseeker=user,  # Assuming `jobseeker` is a foreign key to the user
            defaults={
                'first_name': combined_data['first_name'],
                'last_name': combined_data['last_name'],
                'address': combined_data['address'],
                'city': combined_data['city'],
                'state': combined_data['state'],
                'country': combined_data['country'],
                'zipcode': combined_data['zipcode'],
                'phone': combined_data['phone'],
                'email': combined_data['email'],
                'skills': combined_data['skills'],
                'bio': combined_data['bio'],
                'experience': combined_data['experience'],
                'education': combined_data['education'],
                'preferences': combined_data['preferences'],
                'avatar': combined_data.get('avatar'),
                'resume': combined_data.get('resume'),
                'portfolio': combined_data.get('portfolio'),
                'updated_at': timezone.now(),
            }
        )

        return redirect('professional_profile')
