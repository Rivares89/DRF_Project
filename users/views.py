from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from materials.servises import create_stripe_price, create_stripe_session
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save()
        stripe_price_id = create_stripe_price(payment.course.price)
        payment.payment_link, payment.payment_id = create_stripe_session(stripe_price_id)
        payment.save()

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('lesson', 'course', 'payment_date',)
    ordering_fields = ('payment_date', 'sum',)
    permission_classes = [IsAuthenticated]
