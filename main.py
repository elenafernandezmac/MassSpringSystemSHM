import numpy as np
import matplotlib.pyplot as plt

"""we ask the user for the mass value, the spring constant and the mass value, the initial displacement (the distance between 0 and the mass in time=0) 
and the time in which the user will be analysing the objects position"""

mass_value = float(input("Type your mass value in kg: "))
spring_constant_value = float(input("Type your spring constant in N/m: "))
initial_displacement_value = float(input("Type the initial displacement in m: "))
total_time_value = float(input("Type the time, in seconds, in which you wanna study the object's motion: "))

"""we create a class with all the values needed in the following equations as objects
Fspring=-kx (N/m)
Epe= 0.5kx**2
Ec= epe= 0.5mv**2"""

class SimpleHarmonicMotion:
    def __init__(self, mass, spring_constant, initial_displacement, initial_velocity=0, time_step=0.01, total_time=10):
        #we define each object in the class
        self.mass = mass
        self.spring_constant = spring_constant
        self.initial_displacement = initial_displacement
        self.initial_velocity = initial_velocity
        self.time_step = time_step
        self.total_time = total_time

        #we create an array of time vaules for the simulation to use
        self.time = np.arange(0, total_time, time_step)

        self.displacement = None
        self.velocity = None
        self.acceleration = None

        #we calculate the motion of the system
        self.calculate_motion()

    def calculate_motion(self):
        """in order to calculate displacement, velocity, and acceleration we use the following simple harmonic movement equations
        ω=(k/m)**0.5
        x(t)=Acos(ωt)
        v(t)=−Aωsin(ωt)
        aangular(t)= −Aω^2 cos(ωt) """
        omega = np.sqrt(self.spring_constant / self.mass)
        self.displacement = self.initial_displacement * np.cos(omega * self.time)
        self.velocity = -self.initial_displacement * omega * np.sin(omega * self.time)
        self.acceleration = -self.initial_displacement * omega**2 * np.cos(omega * self.time)

    def plot_motion(self):
        #we plot the displacement, velocity, and acceleration over the given time span
        plt.figure(figsize=(10, 6))

        plt.subplot(3, 1, 1)
        plt.plot(self.time, self.displacement, label='Displacement (m)')
        plt.title('Simple Harmonic Motion')
        plt.xlabel('Time (s)')
        plt.ylabel('Displacement (m)')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(self.time, self.velocity, label='Velocity (m/s)', color='pink')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(self.time, self.acceleration, label='Acceleration (m/s^2)', color='purple')
        plt.xlabel('Time (s)')
        plt.ylabel('Acceleration (m/s^2)')
        plt.legend()

        plt.tight_layout()
        plt.show()

    def calculate_spring_force(self):
        #we calculate the spring force at each time step
        spring_force = -self.spring_constant * self.displacement
        return spring_force

    def calculate_elastic_potential_energy(self):
        #we calculate the elastic potential energy at each time step
        elastic_potential_energy = 0.5 * self.spring_constant * self.displacement**2
        return elastic_potential_energy

    def calculate_kinetic_energy(self):
        #we calculate the kinetic energy at each time step
        kinetic_energy = 0.5 * self.mass * self.velocity**2
        return kinetic_energy



shm_system = SimpleHarmonicMotion(mass_value, spring_constant_value, initial_displacement_value, total_time=total_time_value)
shm_system.plot_motion()

spring_force = shm_system.calculate_spring_force()
elastic_potential_energy = shm_system.calculate_elastic_potential_energy()
kinetic_energy = shm_system.calculate_kinetic_energy()

#we print the values 
print("Spring Force:", spring_force)
print("Elastic Potential Energy:", elastic_potential_energy)
print("Kinetic Energy:", kinetic_energy)