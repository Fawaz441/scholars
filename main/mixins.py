class SearchMixin(object):
    def get_queryset(self,**kwargs):
        queryset = super(SearchMixin,self).get_queryset(**kwargs)
        if self.request.GET.get('q'):
            name = self.request.GET.get('q')
            queryset = queryset.filter(name__icontains=name)
        return queryset