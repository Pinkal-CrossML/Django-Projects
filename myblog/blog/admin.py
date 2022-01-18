from django.contrib import admin
# 
from blog.models import Blog, Author
 

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
   pass
admin.site.register(Author,AuthorAdmin)



class BlogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blog,BlogAdmin)





