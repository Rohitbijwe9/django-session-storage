from rest_framework import serializers
from .models import Products



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Products
        fields='__all__'

#django admin commonds
#postgres--pgadmin for like workbench
#viweset
#array field
#nastedserializers
#django celery
#admin filter
#one to one, one to many,many to many
#single field validation widgets in serializer
#serial specific function
#revise orm
#exception on views


