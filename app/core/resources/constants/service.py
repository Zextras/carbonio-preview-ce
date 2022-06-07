# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com
# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com>
#
# SPDX-License-Identifier: AGPL-3.0-only

from app.core.resources.config_loader import read_config


# SERVICE CONFIG
service_section_name: str = "service"
NAME: str = read_config(section=service_section_name, value="name")
TIMEOUT: int = int(read_config(section=service_section_name, value="timeout"))
IP: str = read_config(section=service_section_name, value="ip")
PORT: str = read_config(section=service_section_name, value="port")

DESCRIPTION = """
Preview service. 🚀 \n
You can preview the following type of files:

* **images(png/jpeg)**
* **pdf**
* **documents (xls, xlsx, ods, ppt, pptx, odp, doc, docx, odt)**

You will be able to:

* **Preview images**.
* **Generate smart thumbnails**.

The main difference between thumbnail and preview
 functionality is that preview tends to be more faithful
while thumbnail tends to elaborate on it, cropping
 it by default and rounding the image if asked.
Preview should always output the file in its original format,
 while thumbnail will convert it to an image.
There is no difference in quality between the two,
 the difference in quality can be achieved only
by asking for a jpeg format and changing the quality parameter.
"""

# IMAGE
IMAGE_NAME: str = read_config(section=service_section_name, value="image_name")

# HEALTH
HEALTH_NAME: str = read_config(section=service_section_name, value="health_name")

# PDF
PDF_NAME: str = read_config(section=service_section_name, value="pdf_name")

# DOCUMENT

DOC_NAME: str = read_config(section=service_section_name, value="document_name")
