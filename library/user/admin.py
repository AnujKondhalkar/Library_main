from django.contrib import admin

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'username', 'email', 'password')
