import json
from rest_framework.decorators import api_view
from rest_framework import status as STATUS
from api.helpers.common_helper import fetch_api_response


@api_view(["GET"])
def fetch_status(Request):
    return fetch_api_response(
        status=STATUS.HTTP_200_OK,
        message="Server UP And Running !!",
    )
