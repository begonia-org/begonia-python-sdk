#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2024/06/16 12:12:18
@Desc    :
'''
from pydantic import BaseModel, Field


class ReadFileRequest(BaseModel):
    bucket: str = Field(..., description="The bucket name")
    # engine: str = Field(..., description="The storage engine")
    key: str = Field(..., description="The file key, must be a relative path, e.g., test/a.txt")
    version: str = Field(default="", description="The file version")


class FileDetails(BaseModel):
    sha256: str
    content_type: str
    size: int
    version: str
    bucket: str
