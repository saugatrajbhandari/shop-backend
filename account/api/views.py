from django.contrib.auth import get_user_model
from account.serializers import UserRegistrationSerializer
from rest_framework.generics import CreateAPIView

class UserRegistrationView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer