from rest_framework import serializers
from materials.models import Course, Lesson, Quantity, Subscription
from materials.validators import TitleValidator


class QuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Quantity
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    course_quantity = serializers.SerializerMethodField(read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_course_quantity(self, instance):
        quantity_instance = instance.quantity_set.first()
        if quantity_instance:
            return quantity_instance.quantity
        return 0

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [TitleValidator(field='video_link')]

class CourseQuantitySerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Quantity
        fields = ('quantity', 'course')

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
