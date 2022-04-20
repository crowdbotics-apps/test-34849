from rest_framework import authentication
from partners.models import Partner
from .serializers import PartnerSerializer
from rest_framework import viewsets


class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Partner.objects.all()
