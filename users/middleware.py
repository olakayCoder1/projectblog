from django.shortcuts import redirect



class AuthUserRedirectMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('HELLO WORLD')
        if request.user.is_authenticated and request.path == '/':
            print('YES')
            return redirect('/posts')
        else:
            print('NO')
        response = self.get_response(request)

        return response