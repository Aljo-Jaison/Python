import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 50]  # Line 1
y2 = [5, 15, 30, 35, 40]   # Line 2
y3 = [2, 10, 20, 25, 35]   # Line 3

# Plot multiple lines
plt.plot(x, y1, marker="o", linestyle="-", color="blue", label="Product A")
plt.plot(x, y2, marker="s", linestyle="--", color="green", label="Product B")
plt.plot(x, y3, marker="^", linestyle=":", color="red", label="Product C")

plt.title(" Sales Performance Over Time")
plt.xlabel("Months")
plt.ylabel("Sales (in units)")

plt.legend()

plt.grid(True)

plt.show()
