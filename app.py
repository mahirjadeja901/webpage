import requests
import streamlit as st
from streamlit_lottie import st_lottie  #type ignore



st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# ---LOAD ASSESTS---
lottie_coding = load_lottieurl("https://lottie.host/31f335a2-7371-4864-b28a-0fc7d07e44db/JETIPYGNyJ.json")

# ---HEADER SECTION---
st.subheader("Basics Knowledge.com") 
st.title("A Fluid Mechanics Website") 
st.write("Current Page : Pressure Head")
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
        st.header("what is Pressure Head?")
        st.write("##")
        st.write(
            """
                - Pressure head refers to the internal energy of a fluid due to the pressure exerted on it. 
                - It is measured in terms of the vertical height of a column of that fluid which can be supported by the hydrostatic pressure of the fluid.
                - It is crucial to remember that pressure head gets influenced by the depth and density of the fluid and the gravitational force.
                """)
        st.write("[LEARN MORE >](https://en.wikipedia.org/wiki/Pressure_head#:~:text=In%20fluid%20mechanics%2C%20pressure%20head,but%20not%20static%20head%20pressure).)")
    with right_column:
        st.image(image="https://www.civilconcept.com/wp-content/uploads/2020/01/Pressure-head-formula.gif")

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
                   - The venturi meter and manometer is a common type of flow meter which can be used in many fluid applications 
                     to convert differential pressure heads into volumetric flow rate, linear fluid speed, or mass flow rate using Bernoulli's principle.
                     """)
    with right_column:
        st.image(image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz8Tl8auHnJ0kGUtssoujctC4OfXu3_YFuug&s")

        st.image(image="https://i.pinimg.com/474x/2b/77/eb/2b77ebad5603bf06d510d4636111aa52.jpg")
        st.write("[LEARNMORE >](https://en.wikipedia.org/wiki/Pressure_head#:~:text=In%20fluid%20mechanics%2C%20pressure%20head,but%20not%20static%20head%20pressure).)")


# --PRESSURE HEAD CALCULATOR---
import streamlit as st
st.title("Pressure head Calculator")
num1 = st.number_input("Enter value of Pressure:") 
num2 = st.number_input("Enter density of fluid:")
operation=("num1/num2*9.81") 
result = num1 / (num2*9.81) 
if st.button("Calculate"): 
    result = num1 / num2*9.81
st.write(f"Result: = {result}")



    
