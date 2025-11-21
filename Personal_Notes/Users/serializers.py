
from rest_framework import serializers

from Users.models import Note, user

import jdatetime

class user_serializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["id","email","password","phone_number","date_joined"]

class NoteSerializer(serializers.ModelSerializer):
    #owner = user_serializers(read_only=True,source='user')

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result["owner"] = user_serializers(instance.owner).data
        
        
        return result

    class Meta:
        model = Note
        fields = ["id", "title", "data", "created_date", "updated_date", "owner"]
    






