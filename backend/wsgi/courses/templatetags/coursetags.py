from django import template
from courses.models import TaskSubmission, Registration
register = template.Library()


@register.filter(name='solved')
def solved(task, user):
    return TaskSubmission.objects.filter(submitted_by=user,
                                         task=task,
                                         valid=True).exists()


@register.filter(name='granted_access')
def granted_access(course, user):
    return Registration.objects.filter(course=course,
                                       user=user,
                                       granted=True).exists()


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
