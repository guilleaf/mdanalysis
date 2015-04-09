================================
  MDAnalysis Repository README
================================

MDAnalysis_ is a Python toolkit to analyze molecular dynamics
trajectories generated by CHARMM, Amber, NAMD, LAMMPS, or Gromacs.

Source code is hosted in a git repository at

       https://github.com/MDAnalysis/mdanalysis

and is available under the GNU General Public License, version 2 (see
the file LICENSE_).

This is the top level of the master repository. It contains

1. the MDAnalysis toolkit source files in the directory ::

      package/

2. the unit tests together with any input files required for
   running those tests in the directory ::

      testsuite/

The directory ``maintainer`` contains scripts only needed for
maintaining releases and are not generally useful for the user or the
typical developer. The ``vm`` directory contains configurations for
virtual machines.

(For more details on the directory layout see `Issue 87`_ on the
MDAnalysis issue tracker.)

.. _Issue 87: https://github.com/MDAnalysis/mdanalysis/issues/87
.. _MDAnalysis: http://www.MDAnalysis.org
.. _LICENSE: https://github.com/MDAnalysis/mdanalysis/blob/master/LICENSE