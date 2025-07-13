import time
import requests
import subprocess

INFLUX_URL = "http://localhost:8086/api/v2/write?org=YOUR_ORG&bucket=YOUR_BUCKET&precision=s"
INFLUX_TOKEN = "YOUR_INFLUXDB_TOKEN"
HOSTS = ["h1", "h2", "h3"]  # Mininet host names
INTERFACE = "eth0"
INTERVAL = 2  # seconds

def get_rx_tx_bytes(host, iface):
    cmd = f"mnexec -a $(pgrep -f 'mininet: {host}') cat /sys/class/net/{iface}/statistics/{{rx_bytes,tx_bytes}}"
    try:
        output = subprocess.check_output(cmd, shell=True).decode().split()
        rx, tx = int(output[0]), int(output[1])
        return rx, tx
    except Exception as e:
        print(f"Error reading stats for {host}: {e}")
        return None, None

def main():
    last = {}
    while True:
        for host in HOSTS:
            rx, tx = get_rx_tx_bytes(host, INTERFACE)
            if rx is None or tx is None:
                continue
            if host in last:
                rx_rate = (rx - last[host][0]) / INTERVAL
                tx_rate = (tx - last[host][1]) / INTERVAL
                # Prepare InfluxDB line protocol
                line = f'bandwidth,host={host} rx_rate={rx_rate},tx_rate={tx_rate}'
                headers = {"Authorization": f"Token {INFLUX_TOKEN}"}
                try:
                    requests.post(INFLUX_URL, data=line, headers=headers, timeout=2)
                except Exception as e:
                    print(f"Error sending to InfluxDB: {e}")
                print(line)
            last[host] = (rx, tx)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()