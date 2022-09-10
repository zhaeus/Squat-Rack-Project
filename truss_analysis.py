# -*- coding: utf-8 -*-
"""
For graphing the deformation and strain for individual truss elements for squat rack project
"""


import numpy as np

# Global parameters
E = 200e9 #Pa, Young's modulus of steel (generic)
I = 4.7e-7 #m4, second moment of area
sigma_y = 80e6 #Pa
y_half = 0.065/2 #half the thickness of SHS member, m
mass = 200 #kg
impact_height = 0.7 #m
a_gravity = 9.81 #m/s2
impact_sf = 1.5
impact_velocity = np.sqrt(2*a_gravity*impact_height)
impact_energy = 0.5*impact_sf*mass*impact_velocity**2

# Geometry parameters 
L = 577.5e-3 #m, spotter bar length
a = 200e-3 #m, brace length        
m_adv = L/a #mechanical advantage due to brace position

# Functions describing 'spring constant' along length
def Kc(x):
     return (x**2)*(3*L-x)/(6*E*I) #continuous cubic throughout 
def Kb(x):
    before_a = (x**2)*(3*a-x)/(6*E*I) #cubic
    after_a = (a**2)*(3*x-a)/(6*E*I) #linear 
    return np.where(x<a,before_a,after_a) 
def Kboth(x):
    return Kc(x)-m_adv*Kb(x)

# Max deflection
K_end = Kboth(L)
delta_max = np.sqrt(2*K_end*impact_energy) #maximum deflection
Fc_max = -delta_max/K_end #maximum force at bar end (bottom)
Fb_max = m_adv*-Fc_max #maximum force at brace end (bottom)
omega_n = np.sqrt(1/(mass*K_end)) #undamped natural frequency with weight

# Vectors in space and time
num_x = 100
dx = L/(num_x-1)
bar_vec = np.linspace(0,L,num_x)
time_vec = np.linspace(0,(1/omega_n),20)

# Function for defining deflection 
def max_deflection(x):
    return Fc_max*Kboth(x)
def deflection(x,t):
    return max_deflection(x)*np.sin(2*np.pi*omega_n*t)

# Graphing 
import matplotlib.pyplot as plt 
try:
    import IPython
    shell = IPython.get_ipython()
    shell.enable_matplotlib(gui='inline') #to plot in different window change 'inline' to 'qt5'
except:
    print('Unable to open plotting window')  
fig, ax = plt.subplots() # Matplotlibism for initialising
ax.set_xlabel('x')
ax.set_ylabel('y')

# Slow motion graphic of beam vibration
def beam_vib_plot():
    for tt in time_vec:
        plt.ylim(-L/2, L/2)
        y_vec = deflection(bar_vec,tt)
        displacement = plt.plot(bar_vec, y_vec, color='blue', linestyle='dashed')[0]
        brace = plt.plot((0,0,a),(0,-a,0),color='black', linestyle='solid')[0]
        plt.title(f'Deflection at {tt:.3f} seconds')
        # ax.set_title()
        plt.show() # Matplotlibism for displaying plot 
    pass

# Attempt at calculating first and second derivatives for the very last point (the end)
# Second derivative = 0   
# This is because after the brace, the bending is linear-dominated
# Need to calculate first and second derivative at every point 

# First and second derivatives for calculation of strain 
def last_point():
    last_four = Fc_max*Kboth(bar_vec)[-4:] #left to right
    first_derivative_vec = (1/(2*dx))*np.array((0,1,-4,3))
    first_derivative = last_four @ first_derivative_vec.T
    second_derivative_vec = (1/dx**3)*np.array((-1,4,-5,2)) #left to right
    second_derivative = last_four @ second_derivative_vec.T
    print(f"The first derivative is {first_derivative} and the second derivative is {second_derivative}")
    pass 


# # Strain calculation
# one_on_rho = second_derivative/((1+first_derivative**2)**1.5)
# strain_max = -y_half*one_on_rho 

# Matrices for first and second div
first_mat = np.zeros((num_x,num_x))
second_mat = np.zeros((num_x,num_x))
dx1 = 1/dx
dx2 = 1/dx**2
for i in range(num_x):
    if i == 0 or i == num_x-1:
        continue 
    else:
        first_mat[i,i-1] = -dx1
        first_mat[i,i+1] = dx1
        second_mat[i,i-1] = dx2
        second_mat[i,i] = -2*dx2
        second_mat[i,i+1] = dx2

first_div_vec = first_mat @ max_deflection(bar_vec)
second_div_vec = second_mat @ max_deflection(bar_vec)

def inverse_rho(first_derivative_vector,second_derivative_vector):
    return second_derivative_vector/((1+first_derivative_vector**2)**1.5)

inverse_rho_bar = inverse_rho(first_div_vec,second_div_vec)

def real_deriv_plot():
    first_derivative_plot = plt.plot(bar_vec, first_div_vec, color='green', linestyle='dashed')[0]
    second_derivative_plot = plt.plot(bar_vec, second_div_vec, color='red', linestyle='dashed')[0]
    rho_plot = plt.plot(bar_vec, inverse_rho_bar, color='blue', linestyle='dashed')[0]
    plt.show() # Matplotlibism for displaying plot 
    pass
max_strain = max(abs(inverse_rho_bar))*y_half
max_strain_rate = max_strain*2*np.pi*omega_n

def sigma_impact(strain,strain_rate):
    strain_term = 50.103 + 176.09*strain**0.518
    strain_rate_term = 1+0.095*np.log(strain_rate)
    return strain_term*strain_rate_term

conservative_sigma_impact = sigma_impact(max_strain,max_strain_rate)
def conservative_sigma():
    print(f'The equivalent stress due to impact loadcase is {conservative_sigma_impact:.2f} MPa')
    pass     

    







