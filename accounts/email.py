from django.contrib.auth.tokens import default_token_generator

from djoser.email import ActivationEmail

from djoser import utils
from djoser.conf import settings


# For account activation using email address
class CustomActivationEmail(ActivationEmail):
    template_name = "email/activation.html"

    def get_context_data(self):
        # ActivationEmail can be deleted
        self.context = super().get_context_data()
        user = self.context.get("user")
        self.context["uid"] = utils.encode_uid(user.pk)
        # context["front_end_url"] = djangosettings.FRONTEND_URL
        self.context["token"] = default_token_generator.make_token(user)
        self.context["url"] = settings.ACTIVATION_URL.format(**self.context)
        # get http or https
        self.context["protocol"] = self.request.scheme
        print("***************************************************")
        print(self.context)
        print("***************************************************")
        return self.context

