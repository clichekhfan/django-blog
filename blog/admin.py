from django.contrib import admin
from blog.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'posts', )
    exclude = ("posts",)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    # fields = ('title', 'text', 'author', 'created_date', 'modified_date', 'published_date', )
    inlines = [
        CategoryInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
