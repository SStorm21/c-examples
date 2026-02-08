
import ping3

def ping(host):
    try:
        # Send ICMP echo request and return the round-trip time (in seconds)
        return ping3.ping(host)
    except ping3.errors.Timeout:
        return None  # Timeout occurred
    except PermissionError:
        return "Permission denied. Please run the script as administrator/root."

# Example usage
host = "example.com"
result = ping(host)
if result is not None:
    print(f"Ping to {host} successful. Round-trip time: {result} seconds.")
else:
    print(f"Ping to {host} failed.")