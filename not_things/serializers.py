from rest_framework import serializers
from not_things.models import Not_Thing


class Not_ThingSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'user')
        model = Not_Thing
