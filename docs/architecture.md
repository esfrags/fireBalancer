## Arquitectura
       ┌────────────────────┐
       │      Mininet       │
       │  (SDN topology)    │
       └───────┬────────────┘
               │
         ┌─────▼──────┐
         │ Switch OVS │
         └─────┬──────┘
      ┌────────┴────────┐
      │                 │
  ┌───▼───┐         ┌───▼───┐
  │ Host1 │         │ Host2 │   ← virtual processes
  └───────┘         └───────┘
               ▲
               │
        OpenFlow (6653)
               │
         ┌─────▼─────┐
         │   ONOS    │ ← on Docker Container
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
