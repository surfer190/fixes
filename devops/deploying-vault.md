# Deploying Vault

Download vault from:

    https://www.vaultproject.io/downloads.html
    
Ensure SHA256 matches:

    grep linux_amd64 vault_1.2.2_SHA256SUMS 
    7725b35d9ca8be3668abe63481f0731ca4730509419b4eb29fa0b0baa4798458  vault_1.2.2_linux_amd64.zip

    shasum -a 256 vault_1.2.2_linux_amd64.zip 
    7725b35d9ca8be3668abe63481f0731ca4730509419b4eb29fa0b0baa4798458  vault_1.2.2_linux_amd64.zip

Install unzip:

    sudo apt-get install unzip

Unzip the file:

    unzip vault_*.zip

Copy vault to an accessible location:

    sudo cp vault /usr/local/bin/

 Let the binary perform memory locking without unnecessarily elevating its privileges:
 
    sudo setcap cap_ipc_lock=+ep  /usr/local/bin/vault

Create a vault system user:

    sudo useradd -r -d /var/lib/vault -s /bin/nologin vault

The home directory is `/var/lib/vault` 
The shell is set to `/bin/nologin` - restricting the user as non-interactive

Set the owner of `/var/lib/vault`

    sudo install -o vault -g vault -m 750 -d /var/lib/vault

Create `vault.hcl` at `/etc/vault.hcl` with the following:

    ui = true

    backend "file" {
            path = "/var/lib/vault"
    }

    listener "tcp" {
            tls_disable = 0
            tls_cert_file = "/etc/letsencrypt/live/example.com/fullchain.pem"
            tls_key_file = "/etc/letsencrypt/live/example.com/privkey.pem"
    }

Only allow the vault user - vault's configuration file permissions:
    
    sudo chown vault:vault /etc/vault.hcl 
    sudo chmod 640 /etc/vault.hcl

### Create the vault systemd daemon

In `/etc/systemd/system/vault.service`:

    [Unit]
    Description=a tool for managing secrets
    Documentation=https://vaultproject.io/docs/
    After=network.target
    ConditionFileNotEmpty=/etc/vault.hcl

    [Service]
    User=vault
    Group=vault
    ExecStart=/usr/local/bin/vault server -config=/etc/vault.hcl
    ExecReload=/usr/local/bin/kill --signal HUP $MAINPID
    CapabilityBoundingSet=CAP_SYSLOG CAP_IPC_LOCK
    AmbientCapabilities=CAP_IPC_LOCK
    Capabilities=CAP_IPC_LOCK+ep
    SecureBits=keep-caps
    NoNewPrivileges=yes
    KillSignal=SIGINT

    [Install]
    WantedBy=multi-user.target

Additional info in the sources for working with proper permissions on the certificates and routing requests to localhost from the expected domain.

## Initialising Vault

If you are not using https and a domain name set:

    export VAULT_ADDR=http://127.0.0.1:8200

Start vault and check status:

    sudo systemctl start vault
    sudo systemctl status vault

Check vault status

    vault status

which will tell you the server is not yet initialised

    Key                Value
    ---                -----
    Seal Type          shamir
    Initialized        false
    Sealed             true
    Total Shares       0
    Threshold          0
    Unseal Progress    0/0
    Unseal Nonce       n/a
    Version            n/a
    HA Enabled         false

Initialise vault

    vault operator init -key-shares=3 -key-threshold=2

You will now have a sealed vault:

    stephen@vault:/etc$ vault status
    Key                Value
    ---                -----
    Seal Type          shamir
    Initialized        true
    Sealed             true
    Total Shares       3
    Threshold          2
    Unseal Progress    0/2
    Unseal Nonce       n/a
    Version            1.2.2
    HA Enabled         false

So unseal it with (a number of times):

    vault operator unseal

Enable a secrets engine:

    VAULT_TOKEN=$root_token vault secrets enable -path=mimecast kv

Write a secret

    VAULT_TOKEN=$root_token vault write mimecast/fixes.co.za username=mcmaley password=b0LDered!

#### Create a policy

    sudo vim policy.hcl

    path "mimecast/fixes.co.za" {
        capabilities = ["read"]
    }

Enable the policy:

    VAULT_TOKEN=$root_token vault policy write fixes.co.za-readonly policy.hcl

Create a token for that policy:

    VAULT_TOKEN=$root_token vault token create -policy="fixes.co.za-readonly"

View the tokens:

    app_token=xxx
    VAULT_TOKEN=$app_token vault read mimecast/fixes.co.za

Can't list out stuff:

    stephen@vault:~/policies$ VAULT_TOKEN=$app_token vault list mimecast/
    Error listing mimecast/: Error making API request.

    URL: GET http://127.0.0.1:8200/v1/mimecast?list=true
    Code: 403. Errors:

    * 1 error occurred:
        * permission denied


## Make Vault accessible via IP

If you are just testing vault out and want it accessible via IP you can add this to `config.hcl`:

    listener "tcp" {
        address = "10.200.0.69:8200"
        tls_disable = 1
    }

    api_addr = "https://10.200.0.69:8200"

## LDAP Configuration

> The mapping of groups and users in LDAP to Vault policies is managed by using the users/ and groups/ paths.

    VAULT_TOKEN=$root_token vault auth enable ldap

Get the following config:

    url = ldap://ldap.myorg.com
    starttls = False
    insecure_tls = true

    binddn =
    bindpass =
    userdn =
    userattr = uid

    groupdn = 
    groupfilter =
    groupattr =

For more info on the fields check [vault LDAP configuration](https://www.vaultproject.io/docs/auth/ldap.html#configuration)


It is easier to do this via the `web ui` though, because you end up having to do something like this:

    vault write auth/ldap/config \
        url="ldaps://ldap.example.com" \
        userattr="uid" \
        userdn="ou=Users,dc=example,dc=com" \
        discoverdn=true \
        groupdn="ou=Groups,dc=example,dc=com" \
        certificate=@ldap_ca_cert.pem \
        insecure_tls=false \
        starttls=true

Also check out [vault group policy mapping](https://www.vaultproject.io/docs/auth/ldap.html#ldap-group-gt-policy-mapping) it also seems to be better to do this on the ui.

### Auditing

Enable Syslog auditing

    VAULT_TOKEN=$root_token vault audit enable syslog

You can specify special parameters:

    vault audit enable syslog tag="vault" facility="AUTH"

## Source


* [DigitalOcean Vault setup on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-securely-manage-secrets-with-hashicorp-vault-on-ubuntu-16-04)
* [Setup Hashicorp beginners guide](https://devopscube.com/setup-hashicorp-vault-beginners-guide/)

