from django.contrib import admin

from main.models import Profile, Order, Table, Employee

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    model = Table

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    model = Employee

@admin.register(Order)
class PostAdmin(admin.ModelAdmin):
    model = Order

    # list_display = (
    #     "id",
    #     "title",
    #     "subtitle",
    #     "slug",
    #     "publish_date",
    #     "published",
    # )
    # list_filter = (
    #     "published",
    #     "publish_date",
    # )
    # list_editable = (
    #     "title",
    #     "subtitle",
    #     "slug",
    #     "publish_date",
    #     "published",
    # )
    # search_fields = (
    #     "title",
    #     "subtitle",
    #     "slug",
    #     "body",
    # )
    # prepopulated_fields = {
    #     "slug": (
    #         "title",
    #         "subtitle",
    #     )
    # }
    # date_hierarchy = "publish_date"
    # save_on_top = True