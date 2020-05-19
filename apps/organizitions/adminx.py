from apps.organizitions.models import CourseOrg,City,Teacher
import xadmin
class CourseOrgAdmin(object):
    list_display = ['id','name','address']
class TeacherAdmin(object):
    list_display = ['id','name','company','job']
class CityAdmin(object):
    list_display = ['name','describe']
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(City,CityAdmin)
xadmin.site.register(Teacher,TeacherAdmin)