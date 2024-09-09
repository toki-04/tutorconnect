from django.contrib import admin
from .models import User, LearnerProfile
# Register your models here.
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(LearnerProfile)
