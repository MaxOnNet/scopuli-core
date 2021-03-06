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


class Organization(Base, Schema):
    """
        Таблица ролей
    """
    __tablename__ = 'organization'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица организаций'
        }
    
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    
    code = Column(String(64), unique=True, index=True, nullable=False, doc="Кодовое обозначение роли")
    name = Column(String(256), nullable=False, doc="Наименование роли")
    
    is_ = Column(Boolean(), ColumnDefault(True), nullable=False, doc="Метка использования")


