def base1(request):
    user = request.user
    u = User.objects.get(username=user)
    us = u.User.first_name
    context = {'u': u, 'us': us}
    return render(request, "backend/base.html", context)


def base(request, id):
    if user.is_authenticated:
        obj = User.objects.get(pk=id)
        username = obj.username
    else:
        username = "Hello Guest!"
    return render(request, 'books/base.html', {'username': username})
