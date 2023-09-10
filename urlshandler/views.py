from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect

from .models import ShortUrl
from .serializers import ShortUrlSerializer

from utils.generate_short_url import generate_short_url


class ShortUrlViewSet(ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    permission_classes = [AllowAny]
    lookup_field = 'short_url'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        short_url = generate_short_url()
        ShortUrl.objects.create(
            url=serializer.validated_data['url'],
            short_url= short_url
        )

        data = {
            'short_url': 'https://menucito.app/' + short_url,
            'url': serializer.validated_data['url'],
            'short_code': short_url
        }

        headers = self.get_success_headers(serializer.data)
        return Response(data=data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        print(kwargs)
        short_url = kwargs['short_url']
        short_url_obj = ShortUrl.objects.get(short_url=short_url)
        short_url_obj.visits += 1
        short_url_obj.save()
        return HttpResponseRedirect(short_url_obj.url)
