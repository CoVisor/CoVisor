curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"t1-1", "priority":"1", "active":"true", "actions":""}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:02", "name":"t1-1", "priority":"1", "active":"true", "actions":"output=1"}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:02", "name":"t1-1", "priority":"1", "active":"true", "actions":"output=2"}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:02", "name":"t1-1", "priority":"1", "active":"true", "actions":"output=3"}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:02", "name":"t1-1", "priority":"1", "active":"true", "actions":"output=4"}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:03", "name":"t3-1", "priority":"5", "active":"true", "actions":"output=2"}' http://localhost:10001/wm/staticflowentrypusher/json
curl -d '{"switch": "00:a4:23:05:00:00:00:02", "name":"t2-1", "priority":"3", "active":"true", "actions":"output=1"}' http://localhost:10001/wm/staticflowentrypusher/json
#curl -d '{"switch": "00:a4:23:05:00:00:00:01", "name":"t1-1", "priority":"1", "ether-type":"2048", "src-ip":"196.188.0.0/16", "dst-ip":"38.40.0.0/8", "active":"true", "actions":"set-dst-ip=200.10.10.12"}' http://localhost:10001/wm/staticflowentrypusher/json

