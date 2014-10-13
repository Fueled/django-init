from emailtools import HTMLEmail as _HTMLEmail

try:
    from premailer import transform
except ImportError:
    transform = None


class HTMLEmail(_HTMLEmail):
    """
    Email class for using template rendering for the email template.
    If premailer is installed this is a enhancement over the default HTMLEmail Class of django-email-tools.
    """

    def get_rendered_template(self):
        if transform:
            return transform(super(HTMLEmail, self).get_rendered_template())

        return super(HTMLEmail, self).get_rendered_template()
