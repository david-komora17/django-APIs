from rest_framework import serializers
from .models import Book  # This line fixes the "NameError: name 'Book' is not defined"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_ISBN(self, value):
        """Custom validation for ISBN format length."""
        if len(value) not in (10, 13):
            raise serializers.ValidationError("ISBN must be exactly 10 or 13 characters long.")
        return value
