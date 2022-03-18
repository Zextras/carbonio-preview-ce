# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com
# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com>
#
# SPDX-License-Identifier: AGPL-3.0-only

from typing import Optional

from pydantic import BaseModel

from app.core.schemas.enums.image_quality_enum import ImageQualityEnum
from app.core.schemas.enums.image_type_enum import ImageTypeEnum


class PreviewImageMetadata(BaseModel):
    """
    Class representing all the image information
    """

    version: Optional[int] = 1
    quality: Optional[ImageQualityEnum] = ImageQualityEnum.MEDIUM
    format: Optional[ImageTypeEnum] = ImageTypeEnum.JPEG
    crop: Optional[bool] = False
    height: int
    width: int
