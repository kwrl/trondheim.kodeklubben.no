from rest_framework import serializers

from .models import Course, Registration

class CourseHeaderSerializer(serializers.Serializer):
    pk      = serializers.Field()
    name    = serializers.CharField()
    registration_limit  = serializers.IntegerField()
    
    def restore_object(self, attrs, instance=None):
        if not instance:
            return Course(**attrs)

        instance.pk     = attrs.get('pk', instance.pk)
        instance.name   = attrs.get('name', instance.name)
        instance.registration_limit = attrs.get('registration_limit', instance.registration_limit)

        return instance


class CourseFullSerializer(serializers.Serializer):
    pk      = serializers.Field()
    name    = serializers.CharField()
    desc    = serializers.CharField()

    registration_start  = serializers.DateTimeField()
    registration_end    = serializers.DateTimeField()

    registration_limit  = serializers.IntegerField()
    
    def restore_object(self, attrs, instance=None):
        if not instance:
            return Course(**attrs)

        instance.pk     = attrs.get('pk', instance.pk)
        instance.name   = attrs.get('name', instance.name)
        instance.desc   = attrs.get('desc', instance.desc)
        
        instance.registration_start = attrs.get('registration_start', instance.registration_start)
        instance.registration_end   = attrs.get('registration_end', instance.registration_end)
        instance.registration_limit = attrs.get('registration_limit', instance.registration_limit)

        return instance
