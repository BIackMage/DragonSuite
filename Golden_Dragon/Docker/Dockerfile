# syntax=docker/dockerfile:1

# Create TOR Entry Node
FROM alpine:3.14
RUN apk update && apk add --no-cache tor
COPY ./torrc /etc/tor/torrc
COPY ./hidden_service /var/lib/tor/hidden_service/
EXPOSE 80 443 8050 
CMD ["sh", "-c", "chmod 700 /v /var/lib/tor/hidden_service ; tor"]