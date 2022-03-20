from  rest_framework import serializers
from  otoKlixTestApp.models import otoCrud

class otoCrudSerializer(serializers.ModelSerializer):
   
    class Meta:
            model=otoCrud
            fields=('__all__')
