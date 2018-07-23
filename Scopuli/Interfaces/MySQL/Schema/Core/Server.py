#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright [2018] Tatarnikov Viktor [viktor@tatarnikov.org]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" """

from Scopuli.Interfaces.MySQL.SQLAlchemy import *

from Scopuli.Interfaces.MySQL.Schema import Base


class Server(Base, Schema):
    """
        Таблица серверов работающих под 4Gain Project
    """
    __tablename__ = 'server'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица серверов работающих под 4Gain Project'
    }
    
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    cd_parent = Column(Integer(), ForeignKey(id), nullable=True, doc="Родитель")
    
    vid = Column(Integer(), ColumnDefault(-1), index=True, nullable=False, doc="Идентификатор виртуального сервера")
    
    address_ipv4 = Column(IPAddressType(), ColumnDefault(""), nullable=False, doc="Адрес IPV4")
    address_ipv6 = Column(String(64), ColumnDefault(""), nullable=False, doc="Адрес IPV6")
    
    domain = Column(String(32), ColumnDefault(""), nullable=False, doc="Домен")
    domain_full = Column(String(128), ColumnDefault(""), nullable=False, doc="Домен")
    
    is_enable = Column(Boolean(), ColumnDefault(True), nullable=False, doc="Метка использования")
    is_ve = Column(Boolean(), ColumnDefault(True), nullable=False, doc="Метка виртуального окружения")

    # RelationShip's
    parent = relationship("Server", remote_side=[id])
