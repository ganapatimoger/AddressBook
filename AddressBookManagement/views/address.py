from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import AddressBook
from ..serializers.address_serializer import AddressBookSerializer
from AddressBookManagement.permissions import UserAddressPermission


class AddressBookViewSet(viewsets.ModelViewSet):
    serializer_class = AddressBookSerializer
    queryset = AddressBook.objects.all()
    permission_classes = [IsAuthenticated, UserAddressPermission]

    def list(self, request, *args, **kwargs):
        address_list = request.user.address_list.all()
        return Response(AddressBookSerializer(address_list, many=True).data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        address = self.get_object()
        serializer = self.get_serializer(instance=address, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        address = self.get_object()
        serializer = self.get_serializer(instance=address, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        address = self.get_object()
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        address = self.get_object()
        serializer = self.get_serializer(address)
        return Response(serializer.data)
