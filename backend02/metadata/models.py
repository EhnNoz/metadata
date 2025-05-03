import secrets
from django.conf import settings
from django.db import models

class YourOrganModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # سایر فیلدهای ارگان

class TitleRecord(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organ = models.ForeignKey(YourOrganModel, on_delete=models.PROTECT)

    # Meta fields
    MetaTitle = models.CharField(max_length=255)
    MetaContributors = models.TextField(blank=True)
    MetaPublisher = models.CharField(max_length=255, blank=True)
    MetaSubject = models.CharField(max_length=255, blank=True)
    MetaShotList = models.TextField(blank=True)
    MetaAppendixInfo = models.TextField(blank=True)
    MetaContent = models.TextField(blank=True)
    MetaDescription = models.TextField(blank=True)
    MetaSubFeatures = models.TextField(blank=True)
    MetaShowDate = models.DateField(null=True, blank=True)
    Title = models.CharField(max_length=255)
    AlbumTitle = models.CharField(max_length=255, blank=True)
    EpisodeTitle = models.CharField(max_length=255, blank=True)
    Episodesequence = models.IntegerField(null=True, blank=True)
    PublishmentStartYear = models.IntegerField(null=True, blank=True)
    PublishmentEndYear = models.IntegerField(null=True, blank=True)
    PublishmentCalendar = models.CharField(max_length=50, blank=True)
    AgeGroup = models.CharField(max_length=50, blank=True)
    LangID = models.CharField(max_length=50, blank=True)
    EpisodeCount = models.IntegerField(null=True, blank=True)
    Duration = models.DurationField(null=True, blank=True)

    # Controlled by admin only
    final_status = models.BooleanField(default=False)
    base_code = models.CharField(max_length=100, blank=True)
    father_code = models.CharField(max_length=100, blank=True)

    # Generated for user on creation
    new_title_code = models.CharField(max_length=32, unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.new_title_code:
            self.new_title_code = secrets.token_hex(16)  # 32 chars
        super().save(*args, **kwargs)