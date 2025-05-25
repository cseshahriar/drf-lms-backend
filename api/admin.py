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
    list_display = ('pk', 'order', 'title', 'course', )
    list_filter = ('course', )
    search_fields = ('title', )
    ordering = ('order', )
    inlines = [VariantItemTabularInline, ]
    list_editable = ('order', )


@admin.register(models.VariantItem)
class VariantItemAdmin(admin.ModelAdmin):
    ''' VariantItem Admin '''
    list_display = (
        'pk', 'order', 'title', 'variant', 'duration', 'content_duration')
    list_filter = ('variant', )
    search_fields = ('title', )
    ordering = ('order', )
    list_editable = ('order', 'content_duration', )


@admin.register(models.QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'course', 'user', 'title', 'qa_id', 'date', )
    search_fields = ('title', )
    list_filter = ('course', 'user')


@admin.register(models.QuestionAnswerMessage)
class QuestionAnswerMessageAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'course', 'question', 'user', 'message', 'qam_id', 'qa_id',
        'date'
    )
    search_fields = ('qam_id', 'qa_id', )
    list_filter = ('course', 'question', 'user')


admin.site.register(models.Cart)
admin.site.register(models.CartOrder)
admin.site.register(models.CartOrderItem)
# admin.site.register(models.Certificate)
admin.site.register(models.CompletedLesson)
admin.site.register(models.EnrolledCourse)
admin.site.register(models.Note)


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'user', 'course', 'rating', 'review', 'reply', 'active', 'date'
    )
    search_fields = ('user__username', 'course__title')
    list_filter = ('course', )


admin.site.register(models.Notification)
admin.site.register(models.Coupon)
admin.site.register(models.Wishlist)
admin.site.register(models.Country)
