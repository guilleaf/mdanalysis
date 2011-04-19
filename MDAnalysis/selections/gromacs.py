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
Gromacs selections
==================

Write :class:`MDAnalysis.core.AtomGroup.AtomGroup` selection to a `ndx`_ file
that defines a Gromacs_ index group. To be used in Gromacs like this::

  <GROMACS_COMMAND> -n macro.ndx

The index groups are named *mdanalysis001*, *mdanalysis002*, etc.

.. _Gromacs: http://www.gromacs.org
.. _ndx: http://www.gromacs.org/Documentation/File_Formats/Index_File

.. autoclass:: SelectionWriter
   :inherited-members:
"""
import base

class SelectionWriter(base.SelectionWriter):
    format = "Gromacs"
    ext = "ndx"
    default_numterms = 12

    def _translate(self, atoms, **kwargs):
        # Gromacs index is 1-based; MDAnalysis is 0-based
        return [str(atom.number + 1) for atom in atoms]

    def _write_head(self, out, **kwargs):
        out.write("[ %(name)s ]\n" % kwargs)


