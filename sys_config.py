import subprocess
import json
import psutil

def run_neofetch_ext():
    # Run neofetch command and capture the output
    output = subprocess.check_output(['neofetch', '--json'], universal_newlines=True)
    
    # Convert the output to a JSON object
    try:
        json_output = json.loads(output)
    except json.JSONDecodeError:
        return None
    
    # Extract specific keys from the JSON object
    desired_keys = ["OS", "Host", "Kernel", "Shell", "CPU", "GPU"]
    desired_output = {key: json_output.get(key, "") for key in desired_keys}
    
    desired_output["MEM (Used/Total)"] = get_memory_usage()
    desired_output["SSD (Used/Total)"] = get_ssd_storage()

    json_desired_output = json.dumps(desired_output)

    return json_desired_output


def get_ssd_storage():
    # Get the disk usage information for '/'
    usage = psutil.disk_usage('/')
    
    # Calculate the remaining and total SSD storage in GB
    remaining_storage_gb = round((usage.total - usage.free) / (1024**3), 2)
    total_storage_gb = round(usage.total / (1024**3), 2)
    
    # Format the storage values as a string
    # storage_string = f"{remaining_storage_gb} GB / {total_storage_gb} GB - {round(remaining_storage_gb/total_storage_gb*100, 2)}%"
    storage_string = f"{total_storage_gb}GB / {round(remaining_storage_gb/total_storage_gb*100, 2)}% used"
    
    return storage_string

def get_memory_usage():
    memory = psutil.virtual_memory()
    
    remaining_memory_gb = round((memory.total - memory.available) / (1024**3), 2)
    total_memory_gb = round(memory.total / (1024**3), 2)

    # memory_string = f"{remaining_memory_gb} GB / {total_memory_gb} GB / {round(remaining_memory_gb/total_memory_gb*100, 2)}%"
    memory_string = f"{total_memory_gb}GB / {round(remaining_memory_gb/total_memory_gb*100, 2)}% used"

    return memory_string

# result = run_neofetch_ext()
# print(result)
# print(type(result))



