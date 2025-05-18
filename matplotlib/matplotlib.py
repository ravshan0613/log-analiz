import matplotlib.pyplot as plt

timestamps = ['2025-05-19 12:00:00', '2025-05-19 12:30:00', '2025-05-19 13:00:00']
error_counts = [5, 2, 10]

plt.plot(timestamps, error_counts, label='Error Count')
plt.xlabel('Time')
plt.ylabel('Number of Errors')
plt.title('Error Count Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.show()
