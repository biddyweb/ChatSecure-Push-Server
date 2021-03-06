from django.db import models

class PushApplication(models.Model):
    sandbox_mode = models.BooleanField('Sandbox Mode')
    apns_cert = models.TextField('APNS Certificate', null=True, blank=True)
    gcm_api_key = models.TextField('Google Cloud Messaging API Key', null=True, blank=True)
    itunes_shared_secret = models.CharField('iTunes Shared Secret', max_length=50, null=True, blank=True)