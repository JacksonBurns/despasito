
SAFT
=======================

The Statistical Associating Fluid Theory (SAFT) equation of state (EOS) is based on first order perturbation of the residual Helmholtz energy. The total Helmholtz energy is then defined as the sum of ideal gas, monomer (i.e. segment or group), chain (i.e. component), and association terms.

:math:`\frac{A}{N k_{B} T}=\frac{A^{ideal}}{N k_{B} T}+\frac{A^{mono.}}{N k_{B} T}+\frac{A^{chain}}{N k_{B} T}+\frac{A^{assoc.}}{N k_{B} T}`

The ideal and association terms are defined in the main saft object. The monomer and chain terms (or others such as :math:`A^{elec.}` for electrolytes) are defined in a more specific object that the main ``saft`` class will import. This secondary class will provide the radial distribution function used by the association term with the method, ``gr_assoc``.

.. autosummary::
   :toctree: _autosummary

   despasito.equations_of_state.saft.saft.EosType
   despasito.equations_of_state.saft.saft.saft_type

SAFT-𝛾-Mie
-----------------------

EOS type: ``saft.gamma_mie``

This heteronuclear version of SAFT uses the Mie potential to not only offer a group contribution EOS but a means to connect thermodynamic properties to bead definitions that can be simulated.
    
Papaioannou, V. et. al, J. Chem. Phys. 140, 054107 (2014); https://doi.org/10.1063/1.4851455

.. autosummary::
   :toctree: _autosummary

   despasito.equations_of_state.saft.gamma_mie.SaftType

Supporting Functions
####################

.. autosummary::
   :toctree: _autosummary

   despasito.equations_of_state.saft.compiled_modules.ext_gamma_mie_python

SAFT-𝛾-SW
-----------------------

EOS type: ``saft.gamma_sw``

This heteronuclear version of SAFT uses the square-wave potential to not only offer a group contribution EOS but a means to connect thermodynamic properties to bead definitions that can be simulated.

Lymperiadis, A. et. al, J. Chem. Phys. 127, 234903 (2007); https://doi.org/10.1063/1.2813894

.. autosummary::
   :toctree: _autosummary

   despasito.equations_of_state.saft.gamma_sw.SaftType

General Functions
-----------------------
.. autosummary::
   :toctree: _autosummary

    despasito.equations_of_state.saft.saft_toolbox
    despasito.equations_of_state.saft.Aideal
    despasito.equations_of_state.saft.Aassoc
