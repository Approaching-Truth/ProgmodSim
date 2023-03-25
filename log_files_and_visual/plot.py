import sys
import numpy as np
import matplotlib.pylab as plt
import matplotlib.ticker as ticker

# Change default path 
# sys.path.append('PROGMOD_')

# Get data
f = open("log_files/sce5_log", "r")
lines : str = f.read()

# Function for formatting file to array of specific variables
# data = txt file
# sh_index = state history index, i.e. controller or environment
# var_index = variable index, i.e. timestamp, joint_angle etc...
def txt_to_variable_array (data, sh_index, var_index):
    sh = data.split("|")[sh_index]
    vars = sh.split("/")[var_index]
    seperated = vars.split("&")
    
    # Remove blank spaces
    index_to_remove = []
    for i, e in enumerate(seperated):
        if (e == ""):
            index_to_remove.append(i)
    for e in reversed(index_to_remove):
        seperated.pop(e)

    # Convert from strings to float
    in_numbers = [float(numerical_string) for numerical_string in seperated]
    return in_numbers

# GET XY DATA
x = txt_to_variable_array(lines, 0, 0)
y = txt_to_variable_array(lines, 0, 1)

# PLOT REFFERNCE LINE
ref = 3.14/8
x_start = 0
x_end = max(x)
res = 100 # resolution
x_target = np.linspace(x_start, x_end, res)
y_target = np.full(100, ref)
plt.plot(x_target, y_target, color="black", label="Target")

# Safe ranges
N1 = 0
N2 = 3.1415/4
x_start = 0
x_end = max(x)
res = 100 # resolution
y_N1 = np.full(res, N1)
y_N2 = np.full(res, N2)
plt.plot(x_target, y_N1, color="red", label="N1")
plt.plot(x_target, y_N2, color="red", label="N2")



# PLOT XY DATA
plt.plot(x, y, "ro-", color="blue")
plt.xlabel("x")
plt.ylabel("y")

# SET UNITS
# plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f s'))
# plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f rad'))

plt.grid()
plt.legend()
plt.show()