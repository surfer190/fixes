# Check the SSL Certs

To check the SSL certs being used expiry etc use:

    echo | openssl s_client -showcerts -servername <domain.tld> -connect <servername.domain.tld> 2>/dev/null | openssl x509 -inform pem -noout -text

Example:

    echo | openssl s_client -showcerts -servername example.com -connect registry.example.com:9000 2>/dev/null | openssl x509 -inform pem -noout -text
