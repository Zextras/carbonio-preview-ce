#!/bin/bash

# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com
# 
# SPDX-License-Identifier: AGPL-3.0-only

PYTHONPATH="${PYTHONPATH}:/opt/zextras/docs/core/program/:/opt/zextras/common/lib/python3.8/site-packages/" \
  /opt/zextras/common/bin/gunicorn app.controller:app \
  --config /opt/zextras/common/lib/python3.8/site-packages/app/gunicorn.conf.py
