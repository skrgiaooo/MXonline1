from django.shortcuts import render
from django.views.generic import View
from apps.organizitions.models import City,CourseOrg,Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
class OrgView(View):
    def get(self,request,*args,**kwargs):
        """
        展示授课机构列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        all_orgs = CourseOrg.objects.all()
        org_nums = CourseOrg.objects.all().count()
        all_citys = City.objects.all()
        return render(request,'org-list.html',
                      {'all_orgs':all_orgs,'org_nums':org_nums,'all_citys':all_citys})
        # all_orgs = CourseOrg.objects.all()
        # all_city = City.objects.all()
        # category = request.GET.get("ct",'')
        # hot_orgs = all_orgs.order_by('-click_num')[:3]
        # if category:
        #     all_orgs = all_orgs.filter(category = category)
        # city_id = request.GET.get('city','')
        # city_name = ''
        # if city_id:
        #     city = City.objects.get(id=int(city_id))
        #     city_name = city_name
        #     if city_id.isdight():
        #         all_orgs = all_orgs.filter(city__id=city_id)
        # sort = request.GET.get('sort','')
        # if sort:
        #     all_orgs = all_orgs.order_by(sort)
        # org_nums = all_orgs.count()
        # try:
        #     page = request.GET.get('page',1)
        # except PageNotAnInteger:
        #     page = 1
        # p = Paginator(all_orgs,per_page=10,request=request)
        return render(request,'org-list.html')
class AddAsk(View):
    def post(self,request,*args,**kwargs):
        return render(request,'org-list.html')