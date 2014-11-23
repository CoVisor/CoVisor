curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"t1-0", "priority":"0", "active":"true", "actions":""}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"t1-1", "priority":"1", "ether-type":"2048", "dst-ip":"3.0.0.0", "active":"true", "actions":"set-dst-ip=1.0.0.2"}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"t1-2", "priority":"3", "ether-type":"2048", "src-ip":"1.0.0.0/2", "dst-ip":"3.0.0.0", "active":"true", "actions":"set-dst-ip=1.0.0.1"}' http://localhost:10001/wm/staticflowentrypusher/json

