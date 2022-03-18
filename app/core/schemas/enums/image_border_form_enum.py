# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com
# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com>
#
# SPDX-License-Identifier: AGPL-3.0-only

from enum import Enum


class ImageBorderShapeEnum(str, Enum):
    """
    Class representing all the image type accepted values
    """

    ROUNDED = "rounded"

    RECTANGULAR = "rectangular"
