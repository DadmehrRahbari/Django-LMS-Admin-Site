from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]
    
class InstructorAdmin(admin.ModelAdmin):
    fields = #<HINT> add user, full_time field names here#

class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5



admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)



