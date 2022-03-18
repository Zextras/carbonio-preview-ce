# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com
# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com>
#
# SPDX-License-Identifier: AGPL-3.0-only

import logging

from fastapi import APIRouter
import requests
from starlette import status
from starlette.responses import Response

try:
    from unoserver.converter import UnoConverter
except ImportError:
    UnoConverter = ImportError("Couldn't import UnoConverter")

from app.core.resources.constants import service, storage, message
from app.core.resources.constants.settings import (
    NUMBER_OF_WORKERS,
    LIBRE_OFFICE_FIRST_PORT,
)

router = APIRouter(
    prefix=f"/{service.HEALTH_NAME}",
    tags=[service.HEALTH_NAME],
    responses={
        502: {"description": message.STORAGE_UNAVAILABLE_STRING},
        429: {"description": message.LIBRE_OFFICE_NOT_RUNNING},
    },
)
logger = logging.getLogger("Health")


@router.get("/")
async def health() -> dict:
    """
    Checks if the service and all of its dependencies are
    working and returns a descriptive json
    \f
    :return: json with status of service and optional dependencies
    """

    req = f"{storage.FULL_ADDRESS}/{storage.HEALTH_CHECK_API}"
    is_libre_up: bool = _is_unoserver_up()
    try:
        response = requests.get(req, timeout=5)
        response.raise_for_status()
        is_storage_up: bool = True
    except requests.exceptions.RequestException:
        is_storage_up: bool = False

    result_dict = {
        "ready": True if is_libre_up else False,
        "dependencies": [
            {
                "name": "carbonio-storages",
                "ready": is_storage_up,
                "live": is_storage_up,
                "type": "OPTIONAL",
            },
            {
                "name": "libreoffice",
                "ready": is_libre_up,
                "live": is_libre_up,
                "type": "REQUIRED",
            },
        ],
    }
    logger.debug(result_dict)
    return result_dict


@router.get("/ready/")
async def health_ready() -> Response:
    """
    Checks if the service is up and essential dependencies are running correctly
    \f
    :return: returns 200 if service and libreoffice are running
    """
    if _is_unoserver_up():
        logger.debug("Health ready with status code 200")
        return Response(status_code=status.HTTP_200_OK)
    else:
        logger.debug("Health ready with status code 500 (LibreOffice not up)")
        return Response(
            content=message.LIBRE_OFFICE_NOT_RUNNING,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.get("/live/")
async def health_live() -> Response:
    """
    Checks if the service is up
    \f
    :return: returns 200 if the service is up
    """
    logger.debug("Health live with status code 200")
    return Response(status_code=status.HTTP_200_OK)


def _is_unoserver_up() -> bool:
    """
    Private method that checks if all the instances of unoserver are up and running
    :return: True if all the instance are working
    """
    if type(UnoConverter) != ImportError:
        try:
            for curr_server_port in range(0, NUMBER_OF_WORKERS):
                new_port = LIBRE_OFFICE_FIRST_PORT + curr_server_port
                UnoConverter(port=str(new_port))
            return True
        except Exception as e:
            logger.warning(
                f"Encountered the following exception"
                f" while trying to connect to unoserver: {e}"
            )

    return False
