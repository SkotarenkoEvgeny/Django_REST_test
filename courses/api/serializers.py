from rest_framework import serializers

from courses_app.models import Course


class CourseSerializer(serializers.Serializer):
    id =  serializers.ReadOnlyField()
    name = serializers.CharField(max_length=255)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    lectures_amount = serializers.IntegerField()

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get(
            'start_date', instance.start_date
            )
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.lectures_amount = validated_data.get(
            'lectures_amount', instance.lectures_amount
            )
        instance.save()

        return instance

    def validate(self, data):

        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "end date must occur after "
                "start date"
                )

        if data['lectures_amount'] <= 0:
            raise serializers.ValidationError(
                "lectures_amount must be greater than 0"
                )

        return data
