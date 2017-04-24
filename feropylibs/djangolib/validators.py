# -*- encoding: utf-8 -*-
"""
Some django validators
"""

# Copyright (C) 2011 Luca Ferroni <https://github.com/feroda>
#
# This file is part of feropylibs: "Luca Ferroni Python libs"
# feropylibs is free software: you can redistribute it and/or modify
# it under the terms of the MIT License
#
# feropylibs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# MIT License for more details.

from django.core.validators import validate_email, RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

def multiple_email_validator(value):

    emails = value.split(',')
    for email in emails:
        try:
            validate_email(email.strip())
        except ValidationError as e:
            raise ValidationError(_(u'Enter a valid e-mail address separated by commas.'), code='invalid')

def not_double_quotes(value):
    if '"' in value:
       raise ValidationError(u'Il campo non può contenere virgolette (")', code='invalid')

def alphanumeric(value):

    return RegexValidator(
        regex = "^([a-zA-Z0-9]*)$",
        message = u'il campo può contenere solo lettere e numeri'
    )(value)

def dns_part_valid(value):

    return RegexValidator(
        regex = "^([a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])$",
        message = u'il campo può contenere solo lettere e numeri e "-", ma non può terminare con il "-"'
    )(value)



