{% if cookiecutter.add_postgis.lower() == "y" %}FROM postgis/postgis:13-3.3{% else %}FROM postgres:13{% endif %}

COPY ./compose/dev/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance
