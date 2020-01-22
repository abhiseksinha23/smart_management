from django.contrib import admin
from .models import quaries, faculties, students, centers, fee, rankers
# Register your models here.
class quariesAdmin(admin.ModelAdmin):
    search_fields = ['created_data', 'subject', 'author']
    list_filter = [ 'created_data']
    list_display = ['author', 'subject', 'created_data']
class studentsAdmin(admin.ModelAdmin):
    search_fields = ['name', 'fathername', 'joinyear', 'program', 'center']
    list_filter = [ 'joinyear', 'program', 'center', 'feestatus']
    list_display = ['name', 'joinyear', 'program', 'center',]
class facultiesAdmin(admin.ModelAdmin):
    search_fields = ['name', 'subject', 'center', 'position']
    list_filter = [ 'subject', 'center', 'position']
    list_display = ['name', 'subject', 'position', 'center',]
class centersAdmin(admin.ModelAdmin):
    search_fields = ['name', 'place']
    list_filter = [ 'place', 'name']
    list_display = ['name', 'place']
class feeAdmin(admin.ModelAdmin):
    search_fields = ['course', 'years', 'type']
    list_filter = [ 'course', 'type', 'years']
    list_display = ['course', 'type', 'years']
class rankersAdmin(admin.ModelAdmin):
    search_fields = ['name','rank', 'achievement']
    list_filter = [ 'program', 'achievement']
    list_display = ['name', 'rank', 'achievement']
admin.site.register(quaries, quariesAdmin)
admin.site.register(faculties, facultiesAdmin)
admin.site.register(students, studentsAdmin)
admin.site.register(centers, centersAdmin)
admin.site.register(fee, feeAdmin)
admin.site.register(rankers, rankersAdmin)
