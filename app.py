import requests # type: ignore
import streamlit as st # type: ignore
from streamlit_lottie import st_lottie  # type: ignore

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# ---LOAD ASSESTS---
lottie_coding = load_lottieurl("https://lottie.host/31f335a2-7371-4864-b28a-0fc7d07e44db/JETIPYGNyJ.json")

# ---HEADER SECTION---
st.subheader("Fluid Mechanics Webpage") 
st.title("Fundamentals Of Pressure Head") 
st.write("Step by step calculation of Pressure Head")
# ---INTRODUCTION TO FLUID MECHANICS---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is Fluid Mechanics?")
        st.write("##")
        st.write(
            """
                - Fluids do not have a shape, so they only interact with solid objects, i.e. containers they are kept in. 
                  These fluids are either stationary or moving in these containers (buckets, pipes, reservoirs, etc.). 
                  The fluids exert certain forces on the containers, either static or dynamic.
                - Fluid mechanics is a branch of physics that deals with the behaviour of fluids under external forces such as gravity, pressure, or shear stress.
                   The goal of fluid mechanics is to understand and predict the behaviour of fluids to design efficient systems and structures.
                   """)
        st.write("[LEARN MORE >](https://www.britannica.com/science/fluid-mechanics#:~:text=fluid%20mechanics%2C%20science%20concerned%20with,engineering%2C%20meteorology%2C%20and%20zoology.)")
    with right_column:
        st_lottie(lottie_coding , height = 300,key = "coding")

# ---INTRODUCTIION TO PRESSURE HEAD---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is Pressure Head?")
        st.write("##")
        st.write(
            """
                - Pressure head refers to the internal energy of a fluid due to the pressure exerted on it. 
                - It is measured in terms of the vertical height of a column of that fluid which can be supported by the hydrostatic pressure of the fluid.
                - It is crucial to remember that pressure head gets influenced by the depth and density of the fluid and the gravitational force.
                """)
        st.write("[LEARN MORE >](https://en.wikipedia.org/wiki/Pressure_head#:~:text=In%20fluid%20mechanics%2C%20pressure%20head,but%20not%20static%20head%20pressure).)")
    with right_column:
        left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image="https://www.civilconcept.com/wp-content/uploads/2020/01/Pressure-head-formula.gif", width=350)
        
# --- APPLICATIONS OF PRESSURE HEAD ---
        
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Application(s) of Pressure Head In Fluid Mechanics")
        st.write("##")
        st.write(
            """
                STATIC
                   - A mercury barometer is one of the classic uses of static pressure head.
                   - Such barometers are an enclosed column of mercury standing vertically with gradations on the tube. 
                   
                DIFFERENTIAL
                   - The venturmeter and manometer is a common type of flow meter which can be used in many fluid applications 
                     to convert differential pressure heads into volumetric flow rate, linear fluid speed, or mass flow rate using Bernoulli's principle.
                     """)
        st.write("[LEARNMORE >](https://en.wikipedia.org/wiki/Pressure_head#:~:text=In%20fluid%20mechanics%2C%20pressure%20head,but%20not%20static%20head%20pressure).)")
    with right_column:
        left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image="https://i.pinimg.com/474x/2b/77/eb/2b77ebad5603bf06d510d4636111aa52.jpg", width = 350)
with cent_co:
    st.write("   "*10,"VENTURIMETER", width=250)  
with cent_co: 
    st.image(image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz8Tl8auHnJ0kGUtssoujctC4OfXu3_YFuug&s", width=350)
with cent_co:
    st.write("  " *10 ,"MERCURY BAROMETER", width=250)


#---STEP BY STEP CALCULATION OF PRESSURE HEAD---
st.write(
    """
    Step 1: Identify the Required Formula
    
    The formula for pressure head 'h' is derived from the relationship between pressure, density, and gravity:

                                        h=P/ρg

Where:

h = pressure head (in meters or feet)

P = pressure (in Pascals or Newtons per square meter)

ρ = density of the fluid (in kg/m³ for SI units)

g = gravitational acceleration (in m/s²) 


SI units:

Pressure P is measured in Pascals (Pa)

Density ρ is in kg/m³ (for water, this is approximately 1000 kg/m³)

Gravitational acceleration 𝑔 is approximately 9.81 m/s²    

Step 2: Convert Units (if necessary)
 
Common conversions include:

1 atm = 101325 Pa

1 bar = 100000 Pa

1 ps i= 6894.76 Pa

Step 3: Put the Values into the Formula

Step 4: Solve for h (Pressure Head)

Example Calculation

Pressure 𝑃 = 50000 Pa

Fluid density 𝜌 = 1000 kg/m**3 (for water)

Gravitational acceleration 𝑔 = 9.81 m/s**2


Substitute these values into the formula:

                                         h = P /ρg
                                          h = 50000/1000*9.81
                                          h = 5.10 metres

The calculated pressure head is approximately 5.10 meters. This means that a pressure of 50,000 Pascals corresponds to a fluid column height of 5.10 meters of water.
"""
)


# --PRESSURE HEAD CALCULATOR---
import streamlit as st  # type: ignore 
st.title("Pressure head Calculator")
num1 = st.number_input("Enter value of Pressure:") 
num2 = st.number_input("Enter density of fluid:")
operation=("num1/num2*9.81") 
result = 0
if st.button("Calculate"): 
    result = num1 / num2*9.81
st.write(f"Result: = {result}")


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Constants
g = 9.81  # Acceleration due to gravity in m/s²
rho = 1000  # Density of water in kg/m³

# Streamlit App
st.title('Real-time Pressure Head Graph')

# User input for pressure in Pascals
pressure = st.slider('Select Pressure (P) in Pascals:', min_value=0.0, max_value=90000.0, step=100.0)

# Placeholder for Matplotlib animation
plot_placeholder = st.empty()

# Initialize arrays for pressure and pressure head values
time_steps = np.linspace(0, 10, 100)  # 100 time steps
pressure_data = np.zeros_like(time_steps)
pressure_head_data = np.zeros_like(time_steps)

# Function to update the plot in real-time
def update_plot(pressure, time_step):
    global pressure_data, pressure_head_data
    
    # Simulate a dynamic pressure change
    pressure_data[time_step] = pressure
    pressure_head_data[time_step] = pressure / (rho * g)
    
    # Plotting
    fig, ax = plt.subplots()
    ax.plot(time_steps[:time_step+1], pressure_head_data[:time_step+1], color='blue', label='Pressure Head (m)')
    ax.set_xlim([0, 10])
    ax.set_ylim([0, max(pressure_head_data) + 1])
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Pressure Head (m)')
    ax.legend()
    ax.set_title('Pressure Head over Time')
    plot_placeholder.pyplot(fig)

# Animation loop
for t in range(len(time_steps)):
    update_plot(pressure, t)
    time.sleep(0.9)  # Slow down the animation for visibility

    