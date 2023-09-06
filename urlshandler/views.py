from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import ShortUrl
from .serializers import ShortUrlSerializer

from utils.generate_short_url import generate_short_url


class ShortUrlViewSet(ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        short_url = generate_short_url()
        ShortUrl.objects.create(
            url = serializer.validated_data['url'],
            short_url = 'https://menucito.app/' + short_url
        )

        data = {
            'short_url': 'https://menucito.app/' + short_url,
            'url': serializer.validated_data['url']
        }

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
