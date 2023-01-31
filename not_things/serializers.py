from rest_framework import serializers
from not_things.models import Not_Thing


class Not_ThingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Not_Thing
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'user')
        