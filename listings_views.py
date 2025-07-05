"""
Views for the listings app.
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='get',
    operation_description="Health check endpoint to verify API is running",
    responses={
        200: openapi.Response(
            description="API is healthy",
            examples={
                "application/json": {
                    "status": "healthy",
                    "message": "ALX Travel App API is running successfully"
                }
            }
        )
    }
)
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Health check endpoint to verify the API is running.
    """
    return Response({
        'status': 'healthy',
        'message': 'ALX Travel App API is running successfully'
    }, status=status.HTTP_200_OK)


# Example view structure for future implementation
# from rest_framework import viewsets, generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .models import Listing
# from .serializers import ListingSerializer

# class ListingViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing listing instances.
#     """
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     
#     def get_queryset(self):
#         """
#         Optionally restricts the returned listings to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Listing.objects.all()
#         username = self.request.query_params.get('username')
#         if username is not None:
#             queryset = queryset.filter(owner__username=username)
#         return queryset