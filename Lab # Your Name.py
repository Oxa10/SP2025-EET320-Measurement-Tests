# Othman Alrawi
# EET321
# 1
# Mini Lab 1

import subprocess
import sys

def install(package):
    """Attempts to install the required package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}. Please install it manually.")

# Install required package
install("pyvisa")

# Import Pyvisa for instrument communication
import pyvisa

# Initialize the resource manager
rm = pyvisa.ResourceManager()

try:
    # Find power supply address
    Powersupply = [a for a in rm.list_resources() if 'SPD' in a]
    if Powersupply:
        supply = rm.open_resource(Powersupply[0])
    else:
        print("PowerSupply not detected. Ensure it is connected and powered on.")
except IndexError:
    print("Error accessing PowerSupply. Check the connection and try again.")

try:
    # Find Digital Multimeter (DMM) address
    Digital = [b for b in rm.list_resources() if 'SDM' in b]
    dmm = rm.open_resource(Digital[0])
except IndexError:
    print("Digital MultiMeter not connected or powered on")

try:
    # Find Oscilloscope address
    OSilly = [c for c in rm.list_resources() if 'SDS' in c]
    oscope = rm.open_resource(OSilly[0])
except IndexError:
    print("Oscilloscope not connected or powered on")

try:
    # Find Function Generator address
    Fuci = [d for d in rm.list_resources() if 'SDG' in d]
    fungen = rm.open_resource(Fuci[0])
except IndexError:
    print("Function Generator not connected or powered on")

try:
    # Part1: Function Generator Waveform Output
    with open("Part1.txt", 'w') as file:
        # Turn off function generator output
        fungen.write("C1:OUTP OFF")
        response = fungen.query("C1:BSWV?")
        file.write(f"C1:OUTP OFF -> {response}\n")

        # Turn on function generator output and wait
        fungen.write("C1:OUTP ON")
        import time
        time.sleep(5)

        # Configure and test different waveforms
        for wave_type, freq, amp in [("SINE", 2000, 1), ("SQUARE", 500, 2), ("RAMP", 1500, 3)]:
            fungen.write(f"C1:BSWV WVTP,{wave_type}")
            fungen.write(f"C1:BSWV FRQ,{freq}")
            fungen.write(f"C1:BSWV AMP,{amp}")
            time.sleep(5)
            response = fungen.query("C1:BSWV?")
            file.write(f"{wave_type} Waveform: FRQ={freq}, AMP={amp} -> {response}\n")

    # Part2: Oscilloscope Measurements
    with open("Part2.txt", 'w') as file:
        # Configure function generator
        fungen.write("C1:BSWV WVTP,SINE")
        fungen.write("C1:BSWV FRQ,1000")
        fungen.write("C1:BSWV AMP,2")
        time.sleep(5)

        # Configure oscilloscope and measure amplitude and frequency
        for attn, vdiv, tdiv in [(10, "1V", "500US"), (1, "2V", "1MS")]:
            oscope.write(f"C1:ATTN {attn}")
            oscope.write(f"C1:VDIV {vdiv}")
            oscope.write(f"TDIV {tdiv}")
            time.sleep(2)
            amp_response = oscope.query("C1:PAVA? AMPL")
            freq_response = oscope.query("C1:PAVA? FREQ")
            time.sleep(2)
            file.write(f"{attn}x Attenuation, {vdiv}/div, {tdiv}/div:\n")
            file.write(f"Amplitude: {amp_response}\n")
            file.write(f"Frequency: {freq_response}\n\n")

finally:
    # Ensure all resources are properly closed
    if 'oscope' in locals():
        oscope.close()
    if 'fungen' in locals():
        fungen.close()
