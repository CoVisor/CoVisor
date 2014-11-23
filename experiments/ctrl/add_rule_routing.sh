curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"t2-0", "priority":"0", "active":"true", "actions":""}' http://localhost:20001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"t2-1", "priority":"1", "ether-type":"2048", "dst-ip":"1.0.0.1", "active":"true", "actions":"output=1"}' http://localhost:20001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"t2-2", "priority":"1", "ether-type":"2048", "dst-ip":"1.0.0.2", "active":"true", "actions":"output=2"}' http://localhost:20001/wm/staticflowentrypusher/json

