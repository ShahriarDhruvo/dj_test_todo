from dj_rest_auth.serializers import PasswordResetSerializer
# from dj_rest_auth.registration.serializers import VerifyEmailSerializer
from django.conf import settings

# class CustomVerifyEmailSerializer(VerifyEmailSerializer):
#     def save(self):
#         request = self.context.get('request')
#         # Set some values to trigger the send_email method.
#         opts = {
#             'use_https': request.is_secure(),
#             'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
#             'request': request,
#             # here I have set my desired template to be used
#             # don't forget to add your templates directory in settings to be found
#             'email_template_name': 'password_reset_email.html'
#         }

#         # opts.update(self.get_email_options())
#         self.reset_form.save(**opts)

class CustomPasswordResetSerializer(PasswordResetSerializer):
    def save(self):
        request = self.context.get('request')
        
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
            'email_template_name': 'password_reset_email.html'
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)
