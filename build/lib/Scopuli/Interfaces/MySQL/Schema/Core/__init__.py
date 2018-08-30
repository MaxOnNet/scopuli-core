#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright [2017] Tatarnikov Viktor [viktor@tatarnikov.org]
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


class Image(Base, Schema):
    """
        Базовая таблица храниения изображений
    """
    __tablename__ = 'image'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком и информацией об используемых изображениях'
    }
    
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    uuid = Column(String(64), index=True, nullable=False, doc="UUID файла в кэше")
    
    file = Column(String(256), nullable=False, doc="Относительный путь до изображения")
    md5sum = Column(String(64), index=True, nullable=False, doc="Контрольная сумма изображения")
    
    file_thumbnail = Column(String(256), nullable=False, doc="Относительный путь до изображения")
    md5sum_thumbnail = Column(String(64), index=True, nullable=False, doc="Контрольная сумма изображения")
    
    size = Column(Integer(), ColumnDefault(0), nullable=False, doc="Размер изображения")
    height = Column(Integer(), ColumnDefault(0), nullable=False, doc="Высота изображения")
    width = Column(Integer(), ColumnDefault(0), nullable=False, doc="Ширина изображения")
    
    # Automatic Logger
    date_create = Column(DateTime(), nullable=False, default=func.utc_timestamp(), doc="AutoLogger - Время создания")
    date_change = Column(DateTime(), nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp(), doc="AutoLogger - Время последнего изменения")


class File(Base, Schema):
    """
        Базовая таблица хранения файлов
    """
    __tablename__ = 'file'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком и информацией об используемых файлов'
    }
    
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    uuid = Column(String(64), index=True, nullable=False, doc="UUID файла в кэше")
    
    file = Column(String(256), nullable=False, doc="Относительный путь до файла")
    type = Column(String(16), nullable=False, doc="Тип файла")
    md5sum = Column(String(64), index=True, nullable=False, doc="Сонтрольная сумма изображения")
    
    file_thumbnail = Column(String(256), nullable=False, doc="Относительный путь до изображения")
    md5sum_thumbnail = Column(String(64), index=True, nullable=False, doc="Сонтрольная сумма изображения")
    
    size = Column(Integer(), ColumnDefault(0), nullable=False, doc="Размер файла")
    
    # Automatic Logger
    date_create = Column(DateTime(), nullable=False, default=func.utc_timestamp(), doc="AutoLogger - Время создания")
    date_change = Column(DateTime(), nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp(), doc="AutoLogger - Время последнего изменения")


class Address(Base, Schema):
    """
        Базовая таблица хранения адресов
    """
    __tablename__ = 'address'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком и информацией об используемых файлов'
    }
    
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    
    country = Column(String(64), nullable=False, doc="Страна")
    city = Column(String(64), nullable=False, doc="Город")
    street = Column(String(64), nullable=False, doc="Улица")
    house = Column(String(8), nullable=False, doc="Дом")
    room = Column(String(8), nullable=False, doc="Кабинет \ квартира")
    floor = Column(String(256), nullable=False, doc="Этаж")
    index = Column(String(64), nullable=False, doc="Почтовый индекс")
    type = Column(String(16), nullable=False, doc="Тип файла")

    latitude = Column(String(16), nullable=False, doc="Широта")
    longitude = Column(String(16), nullable=False, doc="Долгота")
    
    # Automatic Logger
    date_create = Column(DateTime(), nullable=False, default=func.utc_timestamp(), doc="AutoLogger - Время создания")
    date_change = Column(DateTime(), nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp(),
                         doc="AutoLogger - Время последнего изменения")

    # Rela
    phones = association_proxy('address_phones', 'phone')
    urls = association_proxy('address_urls', 'url')
    emails = association_proxy('address_emails', 'email')


