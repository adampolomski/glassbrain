epel-release:
  pkg.installed
  
redis:
  pkg.installed:
    - require:
      - pkg: epel-release
  service.running:
    - watch:
      - file: /etc/redis.conf
    - require:
      - pkg: redis
      
/etc/redis.conf:
  file.managed:
    - source: salt://redis/redis.conf