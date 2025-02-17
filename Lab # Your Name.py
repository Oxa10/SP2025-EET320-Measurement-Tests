# YOUR NAME
# EET321
# SECTION NUMBER
# ASSIGNMENT NAME
# DATE
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("pyvisa")

# Import Pyvisa.
import pyvisa

rm = pyvisa.ResourceManager()

#Find power supply address
try:
    Powersupply = [a for a in rm.list_resources() if 'SPD' in a]
    supply = rm.open_resource(Powersupply[0])
except IndexError:
    print("PowerSupply not connected or powered on")

#Find DMM address
try:
    Digital = [b for b in rm.list_resources() if 'SDM' in b]
    dmm = rm.open_resource(Digital[0])
except IndexError:
    print("Digital MultiMeter not connected or powered on")

#Find Osilly address
try:
    OSilly = [c for c in rm.list_resources() if 'SDS' in c]
    oscope = rm.open_resource(OSilly[0])
except IndexError:
    print("Oscilloscope not connected or powered on")

#Find Function  address
try:
    Fuci = [d for d in rm.list_resources() if 'SDG' in d]
    fungen = rm.open_resource(Fuci[0])
except IndexError:
    print("Function Generator not connected or powered on")



# Part1
# Open the file to save the results
file = open("Part1.txt",'w')
# Begin the Measurements
fungen.write("C1:OUTP OFF")
response = fungen.query("C1:BSWV?")
file.write(f"C1:OUTP OFF -> {response}\n")

fungen.write("C1:OUTP ON")
# Adding 5 seconds time delay
import time
time.sleep(5)

# set waveform as SINE, query, and save the details
fungen.write("C1:BSWV WVTP,SINE")
fungen.write("C1:BSWV FRQ,2000")
fungen.write("C1:BSWV AMP,1")
# Adding 5 seconds time delay
time.sleep(5)
response = fungen.query("C1:BSWV?")
file.write(f"Sine Waveform: FRQ=2000, AMP=1 -> {response}\n")

# set waveform as SQUARE, query, and save the details
fungen.write("C1:BSWV WVTP,SQUARE")
fungen.write("C1:BSWV FRQ,500")
fungen.write("C1:BSWV AMP,2")
# Adding 5 seconds time delay
time.sleep(5)
response = fungen.query("C1:BSWV?")
file.write(f"Square Waveform: FRQ=500, AMP=2 -> {response}\n")

# set waveform as RAMP, query, and save the details
fungen.write("C1:BSWV WVTP,RAMP")
fungen.write("C1:BSWV FRQ,1500")
fungen.write("C1:BSWV AMP,3")
# Adding 5 seconds time delay
time.sleep(5)
response = fungen.query("C1:BSWV?")
file.write(f"Ramp Waveform: FRQ=1500, AMP=3 -> {response}\n")

# Close the file after finishing all commands
file.close()

#Part2
file = open("Part2.txt",'w')

fungen.write("C1:BSWV WVTP,SINE")
fungen.write("C1:BSWV FRQ,1000")
fungen.write("C1:BSWV AMP,2")

# Initial delay before starting
time.sleep(5)

# First Configuration
# Set attenuation to 10x
oscope.write("C1:ATTN 10")
oscope.write("C1:VDIV 1V")
# Set timebase scale to 500 s/div
oscope.write("TDIV 500US")
time.sleep(2)

# Measure Amplitude and Frequency
amp_response = oscope.query("C1:PAVA? AMPL")
freq_response = oscope.query("C1:PAVA? FREQ")
time.sleep(2)
file.write(f"10x Attenuation, 1V/div, 500s/div:\n")
file.write(f"Amplitude: {amp_response}\n")
file.write(f"Frequency: {freq_response}\n\n")

# Second Configuration
oscope.write("C1:ATTN 1")
oscope.write("C1:VDIV 2V")
oscope.write("TDIV 1MS")

# Measure Amplitude and Frequency again
amp_response = oscope.query("C1:PAVA? AMPL")
freq_response = oscope.query("C1:PAVA? FREQ")
time.sleep(2)
file.write(f"1x Attenuation, 2V/div, 1ms/div:\n")
file.write(f"Amplitude: {amp_response}\n")
file.write(f"Frequency: {freq_response}\n")

# Close the File
file.close()

# Part3
import csv
with open("Part3.csv", mode='w', newline='') as file:
    writer = csv.writer(file)

    # CSV Headers
    writer.writerow([
        "Waveform Type",
        "Set Frequency (Hz)",
        "Set Amplitude (V)",
        "Measured Frequency (Hz)",
        "Measured Amplitude (V)"
    ])

    # Define the waveforms list with their settings (like in Part 1)
    waveforms = [
        {"type": "SINE", "frequency": 2000, "amplitude": 1},  # Sine wave at 2000 Hz, 1 V
        {"type": "SQUARE", "frequency": 500, "amplitude": 2},  # Square wave at 500 Hz, 2 V
        {"type": "RAMP", "frequency": 1500, "amplitude": 3}  # Ramp wave at 1500 Hz, 3 V
    ]

    # Loop through each waveform
    for wave in waveforms:
        # Configure the function generator
        fungen.write(f"C1:BSWV WVTP,{wave['type']}")  # Set waveform type (SINE, SQUARE, RAMP)
        fungen.write(f"C1:BSWV FRQ,{wave['frequency']}")  # Set frequency
        fungen.write(f"C1:BSWV AMP,{wave['amplitude']}")  # Set amplitude
        time.sleep(3)  # Allow time for waveform to stabilize

        # Measure the frequency and amplitude using the oscilloscope
        measured_freq = oscope.query("C1:PAVA? FREQ").strip()
        measured_amp = oscope.query("C1:PAVA? AMPL").strip()

        # Write the results to the CSV file
        writer.writerow([
            wave['type'],
            wave['frequency'],
            wave['amplitude'],
            measured_freq,
            measured_amp
        ])
#Part4
install("numpy")
import numpy as np
with open("Part4.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "Time (s)",
        "Sweep Frequency (Hz)",
        "Measured Frequency (Hz)"
    ])

    # Sweep Parameters
    start_freq = 100  # 100 Hz
    end_freq = 100000  # 100 kHz
    sweep_time = 10  # Total time for sweep (10 seconds)

    # Calculate how many data points to collect (e.g., 100 points)
    num_points = 100
    time_intervals = np.linspace(0, sweep_time, num_points)  # Time intervals for the sweep
    frequencies = np.linspace(start_freq, end_freq, num_points)  # Frequencies corresponding to time intervals

    for i, current_time in enumerate(time_intervals):
        current_freq = frequencies[i]

        # Set the frequency for the function generator
        fungen.write(f"C1:BSWV WVTP,SINE")  # Set waveform type to SINE
        fungen.write(f"C1:BSWV FRQ,{current_freq}")  # Set frequency
        fungen.write(f"C1:BSWV AMP,1")  # Set amplitude to 1
        time.sleep(0.05)  # Small delay to stabilize

        # Measure the frequency using the oscilloscope
        measured_freq = oscope.query("C1:PAVA? FREQ").strip()  # Get the measured frequency
        measured_freq = measured_freq.replace("C1:PAVA FREQ,", "").replace("Hz", "").strip()

        # Record the data (Time, Set Frequency, Measured Frequency)
        writer.writerow([current_time, current_freq, measured_freq])


#Close the resources
oscope.close()
fungen.close()