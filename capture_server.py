import socket
import struct

from src.creating_data_object import create_data_object

def parse_forza_data(data):
    """
    Parses the binary data received from Forza Horizon 5 telemetry.

    Args:
        data (bytes): The raw binary data from the UDP packet.

    Returns:
        dict: Parsed telemetry data with meaningful keys and values.
    """
    try:
        # Example parsing structure: adjust based on actual Forza telemetry structure
        telemetry_format = "<i4f"  # Example: 1 int followed by 4 floats
        unpacked_data = struct.unpack(telemetry_format, data[:struct.calcsize(telemetry_format)])

        # Map unpacked data to meaningful keys (example)
        parsed_data = {
            "car_id": unpacked_data[0],
            "speed": unpacked_data[1],
            "engine_rpm": unpacked_data[2],
            "acceleration_x": unpacked_data[3],
            "acceleration_y": unpacked_data[4],
        }
        parsed_data = create_data_object(unpacked_data)
        return parsed_data
    except struct.error as e:
        print(f"Error parsing data: {e}")
        return None

def capture_udp_data(host="127.0.0.1", port=5000):
    """
    Captures UDP packets sent to the specified host and port.

    Args:
        host (str): The IP address to bind the server to. Defaults to localhost.
        port (int): The port to listen on for UDP packets. Defaults to 5000.

    """
    # Create a socket object
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified host and port
    udp_socket.bind((host, port))
    
    print(f"Listening for UDP packets on {host}:{port}...")

    try:
        while True:
            # Receive data from the socket (max buffer size 1024 bytes)
            data, addr = udp_socket.recvfrom(1024)
            print(f"Received raw data from {addr}: {data}")

            # Parse the received data
            parsed_data = parse_forza_data(data)
            if parsed_data:
                print(f"Parsed telemetry data: {parsed_data}")
    except KeyboardInterrupt:
        print("Server stopped.")
    finally:
        udp_socket.close()

if __name__ == "__main__":
    # Replace with the port configured in Forza Horizon 5 telemetry settings
    capture_udp_data(port=5000)
