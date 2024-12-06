from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import HealthData, HealthTip
from .serializers import HealthDataSerializer, HealthTipSerializer

class HealthDataViewSet(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer
    permission_classes = [AllowAny]  # No authentication required

class HealthTipViewSet(viewsets.ModelViewSet):
    queryset = HealthTip.objects.all()
    serializer_class = HealthTipSerializer
    permission_classes = [AllowAny]  # No authentication required

    def create(self, request, *args, **kwargs):
        # Get user_id from the request body
        user_id = request.data.get('user_id', None)
        if user_id is None:
            return Response({"error": "user_id is required."}, status=400)

        # Retrieve the most recent health data for the user
        recent_data = HealthData.objects.filter(user_id=user_id).order_by('-timestamp').first()

        if not recent_data:
            return Response({"error": "No health data available for this user."}, status=400)

        # Generate health tip based on the health data
        health_tip = self.generate_health_tip(recent_data)

        # Create the health tip object
        health_tip_obj = HealthTip.objects.create(user_id=user_id, tip=health_tip)

        # Return the generated health tip
        return Response({"id": health_tip_obj.id, "tip": health_tip_obj.tip, "user_id": user_id}, status=201)

    def generate_health_tip(self, health_data):
        """Generate a personalized health tip based on user data."""
        if health_data.metric_type == "Steps":
            if health_data.value < 5000:
                return "Your activity level is low. Try to walk at least 10,000 steps daily."
            else:
                return "Great job! You're staying active. Keep it up with daily exercise."

        elif health_data.metric_type == "Heart Rate":
            if health_data.value > 100:
                return "Your heart rate seems high. Consider relaxation exercises or check with a healthcare provider."
            else:
                return "Your heart rate is normal. Keep up with your healthy lifestyle."

        elif health_data.metric_type == "Mood":
            if health_data.value < 5:
                return "It seems you're feeling down. Try mindfulness exercises or relaxation techniques."
            else:
                return "You're in a good mood! Keep up with your positive mindset."

        return "Stay hydrated and keep maintaining a healthy lifestyle!"








