# syntax=docker/dockerfile:1

# Create TOR Entry Node
FROM alpine:3.14
RUN apk update && apk add --no-cache tor
COPY ./torrc /etc/tor/torrc
EXPOSE 9050
CMD ["tor"]