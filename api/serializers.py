from rest_framework import serializers
from .models import Task


# serializers allows us return any object model into a json response
# here we can serialize any form of data but using 'ModelSerializer' we're serializing the model.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # 'Task' beign the model that we want to serialize
        model = Task
        # the feilds we wanna see and I said all below
        fields = '__all__'
