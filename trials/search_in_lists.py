def find_where(items, search_request):
    default = object()
    for item in items:
        for key, value in search_request.items():
            if item.get(key, default) != value:
                break
        else:
            return item
