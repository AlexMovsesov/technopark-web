from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class Paginate:
    def __init__(self, objects, on_page = 5):
        self.paginator = Paginator(objects, on_page)

    def paginate(self, page = 1):
        try:
            self.objects = self.paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            self.objects = self.paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            self.objects = self.paginator.page(self.paginator.num_pages)
        return self.objects