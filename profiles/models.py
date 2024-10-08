from django.db import models
from U_auth.models import UserPersonalDetails, costume_user
# Create your models here.


# ..............Target user profile flow model here.............................

class InterestRequest(models.Model):
    sender=models.ForeignKey(costume_user, related_name="sent_requests", on_delete=models.CASCADE)
    receiver=models.ForeignKey(costume_user, related_name="received_requests", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.status}"
    
class Shortlist(models.Model):
    user = models.ForeignKey(costume_user, related_name='shortlists', on_delete=models.CASCADE)  # The user who shortlists
    shortlisted_user = models.ForeignKey(costume_user, related_name='shortlisted_by', on_delete=models.CASCADE)  # The shortlisted user
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} shortlisted {self.shortlisted_user.username}"
