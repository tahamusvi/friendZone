from django.contrib import admin
from .models import City, User



class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'gender', 'city','birthdateChange')
    list_filter = ('gender', 'city')
    actions = ['change_gender']

    def save_model(self, request, obj, form, change):
        user = obj
        user.gender = form.cleaned_data['gender']
        user.save()

    def change_gender(self, request, queryset):
        queryset.update(gender='f')
    
    def birthdateChange(self,obj):
        return obj.birthdate_shamsi()


    change_gender.short_description = "Change gender to female"

admin.site.register(City)
admin.site.register(User, UserAdmin)