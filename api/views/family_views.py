from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.family import Family
from ..serializers import FamilySerializer

# Create your views here.
class Families(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = FamilySerializer
    def get(self, request):
        """Index request"""
        # Get all the families:
        # families = Family.objects.all()
        # Filter the familys by owner, so you can only see your owned familys
        families = Family.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = FamilySerializer(families, many=True).data
        return Response({ 'families': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['family']['owner'] = request.user.id
        # Serialize/create family
        family = FamilySerializer(data=request.data['family'])
        # If the family data is valid according to our serializer...
        if family.is_valid():
            # Save the created family & send a response
            family.save()
            return Response({ 'family': family.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(Family.errors, status=status.HTTP_400_BAD_REQUEST)

class FamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the family to show
        family = get_object_or_404(Family, pk=pk)
        # Only want to show owned families?
        if request.user != family.owner:
            raise PermissionDenied('Unauthorized, you do not own this family')

        # Run the data through the serializer so it's formatted
        data = FamilySerializer(family).data
        return Response({ 'family': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate family to delete
        family = get_object_or_404(Family, pk=pk)
        # Check the family's owner against the user making this request
        if request.user != family.owner:
            raise PermissionDenied('Unauthorized, you do not own this family')
        # Only delete if the user owns the  family
        family.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Family
        # get_object_or_404 returns a object representation of our Family
        family = get_object_or_404(Family, pk=pk)
        # Check the family's owner against the user making this request
        if request.user != family.owner:
            raise PermissionDenied('Unauthorized, you do not own this family')

        # Ensure the owner field is set to the current user's ID
        request.data['family']['owner'] = request.user.id
        # Validate updates with serializer
        data = FamilySerializer(family, data=request.data['family'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
