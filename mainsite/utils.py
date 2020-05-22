import os

from django.conf import settings
from django.core.mail import send_mail
from jinja2 import Environment, FileSystemLoader


def send_mail_from_template(subject, info, path_to_template, to):
    template_dir, template_file = os.path.split(path_to_template)
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = env.get_template(template_file)
    send_mail(
        subject,
        template.render(info),
        settings.EMAIL_HOST_USER,
        to,
        fail_silently=False,
    )
