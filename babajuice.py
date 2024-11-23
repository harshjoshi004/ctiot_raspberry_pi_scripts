import subprocess
import time

def start_ble_advertising():
    try:
        # Disable any existing advertising
        subprocess.run(['sudo', 'hciconfig', 'hci0', 'down'], check=True)
        # Bring up the Bluetooth adapter
        subprocess.run(['sudo', 'hciconfig', 'hci0', 'up'], check=True)
        # Set scan response and advertising data
        subprocess.run([
            'sudo', 'hcitool', '-i', 'hci0', 'cmd',
            '0x08', '0x0006', # HCI_LE_Set_Advertising_Parameters
            '30', '00', # Min interval (30ms)
            '30', '00', # Max interval (30ms)
            '00', # Advertising type (Connectable undirected)
            '00', # Own address type (public)
            '00', # Peer address type
            '00', '00', '00', '00', '00', '00', # Peer address
            '07', # Advertising channel map
            '00' # Advertising filter policy
        ], check=True)
        # Set advertising data (changed name to "baba")
        subprocess.run([
            'sudo', 'hcitool', '-i', 'hci0', 'cmd',
            '0x08', '0x0008', # HCI_LE_Set_Advertising_Data
            '11', # Total Length (17 bytes: flags + UUID + name)
            '02', '01', '06', # Flags
            '03', '03', 'AA', 'FE', # UUID (Eddystone UUID as before)
            '09', # Length of local name
            '09', # Complete Local Name type
            '62', '61', '62', '61', '00', '00', '00', '00', '00', '00' # "baba" in hex
        ], check=True)
        # Enable advertising
        subprocess.run([
            'sudo', 'hcitool', '-i', 'hci0', 'cmd',
            '0x08', '0x000A', # HCI_LE_Set_Advertise_Enable
            '01' # Enable advertising
        ], check=True)
        print("BLE Advertising started. Open NRF Connect to scan.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAdvertising stopped.")
        subprocess.run(['sudo', 'hciconfig', 'hci0', 'down'], check=False)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        subprocess.run(['sudo', 'hciconfig', 'hci0', 'up'], check=False)

if __name__ == '__main__':
    start_ble_advertising()