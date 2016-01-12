from .models import Course, Registration
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    kids_signed_up = serializers.SerializerMethodField()
    reserves_signed_up = serializers.SerializerMethodField()
    masters_signed_up = serializers.SerializerMethodField()

    def get_kids_signed_up(self, course):
        return self.get_role_signed_up(course, Registration.KID)

    def get_reserves_signed_up(self, course):
        return self.get_role_signed_up(course, Registration.RESERVE)

    def get_masters_signed_up(self, course):
        return self.get_role_signed_up(course, Registration.CODE_MASTER)

    def get_role_signed_up(self, course, role):
        return Registration.objects.filter(course=course, role=role).count()

    class Meta:
        model = Course


