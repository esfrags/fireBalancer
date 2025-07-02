# fireBalancer

**fireBalancer** is an SDN project that implements a firewall and a load balancer using mininet emulation and onos controller. Grafana is used for real time data visualization. 

## Directory

firebalancer/
├── README.md
├── requirements.txt              ← herramientas para análisis, métricas
├── fire_topo.py                  ← topología Mininet conectada a ONOS
├── controller/                   ← scripts que hablan con ONOS vía REST
│   ├── firewall.py               ← añadir/borrar reglas
│   └── balancer.py               ← aplicar balanceo L3/L4
├── metrics-exporter/                      ← scripts que recogen y envían métricas
│   └── export_to_influx.py
├── dashboard/                    ← configs para Grafana + ejemplo de dashboards
│   └── firebalancer_dashboard.json
├── utils/                        ← funciones compartidas: logs, ping tests, etc.
│   └── helpers.py
├── docs/                         ← documentación del proyecto
│   └── architecture.md
└── onos-app/                         ← scripts para lanzar ONOS o configurar apps
    └── start_onos.sh


## Componentes

| Software             | Función                                                               |
| -------------------- | --------------------------------------------------------------------- |
| **Mininet**          | Emulación de red con Mininet                                          |
| **ONOS**             | Controlador SDN que gestiona los switches y flujos vía OpenFlow       |
| **Python (control)** | Scripts que hablan con ONOS por REST para aplicar firewall y balanceo |
| **InfluxDB**         | Base de datos de series temporales para guardar métricas              |
| **Grafana**          | Visualización en tiempo real de métricas y reglas activas             |




