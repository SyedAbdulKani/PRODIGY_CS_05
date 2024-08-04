# PRODIGY_CS_05

Network Sniffer App

This is a simple network sniffer application built using Python, Tkinter for the GUI, and Scapy for packet capturing. The application allows you to select a network interface and start sniffing IP packets on that interface. It displays captured packet information, including source IP, destination IP, protocol, and ports (if applicable), in a text box within the GUI.

**Prerequisites**

- Python 3.10 or later
- Scapy library
- Tkinter library (usually comes pre-installed with Python)

**Installation**

1. **Install Python**: Make sure you have Python 3.10 or later installed on your system.
2. **Install Scapy**: You can install Scapy using pip:
   pip install scapy

**Usage**

1. **Run the Application**: Execute the Python script to launch the network sniffer application.
   python k1.py
2. **Select Interface**: Choose the network interface you want to sniff from the dropdown list.
3. **Start Sniffing**: Click the "Start Sniffing" button to begin capturing packets on the selected interface.
4. **View Captured Packets**: Captured packets will be displayed in the text box with details such as source IP, destination IP, protocol, and ports.

 **Notes**

- Ensure you run the script with administrative privileges, as network sniffing often requires elevated permissions.
- The application will print available network interfaces to the console for debugging purposes.

**Example Output**
Available Interfaces: ['eth0', 'wlan0']
Selected Interface: wlan0
IP Packet: 192.168.1.1 -> 192.168.1.2, Protocol: 6, Ports: 12345 -> 80
IP Packet: 192.168.1.3 -> 192.168.1.4, Protocol: 17
