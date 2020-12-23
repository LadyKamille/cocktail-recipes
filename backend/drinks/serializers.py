from rest_framework import serializers

from drinks.models import Drinks


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = '__all__'