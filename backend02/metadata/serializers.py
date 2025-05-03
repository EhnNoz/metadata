from rest_framework import serializers
from .models import TitleRecord

class TitleRecordSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    new_title_code = serializers.CharField(read_only=True)
    final_status = serializers.BooleanField(read_only=True)
    base_code = serializers.CharField(read_only=True)
    father_code = serializers.CharField(read_only=True)

    class Meta:
        model = TitleRecord
        fields = [
            'id', 'owner', 'organ', 'MetaTitle', 'MetaContributors', 'MetaPublisher',
            'MetaSubject', 'MetaShotList', 'MetaAppendixInfo', 'MetaContent',
            'MetaDescription', 'MetaSubFeatures', 'MetaShowDate', 'Title',
            'AlbumTitle', 'EpisodeTitle', 'Episodesequence', 'PublishmentStartYear',
            'PublishmentEndYear', 'PublishmentCalendar', 'AgeGroup', 'LangID',
            'EpisodeCount', 'Duration', 'new_title_code', 'final_status',
            'base_code', 'father_code', 'created_at', 'updated_at'
        ]