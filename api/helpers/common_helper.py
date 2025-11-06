from rest_framework import status as STATUS
from rest_framework.response import Response


def fetch_api_response(
    status=STATUS.HTTP_500_INTERNAL_SERVER_ERROR,
    message="Interval Server Error",
    data=None,
):
    responseObj = {
        "status": status,
        "message": message,
    }

    if data:
        responseObj["data"] = data

    return Response(responseObj)
