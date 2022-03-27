#--- Release ---
FROM helsons/ubuntu:h1ve_v1

ARG WORKDIR
ENV DEBIAN_FRONTEND noninteractive
ENV WORKDIR_IN ${WORKDIR}
WORKDIR $WORKDIR
RUN mkdir -p $WORKDIR /var/log/CTFd /var/uploads
COPY . $WORKDIR

RUN for d in CTFd/plugins/*; do \
      if [ -f "$d/requirements.txt" ]; then \
        pip install -r $d/requirements.txt; \
      fi; \
    done;

RUN chmod +x $WORKDIR/docker-entrypoint.sh


EXPOSE 8000
ENTRYPOINT ${WORKDIR_IN}/docker-entrypoint.sh
