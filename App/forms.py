from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        # We define which fields from the model should be in the form
        fields = ['name', 'location', 'phone_number', 'score', 'extra_info_1', 'extra_info_2']

    def __init__(self, *args, **kwargs):
        """
        This is the magic part. This function runs when the form is created.
        It loops through all the form fields and adds the 'form-control'
        Bootstrap class to each one, which makes them look beautiful.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            # Optional: Add placeholder text to the fields
            if field_name == 'name':
                field.widget.attrs['placeholder'] = 'e.g., John Doe'
            if field_name == 'location':
                field.widget.attrs['placeholder'] = 'e.g., Thrissur'
            if field_name == 'phone_number':
                field.widget.attrs['placeholder'] = 'e.g., 9876543210'
            if field_name == 'score':
                field.widget.attrs['placeholder'] = 'Enter score after assembly'
