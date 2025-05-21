from django.contrib import admin
from api import models

admin.site.register(models.Teacher)
admin.site.register(models.Category)


@admin.register(models.Course)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'price', 'level', 'category', 'teacher', 'featured',
    )
    search_fields = ('title', )
    list_filter = ('category', 'teacher', 'featured', )
    ordering = ('pk', )


class VariantItemTabularInline(admin.TabularInline):
    model = models.VariantItem
    extra = 1  # number of empty forms to display
    fields = (
        'title', 'variant', 'description', 'file', 'duration',
        'content_duration', 'preview', 'variant_item_id', 'date'
    )  # fields to display
    # Optional: you can add more customization
    # readonly_fields = ('title',)
    # can_delete = False


class VariantItemStackedInline(admin.StackedInline):
    model = models.VariantItem
    extra = 1
    fields = (
        'title', 'variant', 'description', 'file', 'duration',
        'content_duration', 'preview', 'variant_item_id', 'date'
    )  # fields to display
    # Optional: you can add more customization
    # filter_horizontal = ('some_many_to_many_field',)


@admin.register(models.Variant)
class VariantAdmin(admin.ModelAdmin):
    ''' Variant Admin '''
    list_display = ('pk', 'title', 'course', )
    list_filter = ('course', )
    search_fields = ('title', )
    inlines = [VariantItemTabularInline, ]


@admin.register(models.VariantItem)
class VariantItemAdmin(admin.ModelAdmin):
    ''' VariantItem Admin '''
    list_display = ('pk', 'title', 'variant', )
    list_filter = ('variant', )
    search_fields = ('title', )

admin.site.register(models.QuestionAnswer)
admin.site.register(models.QuestionAnswerMessage)
admin.site.register(models.Cart)
admin.site.register(models.CartOrder)
admin.site.register(models.CartOrderItem)
# admin.site.register(models.Certificate)
admin.site.register(models.CompletedLesson)
admin.site.register(models.EnrolledCourse)
admin.site.register(models.Note)
admin.site.register(models.Review)
admin.site.register(models.Notification)
admin.site.register(models.Coupon)
admin.site.register(models.Wishlist)
admin.site.register(models.Country)
