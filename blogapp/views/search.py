from django.http.response import HttpResponse
from blogapp.models.Post import Post
from django.db.models import Q
from django.template.loader import render_to_string
from blogapp.models.Setting import Vul
from django.views import View


class searchView(View):
    def get(self, request, *args, **kwargs):

        if self.request.GET["tagId"]:

            query = ""
            tag = ""
            result = []
            xss = Vul.objects.filter(name="XSS").values()[0]["status"]
            sql = Vul.objects.filter(name="SQLI").values()[0]["status"]
            if self.request.method == "GET":
                query = self.request.GET.get("search", None)
                tag = self.request.GET.get("tagId")
                if sql:
                    sqli = (
                        "SELECT * FROM blogapp_post inner  join blogapp_post_tags on blogapp_post.id = blogapp_post_tags.post_id left join blogapp_tags on blogapp_post_tags.tags_id = blogapp_tags.id WHERE title ILIKE '%%"
                        + str(query)
                        + "%%' AND name ILIKE  '%%"
                        + str(tag)
                        + "%%' "
                    )
                    result = Post.objects.raw(sqli)
                else:
                    result = Post.objects.filter(Q(title__icontains=query) & Q(tags__name=tag))

            html = render_to_string(
                "blogapp/search.html", {"query": query, "result": result, "xss": xss, "sql": sql, "tag": tag}
            )

            return HttpResponse(html)

        else:
            query = ""
            result = []
            xss = Vul.objects.filter(name="XSS").values()[0]["status"]
            sql = Vul.objects.get(name="SQLI").status
            if self.request.method == "GET":
                query = self.request.GET.get("search", None)
                if sql:
                    sqli = "SELECT * FROM blogapp_post WHERE title ILIKE '%%" + str(query) + "%%'"
                    result = Post.objects.raw(sqli)
                else:
                    result = Post.objects.raw("SELECT * FROM blogapp_post WHERE title ILIKE  %s", ["%%" + query + "%%"])

            html = render_to_string("blogapp/search.html", {"query": query, "result": result, "xss": xss, "sql": sql})

            return HttpResponse(html)
