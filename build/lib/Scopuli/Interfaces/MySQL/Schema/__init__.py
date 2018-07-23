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

__import__('pkg_resources').declare_namespace(__name__)


from Scopuli.Interfaces.MySQL.SQLAlchemy import *

log = logging.getLogger(__name__)
Base = declarative_base()

from Scopuli.Interfaces.MySQL.Schema.Core import Image, Address, File
from Scopuli.Interfaces.MySQL.Schema.Core.Server import *
from Scopuli.Interfaces.MySQL.Schema.Core.User import User, UserGroup
from Scopuli.Interfaces.MySQL.Schema.Core.Login import *

# from Scopuli.Interfaces.MySQL.Schema.Service import *
# from Scopuli.Interfaces.MySQL.Schema.Service.Mail import *

# from Scopuli.Interfaces.MySQL.Schema.Product import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Attribute import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Brand import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Classificator import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Entrace import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Group import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Manufacturer import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Price import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Shop import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Unit import *
# from Scopuli.Interfaces.MySQL.Schema.Product.Warehouse import *


#from Interfaces.MySQL.Schema.GUI.Cashdesk import *

# from Interfaces.MySQL.Schema.Club import *
# from Interfaces.MySQL.Schema.Club.Room import *
# from Interfaces.MySQL.Schema.Club.Coacher import *
# from Interfaces.MySQL.Schema.Club.Service import *
# from Interfaces.MySQL.Schema.Club.Offer import *
# from Interfaces.MySQL.Schema.Club.Subscribe import *

# from Interfaces.MySQL.Schema.Web import *
# from Interfaces.MySQL.Schema.Web.Module import *
# from Interfaces.MySQL.Schema.Web.Widget import *

# from Interfaces.MySQL.Schema.ELink import *

if __name__ == "__main__":
    log.info("Самотестирование схемы базы данных")