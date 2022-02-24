# CeleryMonitoringPlayground


# How To?

## 1. install requirements
```
pip install -r requirements.txt
```

## 2. start redis
```
docker run -d -p 6379:6379 redis

```

## 3. start celery beat and worker, then flower
```
celery -A app worker --loglevel info -E

celery -A app beat --loglevel info

celery flower -A app --conf=celeryconfig.py

```

## 4. run prometheus and grafana
```
docker run --name Prometheus -d -v <absolute path>/prometheus.yml:/etc/prometheus/prometheus.yml -p 9090:9090 --network host prom/prometheus
docker run --name Grafana -d -v grafana-storage:/var/lib/grafana -p 3000:3000 --network host grafana/grafana

```

## 5. go to localhost:3000
```
use prometheus as datasource(http://localhost:9090->save and test
import, upload celery-monitoring-grafana-dashboard.json


```
