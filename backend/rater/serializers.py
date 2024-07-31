from rest_framework import serializers
from .models import Product , Rating, Category
from decimal import Decimal




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['uuid', 'name', 'slug', 'creation_date']
        read_only_fields = ['slug']




class ProductSerializer(serializers.HyperlinkedModelSerializer): # display every related model field as a hyperlink in the API output.
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    # category = CategorySerializer() # to replace the ID to Name in json date
    
    category = serializers.HyperlinkedRelatedField(queryset = Category.objects.all(),view_name='category-detail')  # display every related model field as a hyperlink in the API output. 

    class Meta:
        model  = Product
        fields = ['uuid', 'name', 'category' ,'price', 'price_after_tax', 'stock', 'description', 'active' , 'creation_date'] 
        read_only_fields = ['uuid', 'creation_date' , 'slug']
        # depth = 1  # to display all of fields is related for the model.


    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Product name must be at least 3 characters long.")
        return value
    
  
    
    
    def calculate_tax(self, product:Product):
        return product.price * Decimal('1.1') # 10% taxs




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Rating
        fields = ['uuid', 'product', 'user', 'stars'] 

