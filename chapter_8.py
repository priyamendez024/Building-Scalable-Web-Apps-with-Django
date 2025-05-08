
# Chapter 8: Authentication, Authorization & Security

# Example of Django's built-in authentication system and JWT
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions

class LoginView(APIView):
    def post(self, request):
        # Authentication logic and JWT token creation
        token = RefreshToken.for_user(user)
        return Response({'access_token': str(token.access_token)})
    