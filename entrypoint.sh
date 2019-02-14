#!/bin/sh
set -e

# AWS Envs
export AWS_HOST_IP=$(curl -sf -m 3 http://169.254.169.254/latest/meta-data/local-ipv4)

# Host IP DNS
[ ! -z "$AWS_HOST_IP" ] && final_host_ip="$AWS_HOST_IP"
[ ! -z "$HOST_IP" ] && final_host_ip="$HOST_IP"

[ ! -z "$final_host_ip" ] && echo "$final_host_ip host-ip" >> /etc/hosts

export HOST_IP="$final_host_ip"

# Run Consul Register Control
# python /logger-service/consul_script.py

exec "$@"