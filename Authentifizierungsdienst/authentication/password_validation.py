import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext


class RegexpValidator:
    def __init__(self, number_of_changes=5):
        self.number_of_changes = number_of_changes

    def validate(self, password, user):
        char_classes = {
            "lower_case": r'[a-z]',
            "upper_case": r'[A-Z]',
            "digit": r'[0-9]',
            "special_char": r'[^a-zA-Z0-9]',
        }

        def get_char_class(char, char_classes: dict):
            for char_class in char_classes.keys():
                if re.search(char_classes[char_class], char):
                    return char_class
            raise ValueError("The \"%s\" character cannot be evaluated by the RegexpValidator." % char)

        previous_char_class = ""
        changes = 0
        for c in password:
            if previous_char_class == get_char_class(c, char_classes):
                continue
            previous_char_class = get_char_class(c, char_classes)
            changes += 1
            if changes - 1 >= self.number_of_changes:
                return
        raise ValidationError(
            gettext("This password must contain at least %(number_of_changes)d number of changes between" +
                    " uppercase letters, lowercase letters, numbers, or special characters."),
            code='password_too_uncomplex',
            params={'number_of_changes': self.number_of_changes},
        )

    def get_help_text(self):
        return gettext("The password must contain at least %d number of changes between" +
                       " uppercase letters, lowercase letters, numbers, or special characters."
                       % self.number_of_changes)
