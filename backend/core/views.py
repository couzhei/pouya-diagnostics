"""
Views for the core app
"""

from core import custom_versions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class HelloApp(APIView):
    """
    Oh lala!
    """

    versioning_class = custom_versions.DefaultCoreAppVersion

    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Oh lala!
        """
        return Response(data={"msg": "Hello from the core"})
