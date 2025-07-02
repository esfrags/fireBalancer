## Arquitectura
       ┌────────────────────┐
       │      Mininet       │
       │  (topología SDN)   │
       └───────┬────────────┘
               │
         ┌─────▼──────┐
         │ Switch OVS │
         └─────┬──────┘
      ┌────────┴────────┐
      │                 │
  ┌───▼───┐         ┌───▼───┐
  │ Host1 │         │ Host2 │   ← procesos virtuales
  └───────┘         └───────┘
               ▲
               │
        OpenFlow (6653)
               │
         ┌─────▼─────┐
         │   ONOS    │ ← en contenedor Docker
         └───────────┘
               │
         REST API (8181)
               │
         ┌─────▼──────┐
         │  Scripts   │ ← firewall, balanceo
         └────────────┘
               │
         ┌─────▼──────┐
         │ Grafana +  │
         │ InfluxDB   │
         └────────────┘
