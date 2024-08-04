import tkinter as tk
from tkinter import ttk, messagebox
import threading
import scapy.all as scapy
from scapy.layers.inet import IP, TCP

class NetworkSnifferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Sniffer")
        self.root.geometry("500x400")

        self.interface_label = ttk.Label(root, text="Select Interface:")
        self.interface_label.pack(pady=10)

        self.interface_combobox = ttk.Combobox(root, values=self.get_available_interfaces())
        self.interface_combobox.pack(pady=10)

        self.start_button = ttk.Button(root, text="Start Sniffing", command=self.start_sniffing)
        self.start_button.pack(pady=10)

        self.output_text = tk.Text(root, height=15, width=70)
        self.output_text.pack(pady=10)

    def get_available_interfaces(self):
        interfaces = scapy.get_if_list()
        print("Available Interfaces:", interfaces)
        return interfaces

    def start_sniffing(self):
        interface = self.interface_combobox.get()
        if not interface:
            messagebox.showwarning("Error", "Please select an interface.")
            return
        print(f"Selected Interface: {interface}")
        threading.Thread(target=self.sniff_packets, args=(interface,), daemon=True).start()

    def sniff_packets(self, interface):
        try:
            scapy.sniff(iface=interface, store=False, prn=self.process_packet, filter="ip")
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            self.root.after(0, self.update_output, error_message + "\n")

    def process_packet(self, packet):
        if packet.haslayer(IP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto

            port_info = ""
            if packet.haslayer(TCP):
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                port_info = f", Ports: {src_port} -> {dst_port}"

            packet_info = f"IP Packet: {src_ip} -> {dst_ip}, Protocol: {protocol}{port_info}\n"
            self.root.after(0, self.update_output, packet_info)

    def update_output(self, packet_info):
        self.output_text.insert(tk.END, packet_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSnifferApp(root)
    root.mainloop()
