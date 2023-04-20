import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# Change default path 
# sys.path.append('PROGMOD_')

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

    return (in_numbers, seperated, vars)
        

def plotxy (x, y, xlab, ylab, xunit, yunit):
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
    N2 = 3.14/2
    x_start = 0
    x_end = max(x)
    res = 100 # resolution
    y_N1 = np.full(res, N1)
    y_N2 = np.full(res, N2)
    plt.plot(x_target, y_N1, color="red", label="N1")
    plt.plot(x_target, y_N2, color="red", label="N2")

    # PLOT XY DATA
    plt.plot(x, y, "ro-", color="blue")
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    # SET UNITS
    plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter(f'%.1f {xunit}'))
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter(f'%.1f {yunit}'))

    plt.grid()
    plt.legend()
    plt.show()


# Main
def main():
    # Changing default matplotlib font: https://jonathansoma.com/lede/data-studio/matplotlib/changing-fonts-in-matplotlib/
    matplotlib.rcParams['font.serif'] = "Palatino Linotype" # Change default serif font
    matplotlib.rcParams['font.family'] = "serif" # Set default family to serif

    # Get data
    f = open("log_files/newlog", "r")
    lines : str = f.read()

    # GET XY DATA
    x_num, x_str, x_str_seperated = txt_to_variable_array(lines, 0, 0)
    y_num, y_str, y_str_seperated = txt_to_variable_array(lines, 0, 1)
    v_num, v_str, v_str_seperated = txt_to_variable_array(lines, 0, 2)

    # # Print for table
    # print(x_str_seperated)
    # print(y_str_seperated)
    # print(v_str_seperated)

    #Plt
    plotxy(x_num, y_num, "Time", "Angle", "s", "rad")
    
    



if __name__ == "__main__":
    main()