# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################

from aiida.orm.implementation.calculation import Calculation, JobCalculation
from .inline import *
from .work import WorkCalculation
from .function import FunctionCalculation

__all__ = ['Calculation', 'JobCalculation', 'WorkCalculation', 'FunctionCalculation'] + inline.__all__
