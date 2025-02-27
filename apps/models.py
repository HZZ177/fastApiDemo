#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/29 上午11:53
# @Author  : Heshouyi
# @File    : models.py
# @Software: PyCharm
# @description:
import tortoise
from tortoise import models, fields, run_async
from core.file_path import db_path


class DeviceMessageModel(models.Model):
    """设备接收下发消息表"""
    id = fields.IntField(pk=True, auto_increment=True, description="主键id")
    device_addr = fields.CharField(max_length=20, null=True, description="设备IP地址")
    message_source = fields.IntField(description="信息来源 0=未知 1=车位相机 2=通道相机 3=LED网络屏 4=LCD一体屏 5=Lora节点 6=四字节节点")
    message = fields.CharField(max_length=1000, null=True, description="接收的服务器下发指令")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table = "device_message"
        table_description = "设备接收下发消息表"


class UpperReportRecordModel(models.Model):
    """接收单车场/统一平台上行记录表"""
    id = fields.IntField(pk=True, auto_increment=True, description="主键id")
    source = fields.IntField(description="信息来源 1：单车场上报 2：统一平台上报 3：未知")
    message_type = fields.CharField(max_length=20, null=True, description="上报类型")
    message = fields.CharField(max_length=1000, description="上报内容")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table = "upper_report_record"
        table_description = "接收单车场/统一平台上行记录表"


if __name__ == "__main__":
    async def init():
        await tortoise.Tortoise.init(
            db_url=f"sqlite:///{db_path}",
            modules={"models": ["apps.models"]},
        )
        await tortoise.Tortoise.generate_schemas()

    run_async(init())
