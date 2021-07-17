from django.contrib import admin

from .models import Post
from .models import Contact
from .models import Category


class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'featured', 'overview', 'timestamp')

class ContactAdmin(admin.ModelAdmin):
  list_display = ('fullname', 'email', 'subject', 'date')

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
