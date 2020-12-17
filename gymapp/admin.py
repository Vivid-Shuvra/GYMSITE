from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib.auth.models import Group
from .models import Category, Pricing, Features, About, SelfInformation, Contact, Customer, Gallery, Video, Blog, Member, Activity, SubGallery
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}

    class Media:
        css = {
            'all': ("css/main.css",)
        }
        js = ("js/catConfigure.js",)


class PricingAdmin(admin.ModelAdmin):
    list_display = ['duration', 'price', 'item']
    list_filter = ['price']


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class SelfInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'locationTitle', 'phone', 'email', 'time']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    search_fields = ['name', 'email']


class SubGalleryAdmin(admin.TabularInline):
    model = SubGallery
    list_display = ['name', 'imagename']
    list_filter = ['name', 'imagename']


class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        SubGalleryAdmin,
    ]

    class Meta:
        model = Gallery
    list_display = ['name']
    list_filter = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']
    list_filter = ['email']
    search_fields = ['name', 'email']


class MemberAdmin(admin.ModelAdmin):
    list_display = ['customer', 'duration', 'phone', 'address', 'status']
    list_filter = ['customer']
    search_fields = ['duration', 'customer']


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['customer', 'title', 'types', 'duration', 'date']
    list_filter = ['customer']
    search_fields = ['types', 'customer', 'title']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['sno', 'title', 'time', 'status']
    list_filter = ['time', 'status']
    search_fields = ['title']
    date_hierarchy = 'time'
    prepopulated_fields = {'slug': ['title']}
    actions = ['select_posted_blog']
    list_per_page = 5

    class Media:
        css = {
            'all': ("css/main.css",)
        }
        js = ("js/configure.js",)

    def select_posted_blog(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(
            request,  ngettext(
                '%d story was successfully marked as published.',
                '%d stories were successfully marked as published.',
                updated,
            ) % updated, messages.SUCCESS)
    select_posted_blog.short_description = 'Mark the status as published'


admin.site.unregister(Group)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Features, FeatureAdmin)
admin.site.register(About)
admin.site.register(SelfInformation, SelfInfoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(SubGallery)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Video)
