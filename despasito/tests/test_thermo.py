"""
Unit and regression test for the despasito package.
"""

# Import package, test suite, and other packages as needed
import despasito.thermodynamics.calc as calc
import despasito.thermodynamics as thermo
import despasito.equations_of_state
import pytest
import sys
import numpy as np

Tlist = [323.2]
xilist = [[0.96176473, 0.03823527]]
yilist = [[0.9954, 0.0046]]
Plist = [4492927.45]
rho_co2_h2o = np.array([19986.78358869])
P = np.array([4099056.163132072])

beads_co2_h2o = ['CO2', 'H2O']
nui_co2_h2o = np.array([[1., 0.],[0., 1.]])
beadlibrary_co2_h2o = {'CO2': {'epsilon': 207.89, 'l_a': 5.055, 'l_r': 26.408, 'sigma': 3.05e-10, 'Sk': 0.8468, 'Vks': 2, 'mass': 0.04401, 'NkH': 1, 'Nka1': 1},'H2O': {'epsilon': 266.68, 'l_a': 6.0, 'l_r': 17.02, 'sigma': 3.0063e-10, 'Sk': 1.0, 'Vks': 1, 'mass': 0.018015, 'NkH': 2, 'Nke1': 2, 'epsilonHe1': 1985.4, 'KHe1': 1.0169e-28}}
crosslibrary_co2_h2o = {'CO2': {'H2O': {'epsilon': 226.38, 'epsilonHe1': 2200.0, 'KHe1': 9.1419e-29}}}
sitenames_co2_h2o = ['H', 'e1', 'a1'] 
epsilonHB_co2_h2o = np.array([[[[   0.,     0.,     0. ], \
                       [   0.,     0.,     0. ], \
                       [   0.,     0.,     0. ]], \
                      [[   0.,  2200.,     0. ], \
                       [   0.,     0.,     0. ], \
                       [   0.,     0.,     0. ]]], \
                     [[[   0.,     0.,     0. ], \
                       [2200.,     0.,     0. ], \
                       [   0.,     0.,     0. ]], \
                      [[   0.,  1985.4,    0. ], \
                       [1985.4,    0.,     0. ], \
                       [   0.,     0.,     0. ]]]])
eos_co2_h2o = despasito.equations_of_state.eos("saft.gamma_mie",xi=np.array(xilist[0]),beads=beads_co2_h2o,nui=nui_co2_h2o,beadlibrary=beadlibrary_co2_h2o,crosslibrary=crosslibrary_co2_h2o,sitenames=sitenames_co2_h2o)

def test_thermo_import():
#    """Sample test, will always pass so long as import statement worked"""
    assert "despasito.thermodynamics" in sys.modules

def test_phase_xiT(eos=eos_co2_h2o,Tlist=Tlist,xilist=xilist):

    output = thermo.thermo(eos,{"calculation_type":"phase_xiT","Tlist":Tlist,"xilist":xilist})
        
    assert output["P"][0]==pytest.approx(4493471.284403669,abs=1e+1) and output["yi"][0]==pytest.approx([0.99539961, 0.00460039],abs=1e-4)

def test_phase_yiT(eos=eos_co2_h2o,Tlist=Tlist,yilist=yilist):

    output = thermo.thermo(eos,{"calculation_type":"phase_yiT","Tlist":Tlist,"yilist":yilist})

    assert output["P"][0]==pytest.approx(4493570.232231314,abs=1e+1) and output["xi"][0]==pytest.approx([0.9617648, 0.0382352],abs=1e-4)

def test_sat_props(eos=eos_co2_h2o,Tlist=Tlist):

    output = thermo.thermo(eos,{"calculation_type":"sat_props","Tlist":Tlist,"xilist":[np.array([1.0, 0.0])]})

    assert output["Psat"][0]==pytest.approx(4738900.71313235,abs=1e+1) and output["rhol"][0]==pytest.approx(17905.96767603,abs=1e-1), output["rhol"][0]==pytest.approx(2371.38970066,abs=1e-1)

def test_liquid_properties(eos=eos_co2_h2o,Tlist=Tlist,xilist=xilist,Plist=Plist):

    output = thermo.thermo(eos,{"calculation_type":"liquid_properties","Tlist":Tlist,"Plist":Plist,"xilist":xilist})

    assert output["rhol"][0]==pytest.approx(17526.54149309,abs=1e-1) and output["phil"][0]==pytest.approx(np.array([84.79316501,  0.21474978]),abs=1e-1)

def test_vapor_properties(eos=eos_co2_h2o,Tlist=Tlist,yilist=yilist,Plist=Plist):

    output = thermo.thermo(eos,{"calculation_type":"vapor_properties","Tlist":Tlist,"Plist":Plist,"yilist":yilist})

    assert output["rhov"][0]==pytest.approx(37.85936814,abs=1e-1) and output["phiv"][0]==pytest.approx(np.array([2.45619145, 0.37836254]),abs=1e-1)
    
