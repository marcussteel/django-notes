from .models import Student, Path
from rest_framework import serializers
from .models import Student

#   1. yöntem
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get(
#             'first_name', instance.first_name)
#         instance.last_name = validated_data.get(
#             'last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ["id", "first_name", "last_name", "number"]
#         # fields = '__all__'
#         # exclude = ['number']

# Relational fields
# class PathSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Path
#         fields = ["id", "path_name"]


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"





# Delete 0001_initial.py under student_api/migrations
#delete db.sqlite3

#eğer ilişki varsa str dakini getiriyor. yoksa id numarasını getirecekti path in. 
class StudentSerializer(serializers.ModelSerializer):
    path = serializers.StringRelatedField()  # pathi string olarak görmek istiyorsak bunu yazmalııyız str_metodunu buluyor
    path_id = serializers.IntegerField() # burada da hem o pathin id sine hem onun ismine ulaşmış oluyoruz üstteki ile braber yazınca

    class Meta:
        model = Student
        fields = "__all__"

# StringRelatedField
# StringRelatedField may be used to represent the target of the relationship using its str method.
# go to student_api.serializers.py and make below amendments
# path içinde o pathe kayıtlı studentsları görmek istiyorum:


class PathSerializer(serializers.ModelSerializer):
    # students = serializers.StringRelatedField(many=True)

    # path içinde o pathe kayıtlı studentsları görmek istiyorum:
    students = StudentSerializer(many=True)

    # PrimaryKeyRelatedField
    # PrimaryKeyRelatedField may be used to represent the target of the relationship using its primary key.
    # go to student_api.serializers.py and make below amendments
    # students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Path
        fields = "__all__"

# PrimaryKeyRelatedField
# PrimaryKeyRelatedField may be used to represent the target of the relationship using its primary key.
# go to student_api.serializers.py and make below amendments

class PathSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Path
        fields = "__all__"


