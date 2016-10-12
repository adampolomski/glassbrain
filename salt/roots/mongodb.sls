mongodb.repo:
  pkgrepo.managed:
    - humanname: MongoDB Repository
    - baseurl: https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.2/x86_64/
    - gpgcheck: 1
    - gpgkey: https://www.mongodb.org/static/pgp/server-3.2.asc
    
mongodb.pkg:
  pkg.installed:
    - name: mongodb-org
    - require:
      - pkgrepo: 'mongodb.repo'
      
mongod:
  service.running:
    - enable: True
    - watch:
      - pkg: mongodb.pkg