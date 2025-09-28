from rest_framework.serializers import ModelSerializer
from .models import Reporter


class ReporterSerializer(ModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
