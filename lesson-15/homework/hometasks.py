
# #### **1. Basic Plotting**
# - **Task**: Plot the function $ f(x) = x^2 - 4x + 4 $ for $ x $ values between -10 and 10. 
# Customize the plot with appropriate labels for the axes and a title.
# ---

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 - 4*x + 4

# Generate x values
x = np.linspace(-10, 10, 500)  # 500 points between -10 and 10

# Compute y values
y = f(x)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$f(x) = x^2 - 4x + 4$", color="blue", linewidth=2)

# Customize the plot
plt.title("Plot of $f(x) = x^2 - 4x + 4$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Add x-axis
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Add y-axis
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()


# #### **2. Sine and Cosine Plot**
# - **Task**: Plot $ \sin(x) $ and $ \cos(x) $ on the same graph for $ x $ values ranging from 0 to $ 2\pi $. 
# Use different line styles, markers, and colors to distinguish between the two functions. Add a legend.

x = np.linspace(0, 2 * np.pi, 500)  # 500 points between 0 and 2π

# Compute y values for sine and cosine
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the functions
plt.figure(figsize=(8, 6))
plt.plot(x, y_sin, label=r"$\sin(x)$", color="red", linestyle="-", linewidth=2)
plt.plot(x, y_cos, label=r"$\cos(x)$", color="blue", linestyle="--", linewidth=2)

# Customize the plot
plt.title("Plot of $\\sin(x)$ and $\\cos(x)$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Add x-axis
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Add y-axis
plt.grid(alpha=0.3)
plt.legend(fontsize=12)

# Show the plot
plt.show()

# #### **3. Subplots**
# - **Task**: Create a 2x2 grid of subplots. In each subplot, plot:
#   - Top-left: $ f(x) = x^3 $
#   - Top-right: $ f(x) = \sin(x) $
#   - Bottom-left: $ f(x) = e^x $
#   - Bottom-right: $ f(x) = \log(x+1) $ (for $ x \geq 0 $)

#   Customize each plot with titles, axis labels, and different colors.

# ---

x = np.linspace(-10, 10, 500)  # For general functions
x_positive = np.linspace(0, 10, 500)  # For log(x+1), as x must be >= 0

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: f(x) = x^3
axs[0, 0].plot(x, x**3, color="blue", label=r"$f(x) = x^3$")
axs[0, 0].set_title(r"$f(x) = x^3$", fontsize=14)
axs[0, 0].set_xlabel("x", fontsize=12)
axs[0, 0].set_ylabel("f(x)", fontsize=12)
axs[0, 0].grid(alpha=0.3)
axs[0, 0].legend(fontsize=10)

# Top-right: f(x) = sin(x)
axs[0, 1].plot(x, np.sin(x), color="red", label=r"$f(x) = \sin(x)$")
axs[0, 1].set_title(r"$f(x) = \sin(x)$", fontsize=14)
axs[0, 1].set_xlabel("x", fontsize=12)
axs[0, 1].set_ylabel("f(x)", fontsize=12)
axs[0, 1].grid(alpha=0.3)
axs[0, 1].legend(fontsize=10)

# Bottom-left: f(x) = e^x
axs[1, 0].plot(x, np.exp(x), color="green", label=r"$f(x) = e^x$")
axs[1, 0].set_title(r"$f(x) = e^x$", fontsize=14)
axs[1, 0].set_xlabel("x", fontsize=12)
axs[1, 0].set_ylabel("f(x)", fontsize=12)
axs[1, 0].grid(alpha=0.3)
axs[1, 0].legend(fontsize=10)

# Bottom-right: f(x) = log(x+1)
axs[1, 1].plot(x_positive, np.log(x_positive + 1), color="purple", label=r"$f(x) = \log(x+1)$")
axs[1, 1].set_title(r"$f(x) = \log(x+1)$", fontsize=14)
axs[1, 1].set_xlabel("x", fontsize=12)
axs[1, 1].set_ylabel("f(x)", fontsize=12)
axs[1, 1].grid(alpha=0.3)
axs[1, 1].legend(fontsize=10)

# Adjust layout
plt.tight_layout()
plt.show()



# #### **4. Scatter Plot**
# - **Task**: Create a scatter plot of 100 random points in a 2D space. The x and y values should be randomly generated 
# from a uniform distribution between 0 and 10. Use different colors and markers for the points. Add a title, axis labels, and a grid.

x_scatter = np.random.uniform(0, 10, 100)
y_scatter = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)
markers = np.random.choice(['o', 's', 'D', '^', 'v', '<', '>'], 100)

plt.figure(figsize=(8, 6))
for i in range(100):
    plt.scatter(x_scatter[i], y_scatter[i], color=plt.cm.jet(colors[i]), marker=markers[i])

plt.title("Scatter Plot of 100 Random Points")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(alpha=0.2)
plt.show()

# #### **5. Histogram**
# - **Task**: Generate a random dataset of 1000 values sampled from a normal distribution (mean=0, std=1). 
# Plot a histogram of the data with 30 bins. Add a title and axis labels. Adjust the transparency of the bars using the `alpha` parameter.

data = np.random.randn(1000)

plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='red')
plt.title('Histogram', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show() 


# #### **6. 3D Plotting**
# - **Task**: Create a 3D surface plot for the function $ f(x, y) = \cos(x^2 + y^2) $ over the range of $ x $ and $ y $ values from -5 to 5. 
# Use a suitable colormap and add a colorbar. Set appropriate labels for the axes and title.

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_title("3D Surface Plot of $f(x, y) = \cos(x^2 + y^2)$")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("f(x, y)")
fig.colorbar(surf)
plt.show()

# #### **7. Bar Chart**
# - **Task**: Create a vertical bar chart displaying the sales data for five different products: `['Product A', 'Product B', 'Product C', 'Product D', 'Product E']`. 
# The sales values for each product are `[200, 150, 250, 175, 225]`. Customize the chart with a title, axis labels, and different bar colors.

categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]

plt.bar(categories, values, color='red', width=0.5)
plt.title('Product sales')
plt.xlabel('Product Name')
plt.ylabel('Cost')
plt.show()

# #### **8. Stacked Bar Chart**
# - **Task**: Create a stacked bar chart that shows the contribution of three different categories (`'Category A'`, `'Category B'`, and `'Category C'`) 
# over four time periods (`'T1'`, `'T2'`, `'T3'`, `'T4'`). Use sample data for each category at each time period. Customize the chart with a title, axis labels, and a legend.


time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [5, 7, 8, 6]
category_B = [3, 5, 6, 4]
category_C = [2, 4, 5, 3]

# Create a stacked bar chart
fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(time_periods, category_A, label='Category A', color='b')
ax.bar(time_periods, category_B, bottom=category_A, label='Category B', color='r')
ax.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='g')

# Customize the chart
ax.set_title("Stacked Bar Chart of Categories Over Time")
ax.set_xlabel("Time Periods")
ax.set_ylabel("Value")
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
