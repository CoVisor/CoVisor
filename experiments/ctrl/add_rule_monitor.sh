curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"flow-mod-1", "priority":"0", "ingress-port":"1", "active":"true", "actions":""}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"flow-mod-2", "priority":"1", "ether-type":"2048", "ingress-port":"1", "src-ip":"1.0.0.0/24", "active":"true", "actions":""}' http://localhost:10001/wm/staticflowentrypusher/json

