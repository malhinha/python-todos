# Import custom models
from .models import Todo
# If you need authentication, import these guys
from django.contrib.auth.models import User, Group
# Where the magic happens to get hyperlinks
from rest_framework import serializers

# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Todo
        # the fields that should be included in the serialized output
        # can be a subset of all fields in model, i.e. need not be exhaustive
        fields = ['id', 'subject', 'details']
