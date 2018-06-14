from django.utils.translation import gettext_lazy as _


'''
Subscriber Constants
'''


class Status:
    PENDING = 1
    SUBSCRIBED = 2
    UNSUBSCRIBED = 3
    CLEANED = 4

    LABELS = {
        PENDING: _('Pending'),
        SUBSCRIBED: _('Subscribed'),
        UNSUBSCRIBED: _('Unsubscribed'),
        CLEANED: _('Cleaned'),
    }

    CHOICES = tuple(LABELS.items())


'''
Activity Constants
'''


class ActivityTypes:
    SUBSCRIBED = 1
    UNSUBSCRIBED = 2
    SENT = 3
    OPENED = 4
    CLICKED = 5

    LABELS = {
        SUBSCRIBED: _('Subscribed'),
        UNSUBSCRIBED: _('Unsubscribed'),
        SENT: _('Was sent'),
        OPENED: _('Opened'),
        CLICKED: _('Clicked'),
    }

    CHOICES = tuple(LABELS.items())


'''
Form Template Constants
'''


class TemplateTypes:
    EMAIL = 1
    PAGE = 2

    LABELS = {
        EMAIL: _('Email'),
        PAGE: _('Page'),
    }

    CHOICES = tuple(LABELS.items())


class Workflows:
    SUBSCRIPTION = 1
    UNSUBSCRIPTION = 2

    LABELS = {
        SUBSCRIPTION: _('Subscription'),
        UNSUBSCRIPTION: _('Unsubscription'),
    }

    CHOICES = tuple(LABELS.items())


class TemplateKeys:
    """
    Key identifiers of the FormTemplate's instances.
    Constants are dashed-strings because they are also used
    as URL args in the views.
    """

    # Subscription workflow
    SUBSCRIBE_PAGE = 'subscribe'
    SUBSCRIBE_THANK_YOU_PAGE = 'subscribe-thank-you'
    CONFIRM_EMAIL = 'confirm-email'
    CONFIRM_THANK_YOU_PAGE = 'confirm-thank-you'
    WELCOME_EMAIL = 'welcome-email'

    # Unsubscription workflow
    UNSUBSCRIBE_PAGE = 'unsubscribe'
    UNSUBSCRIBE_SUCCESS_PAGE = 'unsubscribe-success'
    GOODBYE_EMAIL = 'goodbye-email'

    LABELS = {
        SUBSCRIBE_PAGE: _('Subscribe page'),
        SUBSCRIBE_THANK_YOU_PAGE: _('Subscribe thank you page'),
        CONFIRM_EMAIL: _('Opt-in confirm email'),
        CONFIRM_THANK_YOU_PAGE: _('Opt-in confirm thank you page'),
        WELCOME_EMAIL: _('Final welcome email'),
        UNSUBSCRIBE_PAGE: _('Unsubscribe page'),
        UNSUBSCRIBE_SUCCESS_PAGE: _('Unsubscribe success page'),
        GOODBYE_EMAIL: _('Goodbye email'),
    }

    CHOICES = tuple(LABELS.items())
