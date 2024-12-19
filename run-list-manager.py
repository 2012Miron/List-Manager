import subprocess
import sys

def run_script(script_name, new_window=False):
    try:
        if new_window:
            subprocess.Popen(['python', script_name], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            result = subprocess.run(['python', script_name], check=True, capture_output=True, text=True)
            print(f"Script {script_name} run sucsesfull.")
            print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error with start script {script_name}.")
        print("Error:", e.stderr)
    except Exception as e:
        print(f"Error with start script {script_name}: {e}")

scripts_here = ['checker/checker.py', 'checker/ackter.py'] # The / symbol is needed to tell the script where the file is located
for script in scripts_here:
    run_script(script)

run_script('General.py', new_window=True)

print("Closing run-list-manager.py...")
sys.exit()