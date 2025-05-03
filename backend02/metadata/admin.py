from django.contrib import admin
from .models import YourOrganModel, TitleRecord

@admin.register(YourOrganModel)
class YourOrganModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(TitleRecord)
class TitleRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'Title', 'owner', 'MetaTitle', 'organ', 'new_title_code', 'final_status'
    )
    list_filter = ('final_status', 'organ')
    search_fields = ('Title', 'new_title_code')
    readonly_fields = ('new_title_code', 'created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        ro = list(self.readonly_fields)
        # non-superusers cannot edit admin-only fields
        if not request.user.is_superuser:
            ro += ['final_status', 'base_code', 'father_code']
        return ro

    def has_delete_permission(self, request, obj=None):
        # prevent deletion if final_status=True for non-superusers
        if obj and obj.final_status and not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)