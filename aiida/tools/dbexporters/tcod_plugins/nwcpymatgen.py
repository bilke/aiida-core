# -*- coding: utf-8 -*-

__copyright__ = u"Copyright (c), 2015, ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE (Theory and Simulation of Materials (THEOS) and National Centre for Computational Design and Discovery of Novel Materials (NCCR MARVEL)), Switzerland and ROBERT BOSCH LLC, USA. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file"
__version__ = "0.5.0"
__contributors__ = "Andrius Merkys, Giovanni Pizzi, Martin Uhrin"

from aiida.tools.dbexporters.tcod_plugins import BaseTcodtranslator

class NwcpymatgenTcodtranslator(BaseTcodtranslator):
    """
    NWChem's input and output parameter translator to TCOD CIF dictionary
    tags.
    """
    _plugin_type_string = "nwchem.nwcpymatgen.NwcpymatgenCalculation"

    @classmethod
    def get_software_package(cls,calc,**kwargs):
        """
        Returns the package or program name that was used to produce
        the structure. Only package or program name should be used,
        e.g. 'VASP', 'psi3', 'Abinit', etc.
        """
        return 'NWChem'

    @classmethod
    def get_software_package_version(cls,calc,**kwargs):
        """
        Returns software package version used to compute and produce
        the computed structure file. Only version designator should be
        used, e.g. '3.4.0', '2.1rc3'.
        """
        try:
            return calc.out.job_info.get_dict()['nwchem branch']
        except Exception:
            return None

    @classmethod
    def get_software_package_compilation_timestamp(cls,calc,**kwargs):
        """
        Returns the timestamp of package/program compilation in ISO 8601
        format.
        """
        from dateutil.parser import parse
        try:
            date = calc.out.job_info.get_dict()['compiled']
            return parse(date.replace('_', ' ')).isoformat()
        except Exception:
            return None

    @classmethod
    def get_atom_type_symbol(cls,calc,**kwargs):
        """
        Returns a list of atom types. Each atom site MUST occur only
        once in this list. List MUST be sorted.
        """
        parameters = calc.out.output
        dictionary = parameters.get_dict()
        if 'basis_set' not in dictionary.keys():
            return None
        return sorted(dictionary['basis_set'].keys())

    @classmethod
    def get_atom_type_basisset(cls,calc,**kwargs):
        """
        Returns a list of basisset names for each atom type. The list
        order MUST be the same as of get_atom_type_symbol().
        """
        parameters = calc.out.output
        dictionary = parameters.get_dict()
        if 'basis_set' not in dictionary.keys():
            return None
        return [dictionary['basis_set'][x]['description']
                for x in cls.get_atom_type_symbol(calc,**kwargs)]

    @classmethod
    def get_atom_type_valence_configuration(cls,calc,**kwargs):
        """
        Returns valence configuration of each atom type. The list order
        MUST be the same as of get_atom_type_symbol().
        """
        parameters = calc.out.output
        dictionary = parameters.get_dict()
        if 'basis_set' not in dictionary.keys():
            return None
        return [dictionary['basis_set'][x]['types']
                for x in cls.get_atom_type_symbol(calc,**kwargs)]
