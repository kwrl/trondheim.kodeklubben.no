from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)

        def restore_object(self, attrs, instance=None):
            user = super(UserSerializer, self).restore_object(attrs, instance)
            user.set_password(attrs['password'])
            return user

    def validate_email(self, attrs, source):
        if User.objects.filter(email=attrs[source]).exists():
            print("Derp")
            raise serializers.ValidationError('A user with that email is already registered')
        print("Noderp")
        return attrs
