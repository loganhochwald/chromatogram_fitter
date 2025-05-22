import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from ui import get_excel_file_and_sheet

# Start GUI
excel_info = get_excel_file_and_sheet()
if not excel_info:
    print("No file or sheet selected.")
    exit()

file_path, selected_sheet = excel_info

# Load the column lavels of the DataFrame with Pandas
df = pd.read_excel(file_path, sheet_name=selected_sheet)
df.columns = ['x', 'y']

x_data = df['x'].values
y_data = df['y'].values

# A normal Gaussian distribution curve function
def gaussian(x, amplitude, mean, stdDev):
    return amplitude * np.exp(-(x - mean)**2 / (2 * stdDev**2))

# Sums multiple Gaussians
# The * in *params allows as many sets of Gaussians as needed
# Each set of parameters is [amplitude, mean, stdDev]
def multi_gaussian(x, *params):
    n = int(len(params) / 3)
    result = np.zeros_like(x)
    for i in range(n):
        amp, mean, stdDev = params[i*3:i*3+3]
        result += gaussian(x, amp, mean, stdDev)
    return result

# Peak detection and fitting | Format: [amp1, cen1, wid1, amp2, cen2, wid2, amp3, cen3, wid3]
# Filters out noise by only considering peaks that are at least 10% as tall as the max value
# Ensures detected peaks are at least 10 data points apart (avoids finding multiple close peaks in a single broad peak)
# Can get more info about peaks if needed by removing the _
peaks, _ = find_peaks(y_data, height=np.max(y_data) * 0.1, distance=10)  # You can tweak height/distance

# Build detected peaks list of parameters for the Gaussian function
# If they're not fitting well, try adjusting the stdDev value
detected_peaks = []
for peak in peaks:
    amp = y_data[peak]
    mean = x_data[peak]
    stdDev = (x_data[-1] - x_data[0]) / 30  # Rough width guess
    detected_peaks += [amp, mean, stdDev]

# Fit the model to data
optParams, _ = curve_fit(multi_gaussian, x_data, y_data, p0=detected_peaks)

# Plot the data and the fit
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, label='Original Spectrum', color='black')
plt.plot(x_data, multi_gaussian(x_data, *optParams), label='Fitted Curve', linestyle='--', color='red')

# Plot each individual Gaussian
num_peaks = int(len(optParams) / 3)
for i in range(num_peaks):
    amp, mean, stdDev = optParams[i*3:i*3+3]
    plt.plot(x_data, gaussian(x_data, amp, mean, stdDev), label=f'Peak {i+1}')

plt.xlabel('Time (s)')
plt.ylabel('Intensity (nA)')
plt.title('Deconvolution of Chromatographic Peaks')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print Gaussian parameters if needed
# for i in range(num_peaks):
#     amp, mean, stdDev = optParams[i*3:i*3+3]
#     print(f"Peak {i+1}: Amplitude = {amp:.4f}, Center = {mean:.4f}, Width = {stdDev:.4f}")