class Phone(Base, Schema):
    """
        Базовая таблица хранения телефонов
    """
    __tablename__ = 'phone'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком телефонов'
    }

    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    
    country = Column(String(16), ColumnDefault(""), nullable=False, doc="Код страны")
    city = Column(String(16), ColumnDefault(""), nullable=True, doc="Код города")
    number = Column(String(16), ColumnDefault(""), nullable=False, doc="Номер телефона")

    title = Column(String(128), ColumnDefault(""), nullable=False, doc="Название")
    description = Column(String(256), ColumnDefault(""), nullable=False, doc="Краткое описание")

    is_enable = Column(Boolean(), ColumnDefault(False), default=False, nullable=False, doc="Метка использования")
    is_published = Column(Boolean(), ColumnDefault(False), default=False, nullable=False, doc="Метка использования в интернете")

    # Automatic Logger
    date_create = Column(DateTime(), nullable=False, default=func.utc_timestamp(), doc="AutoLogger - Время создания")
    date_change = Column(DateTime(), nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp(),
                         doc="AutoLogger - Время последнего изменения")

    @hybrid_property
    def phone(self):
        if self.city is None:
            return "+{}{}".format(self.country, self.number)
        else:
            return "+{}{}{}".format(self.country, self.city, self.number)


class AddressPhone(Base, Schema):
    """
        Базовая таблица хранения телефонов
    """
    __tablename__ = 'address_phone'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком телефонов у адреса'
    }
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    cd_address = Column(Integer(), ForeignKey(Address.id), nullable=False, doc="Ссылка на Address")
    cd_phone = Column(Integer(), ForeignKey(Phone.id), nullable=False, doc="Ссылка на Phone")
    
    phone = relationship(Phone)
    address = relationship(Address, backref=backref("address_phones", cascade="all, delete-orphan"))


class Email(Base, Schema):
    """
        Базовая таблица хранения телефонов
    """
    __tablename__ = 'email'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком почтовых адресов'
    }
    
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    
    email = Column(String(128), ColumnDefault(""), nullable=False, doc="Адрес")
    
    title = Column(String(128), ColumnDefault(""), nullable=False, doc="Название")
    description = Column(String(256), ColumnDefault(""), nullable=False, doc="Краткое описание")
    
    is_enable = Column(Boolean(), ColumnDefault(False), default=False, nullable=False, doc="Метка использования")
    is_published = Column(Boolean(), ColumnDefault(False), default=False, nullable=False, doc="Метка использования в интернете")
    
    # Automatic Logger
    date_create = Column(DateTime(), nullable=False, default=func.utc_timestamp(), doc="AutoLogger - Время создания")
    date_change = Column(DateTime(), nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp(),
                         doc="AutoLogger - Время последнего изменения")


class AddressEmail(Base, Schema):
    """
        Базовая таблица хранения почтовых адресов
    """
    __tablename__ = 'address_email'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком электронных почтовых адресов у адреса'
    }
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    cd_address = Column(Integer(), ForeignKey(Address.id), nullable=False, doc="Ссылка на Address")
    cd_email = Column(Integer(), ForeignKey(Email.id), nullable=False, doc="Ссылка на Email")
    
    email = relationship(Email)
    address = relationship(Address, backref=backref("address_emails", cascade="all, delete-orphan"))


class Url(Base, Schema):
    """
        Базовая таблица хранения телефонов
    """
    __tablename__ = 'url'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком почтовых адресов'
    }
    
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    
    url = Column(String(256), ColumnDefault(""), nullable=False, doc="Адрес")
    
    title = Column(String(128), ColumnDefault(""), nullable=False, doc="Название")
    description = Column(String(256), ColumnDefault(""), nullable=False, doc="Краткое описание")
    
    is_enable = Column(Boolean(), ColumnDefault(False), default=False, nullable=False, doc="Метка использования")
    is_published = Column(Boolean(), ColumnDefault(False), default=False, nullable=False, doc="Метка использования в интернете")
    
    # Automatic Logger
    date_create = Column(DateTime(), nullable=False, default=func.utc_timestamp(), doc="AutoLogger - Время создания")
    date_change = Column(DateTime(), nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp(),
                         doc="AutoLogger - Время последнего изменения")


class AddressUrl(Base, Schema):
    """
        Базовая таблица хранения почтовых адресов
    """
    __tablename__ = 'address_url'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_general_ci',
        'mysql_comment': 'Таблица со списком электронных адресов у адреса'
    }
    id = Column(Integer(), primary_key=True, autoincrement=True, doc="Row ID - Сурогатный ключ")
    cd_address = Column(Integer(), ForeignKey(Address.id), nullable=False, doc="Ссылка на Address")
    cd_url = Column(Integer(), ForeignKey(Url.id), nullable=False, doc="Ссылка на Email")
    
    url = relationship(Url)
    address = relationship(Address, backref=backref("address_urls", cascade="all, delete-orphan"))
