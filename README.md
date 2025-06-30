# fireBalancer

**fireBalancer** es un proyecto SDN que implementa un cortafuegos y balanceador de carga usando:

- ONOS como controlador SDN
- Containernet para la emulación de red
- Grafana para visualización en tiempo real


## Directorios

- `onos-app/`: Aplicación Java que controla flujos (firewall y load balancer)
- `containernet-topos/`: Topologías y scripts en Python
- `metrics-exporter/`: Extracción de métricas desde ONOS
- `grafana-dashboards/`: Dashboards para visualización

## Componentes

| Software             | Función                                                               |
| -------------------- | --------------------------------------------------------------------- |
| **Containernet**     | Emulación de red con Mininet + Docker                                 |
| **ONOS**             | Controlador SDN que gestiona los switches y flujos vía OpenFlow       |
| **Python (control)** | Scripts que hablan con ONOS por REST para aplicar firewall y balanceo |
| **InfluxDB**         | Base de datos de series temporales para guardar métricas              |
| **Grafana**          | Visualización en tiempo real de métricas y reglas activas             |


## Arquitectura
     ┌──────────────────────────────────────────────┐
     │                  fireBalancer                │
     └──────────────────────────────────────────────┘
                   │                       ▲
                   ▼                       │
      ┌─────────────────────┐   REST API   │
      │      Containernet   │◄─────────────┘
      │                     │
      │   ┌──────────────┐  │
      │   │ Switch (OVS) │◄─────────────┐
      │   └─────┬────────┘              │
      │         │                       ▼
      │   ┌─────▼──────┐        ┌────────────┐
      │   │ Docker h1  │        │  Docker h2 │    ... hosts
      │   └────────────┘        └────────────┘
      └─────────────────────────────────────────────┘

                         ▲
                         │ (OpenFlow)
               ┌─────────┴─────────┐
               │     ONOS SDN     │
               │   Controller     │
               └──────────────────┘
                         ▲
                         │
                         ▼
           ┌──────────────────────────┐
           │ Python Scripts (control)│
           │ - Firewall rules        │
           │ - Load balancing logic  │
           │ - REST to ONOS          │
           └──────────────────────────┘

                         ▼
          ┌────────────────────────────┐
          │   InfluxDB + Grafana       │
          │  (visualización de métricas)│
          └────────────────────────────┘


## Containernet setup
# 1. Install Ansible
sudo apt-get update
sudo apt-get install ansible

# 2. Clone the Containernet repository
git clone https://github.com/containernet/containernet.git
cd containernet

# 3. Run the Ansible playbook to install dependencies
sudo ansible-playbook -i "localhost," -c local ansible/install.yml

# 4. (If you get a "openflow" directory error, run this before step 3)
# rm -rf openflow

# 5. Set up a Python virtual environment
python3 -m venv venv
source venv/bin/activate

# 6. Install Containernet inside the virtual environment
# For editable mode (development):
pip install -e . --no-binary :all:
# For regular installation:
# pip install .

# 7. (Optional) Add your user to the Docker group to avoid using sudo with Docker
sudo usermod -aG docker $USER
# Log out and back in for changes to take effect

# 8. Run a basic example
sudo -E env PATH=$PATH python3 examples/containernet_example.py

## ONOS setup
docker pull onosproject/onos

docker run -d --name onos -p 8181:8181 -p 8101:8101 -p 6653:6653 onosproject/onos

