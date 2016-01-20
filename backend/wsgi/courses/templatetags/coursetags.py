from django import template
from courses.models import Registration
register = template.Library()

@register.filter(name='registered_kids')
def registered_kids(course):
    return registered_role(course, Registration.KID)


@register.filter(name='registered_reserve')
def registered_reserves(course):
    return registered_role(course, Registration.RESERVE)


@register.filter(name='registered_master')
def registered_master(course):
    return registered_role(course, Registration.CODE_MASTER)


def registered_role(course, role):
    return Registration.objects.filter(course=course,
                                       role=role).count()
