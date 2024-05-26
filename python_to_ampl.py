import subprocess
import time
for i in range(9):
    time.sleep(10)
    process1 = subprocess.Popen(["python", "gen_data_csv1.py"]) # Create and launch process pop.py using python interpreter
    process2 = subprocess.Popen(["python", "gen_data_csv2.py"]) # Create and launch process pop.py using python interpreter
    process3 = subprocess.Popen(["python", "gen_data_csv3.py"]) # Create and launch process pop.py using python interpreter
    process4 = subprocess.Popen(["python", "gen_data_csv4.py"]) # Create and launch process pop.py using python interpreter
    process5 = subprocess.Popen(["python", "gen_data_csv5.py"]) # Create and launch process pop.py using python interpreter
    process6 = subprocess.Popen(["python", "gen_data_csv6.py"]) # Create and launch process pop.py using python interpreterprocess4 = subprocess.Popen(["python", "gen_data_csv4.py"]) # Create and launch process pop.py using python interpreter


    process1.wait() # Wait for process1 to finish (basically wait for script to finish)
    process2.wait() # Wait for process1 to finish (basically wait for script to finish)
    process3.wait() # Wait for process1 to finish (basically wait for script to finish)
    process4.wait() # Wait for process1 to finish (basically wait for script to finish)
    process5.wait() # Wait for process1 to finish (basically wait for script to finish)
    process6.wait() # Wait for process1 to finish (basically wait for script to finish)
