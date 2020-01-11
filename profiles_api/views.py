from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self,request,format=None):
        an_apiview = [
            'Mocha',
            'Latte',
            'Espresso',
        ]

        return Response({'message':'Hello World','an_apiview':an_apiview})
