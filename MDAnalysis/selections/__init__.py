# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# MDAnalysis --- http://mdanalysis.googlecode.com
# Copyright (c) 2006-2011 Naveen Michaud-Agrawal,
#               Elizabeth J. Denning, Oliver Beckstein,
#               and contributors (see website for details)
# Released under the GNU Public Licence, v2 or any higher version
#
# Please cite your use of MDAnalysis in published work:
#
#     N. Michaud-Agrawal, E. J. Denning, T. B. Woolf, and
#     O. Beckstein. MDAnalysis: A Toolkit for the Analysis of
#     Molecular Dynamics Simulations. J. Comput. Chem. (2011),
#     in press.
#

"""
Selection exporters
===================

Functions to write a :class:`MDAnalysis.AtomGroup.AtomGroup` selection
to a file so that it can be used in another programme.

:mod:`MDAnalysis.selections.vmd`
    VMD_ selections
:mod:`MDAnalysis.selections.pymol`
    PyMol_ selections
:mod:`MDAnalysis.selections.gromacs`
    Gromacs_ selections
:mod:`MDAnalysis.selections.charmm`
    CHARMM_ selections

The :class:`MDAnalysis.selections.base.SelectionWriter` base class and
helper functions are in :mod:`MDAnalysis.selections.base`.
"""

import vmd, pymol, gromacs, charmm
from base import get_writer

# Signature:
#   W = SelectionWriter(filename, **kwargs)
#   W.write(AtomGroup)
_selection_writers = {'vmd': vmd.SelectionWriter,
                      'charmm': charmm.SelectionWriter, 'str': charmm.SelectionWriter,
                      'pymol': pymol.SelectionWriter, 'pml': pymol.SelectionWriter,
                      'gromacs': gromacs.SelectionWriter, 'ndx': gromacs.SelectionWriter,
                      }
