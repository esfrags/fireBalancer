#!/bin/bash

# Script para lanzar el contenedor de ONOS y activar las apps necesarias
# Proyecto: fireBalancer

CONTAINER_NAME="onos"
ONOS_IMAGE="onosproject/onos"
ONOS_USER="onos"
ONOS_PASS="rocks"
ONOS_PORT=8101

echo "Lanzando contenedor de ONOS..."

# Inicia o reinicia el contenedor
if docker ps -a --format '{{.Names}}' | grep -q "^$CONTAINER_NAME$"; then
    echo "Contenedor existente. Reiniciando..."
    docker restart $CONTAINER_NAME
else
    echo "Contenedor nuevo. Creando..."
    docker run -d --name $CONTAINER_NAME \
        -p 6653:6653 \
        -p 8181:8181 \
        -p 8101:8101 \
        $ONOS_IMAGE
fi

# Esperar a que ONOS arranque
echo "Esperando 10 segundos a que ONOS arranque..."
sleep 10

# Activar las aplicaciones vía SSH
echo "Activando apps en ONOS..."

# Requiere sshpass
if ! command -v sshpass &> /dev/null; then
    echo "sshpass no está instalado. Ejecuta: sudo apt install sshpass"
    exit 1
fi

COMMANDS=(
  "app activate org.onosproject.openflow"
  "app activate org.onosproject.fwd"
  "app activate org.onosproject.hostprovider"
)

for CMD in "${COMMANDS[@]}"; do
    echo "Ejecutando: $CMD"
    sshpass -p "$ONOS_PASS" ssh -p $ONOS_PORT -o StrictHostKeyChecking=no "$ONOS_USER@localhost" "$CMD"
done

echo "ONOS está listo y con las apps activadas."