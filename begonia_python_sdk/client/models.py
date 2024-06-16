#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2024/06/16 12:12:18
@Desc    :
'''
from pydantic import BaseModel


class FileDetails(BaseModel):
    sha256: str
    content_type: str
    size: int
    version: str
    bucket: str
