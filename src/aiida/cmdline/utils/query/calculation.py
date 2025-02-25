###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida-core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""A utility module with a factory of standard QueryBuilder instances for Calculation nodes."""
from aiida.common.warnings import warn_deprecation

warn_deprecation('This module is deprecated, use `aiida.tools.query.calculation` instead.', version=3)
