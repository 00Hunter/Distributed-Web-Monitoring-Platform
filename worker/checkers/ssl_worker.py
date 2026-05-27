from urllib.parse import urlparse, parse_qs
import socket
import ssl


def extract_host_name(url:str):
    parsed_url=urlparse(url)
    port=parsed_url.port or 443
    hostname=parsed_url.hostname
    return hostname,port
    
    
def get_cert_expiry(hostname, port, timeout):
    context = ssl.create_default_context()
    
    with socket.create_connection(port) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as tls_sock:
            cert = tls_sock.getpeercert()
    
    return cert["notAfter"]