"""
partition_func.py
A statistcal mechanics solver to evaluate the parition function given a collection of eigen states

Handles the primary functions
ei: 
    list of eigen values from schroginger equation
temp: 
    array of temperatures to evaluate partition function
unit:
    determines the units of boltzmann constant (must be same as eigen values)
        kJ/mol
        J
        eV
plot (optional):
    function that can be set to True to plot out the solutions to the SE
"""
# load modules
from scipy import constants
import numpy as np

# load internal modules
from .plot import *

def q_PESq(ei,temp,unit):

    if unit == 'Hartree':
        kb = constants.physical_constants['Boltzmann constant in eV/K'][0]/constants.physical_constants['Hartree energy in eV'][0]
    elif unit == 'eV':
        kb = constants.physical_constants['Boltzmann constant in eV/K'][0]
    elif unit == 'J':
        kb = constants.physical_constants['Boltzmann constant'][0]
    elif unit == 'kJ/mol':
        kb = constants.physical_constants['Boltzmann constant'][0]/1000*constants.N_A
    else:
        raise ValueError('Unit must be Hartree, eV, J, or kJ/mol')

    q_tot = []

    for i in temp:
        q_temp = 0
        for j in ei:
            q_temp = np.exp(-j/(kb*i)) + q_temp

        q_tot.append(q_temp)

    q_tot=np.array(q_tot)

    return q_tot

def q_HO(freq,temp,unit):

    c = constants.physical_constants['speed of light in vacuum'][0]*100

    if unit == 'Hartree':
        kb = constants.physical_constants['Boltzmann constant in eV/K'][0]/constants.physical_constants['Hartree energy in eV'][0]
        h = -1*constants.physical_constants['Planck constant'][0]/constants.physical_constants['hartree-joule relationship'][0]
    elif unit == 'eV':
        kb = constants.physical_constants['Boltzmann constant in eV/K'][0]
        h = -1*constants.physical_constants['Planck constant in eV s'][0]
    elif unit == 'J':
        kb = constants.physical_constants['Boltzmann constant'][0]  
        h = -1*constants.physical_constants['Planck constant'][0]
    elif unit == 'kJ/mol':
        kb = constants.physical_constants['Boltzmann constant'][0]/1000*constants.N_A
        h = -1*constants.physical_constants['Planck constant'][0]/1000*constants.N_A
    else:
        raise ValueError('Unit must be Hartree, eV, J, or kJ/mol')


    q_tot = []

    for i in temp:
        q_temp = 0

        beta = kb*i
        en_freq = h*freq*c

        q_temp = np.exp(en_freq/(2*beta)) / (1-np.exp(en_freq/beta))

        q_tot.append(q_temp)

    q_tot = np.array(q_tot)

    return q_tot