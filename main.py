import numpy as np
import matplotlib.pyplot as plt


def plot_trajectory(height, initial_speed, angle):
    g = 9.81

    # c -> rad
    angle_rad = np.radians(angle)

    # Calculating flight times
    time_of_flight = (initial_speed * np.sin(angle_rad) + np.sqrt(
        (initial_speed * np.sin(angle_rad)) ** 2 + 2 * g * height)) / g

    # Calculating time intervals
    t = np.linspace(0, time_of_flight, num=500)

    # Calculating coordinates
    x = initial_speed * np.cos(angle_rad) * t
    y = height + initial_speed * np.sin(angle_rad) * t - 0.5 * g * t ** 2

    plt.figure(figsize=(5, 6))

    # Trajectory graph
    plt.subplot(3, 1, 1)
    plt.plot(x, y)
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.title('Trajectory')

    # Speed vs time graph
    speed = np.sqrt((initial_speed * np.cos(angle_rad)) ** 2 + (initial_speed * np.sin(angle_rad) - g * t) ** 2)
    plt.subplot(3, 1, 2)
    plt.plot(t, speed)
    plt.xlabel('Time (s)')
    plt.ylabel('Speed (m/s)')
    plt.title('Time dependence of velocity')

    # Graph of coordinates versus time
    plt.subplot(3, 1, 3)
    plt.plot(t, x, label='X (m)')
    plt.plot(t, y, label='Y (m)')
    plt.xlabel('Time(s)')
    plt.ylabel('Coordinates(m)')
    plt.title('Coordinates from time')
    plt.legend()

    plt.tight_layout()
    plt.show()


height = float(input("Enter the height from which the body was thrown (m): "))
initial_speed = float(input("Enter the initial velocity (m/s): "))
angle = float(input("Enter the angle at which the body was thrown (degrees): "))

plot_trajectory(height, initial_speed, angle)
