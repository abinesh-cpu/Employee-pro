from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

# Password Reset Request Form
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No account is associated with this email address.")
        return email


# Password Set Form (for resetting the password)
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput,
        strip=False,
        help_text="Your password can't be too similar to your other personal information. It must contain at least 8 characters, and can't be a commonly used password.",
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput,
        strip=False,
    )
    
    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')

        if password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        
        # Optionally, you can apply Django's password validation here
        password_validation.validate_password(password1, self.user)
        
        return password2