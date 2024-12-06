from django.db import models

# Model to store health data for each user
class HealthData(models.Model):
    user_id = models.IntegerField()  # For simplicity, using user ID
    metric_type = models.CharField(max_length=50)  # Examples: "Steps", "Heart Rate", "Mood"
    value = models.FloatField()  # Example: steps count or mood score
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.metric_type}: {self.value}"

# Model to store health tips
class HealthTip(models.Model):
    user_id = models.IntegerField()  # The user for whom the tip is generated
    tip = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tip for User {self.user_id}: {self.tip}"





















# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission

# # from .models import CustomUser,HealthData,HealthToken,Appointment

# # class CustomUser(AbstractUser):
# #     is_doctor = models.BooleanField(default=False)
# #     phone = models.CharField(max_length=15, blank=True, null=True)
# #     address = models.TextField(blank=True, null=True)
# class CustomUser(AbstractUser):
#     is_doctor = models.BooleanField(default=False)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)

#     # Avoid conflicts with default User model
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='customuser_groups',  # Changed related_name to avoid clash
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='customuser_permissions',  # Changed related_name to avoid clash
#         blank=True
#     )


# class HealthData(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Related user
#     metric_type = models.CharField(max_length=50)  # Example: "Heart Rate"
#     value = models.FloatField()  # Example: 98.6
#     timestamp = models.DateTimeField(auto_now_add=True)

# class HealthToken(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Fixed here
#     tokens = models.PositiveIntegerField()
#     earned_on = models.DateTimeField(auto_now_add=True)

# class Appointment(models.Model):
#     doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="doctor_appointments")  # Fixed here
#     patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="patient_appointments")  # Fixed here
#     date_time = models.DateTimeField()
#     issue = models.TextField()
#     status = models.CharField(
#         max_length=20,
#         choices=[("Scheduled", "Scheduled"), ("Completed", "Completed")],
#         default="Scheduled"
#     )


# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     is_doctor = models.BooleanField(default=False)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)


# class HealthData(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     metric_type = models.CharField(max_length=50)  # Example: "Steps", "Mood"
#     value = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)


# class HealthTip(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     tip = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)


# class MentalHealthCheckIn(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     mood_score = models.IntegerField()  # Example: 1-10 scale
#     feedback = models.TextField(blank=True, null=True)
#     mindfulness_suggestion = models.TextField(blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)





