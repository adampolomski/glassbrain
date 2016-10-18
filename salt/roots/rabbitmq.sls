rabbitmq:
  pkg.installed:
    - sources:
      - erlang: http://www.rabbitmq.com/releases/erlang/erlang-19.0.4-1.el6.x86_64.rpm
      - rabbitmq-server: https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.5/rabbitmq-server-3.6.5-1.noarch.rpm
  service.running:
    - name: rabbitmq-server
    - require:
      - pkg: rabbitmq