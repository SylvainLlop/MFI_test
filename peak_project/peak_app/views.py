import json
from django.shortcuts import render
from rest_framework import viewsets, status, exceptions
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from peak_app.models import Peak
from peak_app.serializers import PeakSerializer


# API to create/read/update/delete a peak
class PeakViewSet(viewsets.ModelViewSet):
    """
    list:
    Retrieves a list of all peaks.

    create:
    Creates a new peak.

    read:
    Retrieves a peak by asking its name.

    update:
    Updates an existing peak with all parameters.

    partial_update:
    Updates an existing peak with selected parameters.

    delete:
    Deletes a peak.
    """
    queryset = Peak.objects.all()
    serializer_class = PeakSerializer
    lookup_field = 'name'


# API to retrieve a list of peaks in a given geographical bounding box
class PeaksInArea(ListAPIView):
    """
    Retrieve a list of peaks in a given geographical bounding box.

    Coordinates have to be given, in integer or floats, in this format :

    latitude1,latitude2,longitude1,longitude2
    """
    serializer_class = PeakSerializer

    # Override queryset to get coordinates given by the user in the URL
    def get_queryset(self):
        # Get all peaks and bounding box
        queryset = Peak.objects.all()
        coords_str = self.kwargs['coords']

        # Set variables
        request_is_valid = True
        error_msg = 'Coordinates have to be given, in integer or floats, in this format :' \
                    'latitude1,latitude2,longitude1,longitude2'
        specific_error_msg = ''

        # Split request by commas
        coords_list = coords_str.split(',')
        if len(coords_list) != 4:
            request_is_valid = False

        else:
            # Test if coordinates are numbers
            try:
                coords_float_list = [float(coord) for coord in coords_list]

            except ValueError:
                request_is_valid = False

            else:
                # Get the four coordinates
                [lat1, lat2, lon1, lon2] = coords_float_list

                # Check if latitudes and longitudes are correct
                if abs(lat1) > 90 or abs(lat2) > 90:
                    request_is_valid = False
                    specific_error_msg = 'Latitudes should be between -90° and 90°'
                if abs(lon1) > 180 or abs(lon2) > 180:
                    request_is_valid = False
                    specific_error_msg = 'Longitudes should be between -180° and 180°'

                lat_min = min(lat1, lat2)
                lat_max = max(lat1, lat2)
                lon_min = min(lon1, lon2)
                lon_max = max(lon1, lon2)

        # Return de filtered queryset if all good
        if request_is_valid:
            queryset = queryset.filter(lat__gte=lat_min).filter(lat__lte=lat_max)
            queryset = queryset.filter(lon__gte=lon_min).filter(lon__lte=lon_max)

            return queryset

        # Return HTTP bad request error otherwise
        else:
            if specific_error_msg == '':
                raise exceptions.ParseError(detail='Error 400. {}'.format(error_msg))
            else:
                raise exceptions.ParseError(detail='Error 400. {}'.format(specific_error_msg))


# View to visualise peaks on a map
def map(request):
    peak_data = list(Peak.objects.all().values())  # use list(), because QuerySet is not JSON serializable
    peak_json = json.dumps(peak_data)
    return render(request, 'peak_app/peaksmap.html', {'data_from_django': peak_json})
