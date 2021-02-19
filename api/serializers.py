from rest_framework import serializers	
from .models import Test


class TestSerializers(serializers.ModelSerializer):
	class Meta:
		model = Test
		fields = '__all__'



# class DemoSerializer(serializers.Serializer):
# 	zip_code = serializers.CharField(max_length=10)
# 	city = serializers.CharField(max_length=10)
# 	age = serializers.IntegerField()

# 	def __str__(self):
# 		return "DemoSerializer object"