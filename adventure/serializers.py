from rest_framework import serializers

# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes
class Serializer(serializers.Serializer):
    id=serializers.IntegerField(default=0)
    title = serializers.CharField(max_length=50, default="DEFAULT TITLE")
    description = serializers.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    n_to = serializers.IntegerField(default=0)
    s_to = serializers.IntegerField(default=0)
    e_to = serializers.IntegerField(default=0)
    w_to = serializers.IntegerField(default=0)