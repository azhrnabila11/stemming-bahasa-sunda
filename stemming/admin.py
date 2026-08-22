from django.contrib import admin
from .models import KamusSunda, KamusStopword, StemmingResult
from import_export.admin import ImportExportModelAdmin 

# Buat pengaturan khusus agar KamusSunda punya tombol Import
class KamusSundaAdmin(ImportExportModelAdmin):
    pass

class KamusStopwordAdmin(ImportExportModelAdmin):
    pass

admin.site.register(KamusSunda, KamusSundaAdmin)
admin.site.register(KamusStopword, KamusStopwordAdmin)
admin.site.register(StemmingResult)