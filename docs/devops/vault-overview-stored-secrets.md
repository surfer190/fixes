---
author: ''
category: Devops
date: '2019-08-27'
summary: ''
title: Vault Overview - Stored Secrets 
---
# Vault Overview - Stored Secrets

* Vault is a client-server application.
* Only the vault server interacts with the data storage backends.
* All operations are done over a TLS connection.

## Install

1. [Download vault](https://www.vaultproject.io/downloads.html)

2. Copy vault binary to a location on the path:

        cp ~/Downloads/vault /usr/local/bin

3. Install autocomplete

        vault -autocomplete-install

4. Reinitialise the shell:

        exec $SHELL


## Starting the Dev Server

The dev server is a built-in, preconfigured server that is not secure used for playing wit vault. Try it with:

    vault server -dev

View the output and keep the `Unseal Key` and `Root Token`

    Unseal Key: xEaty3tfdw6Rk650aFXZPMZMpsGzQO/Y+P+Yejt8/Eo=
    Root Token: s.IpLvMbTXVgjyANAkuFJBxu7s

> Don't ever run the dev server in production

It does not fork, so leave it open and run a separate terminal.
Set the environment variables:

    export VAULT_ADDR='http://127.0.0.1:8200'
    export VAULT_DEV_ROOT_TOKEN_ID="s.IpLvMbTXVgjyANAkuFJBxu7s"

Verify that the server is running:

    vault status

should return something like:

    Key             Value
    ---             -----
    Seal Type       shamir
    Initialized     true
    Sealed          false
    Total Shares    1
    Threshold       1
    Version         1.1.3
    Cluster Name    vault-cluster-f7f38cf7
    Cluster ID      bc72be78-a52b-715f-f875-4da507be1018
    HA Enabled      false

### Note on Existing Server

Sometimes an existing server has already been initialised. In this case trying to start the server gives:

    $ vault server -dev
    Error initializing listener of type tcp: listen tcp 127.0.0.1:8200: bind: address already in use

In that case double check vault is listening:

    $ lsof -i :8200
    COMMAND   PID    USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    vault   13459 stephen    5u  IPv4 0xe0d88d9fe57581cf      0t0  TCP localhost:trivnet1 (LISTEN)

But vault status might fail:

    $ vault status
    Error checking seal status: Get https://127.0.0.1:8200/v1/sys/seal-status: http: server gave HTTP response to HTTPS client

This is because your environment variables are not set, you need to set `VAULT_ADDR`:

    export VAULT_ADDR='http://127.0.0.1:8200'

Now Everything should work...anyway moving on...

## Our First Secret

> One of the core features of Vault is the ability to read and write arbitrary secrets securely

Secrets written to Vault are encrypted and then written to backend storage. For our dev server, backend storage is in-memory, but in production this would more likely be on disk.

> Vault encrypts the value before it is ever handed to the storage driver. The backend storage mechanism never sees the unencrypted value and doesn't have the means necessary to decrypt it without Vault.

### Writing a Secret

With this template:

    vault kv put <path> <key>=<value>

If is important that the path starts with `secret/`:

    vault kv put secret/google-adwords iol.co.za=Jiso87Gydh332H!

returns:

    Key              Value
    ---              -----
    created_time     2019-08-16T08:57:21.938583Z
    deletion_time    n/a
    destroyed        false
    version          1

It is better to use files to set secrets as the CLI stores history.

### Reading a Secret

With this format:

    vault kv get <path>

Read a secret with:

    vault kv get secret/google-adwords

    ====== Metadata ======
    Key              Value
    ---              -----
    created_time     2019-08-16T08:57:21.938583Z
    deletion_time    n/a
    destroyed        false
    version          1

    ====== Data ======
    Key          Value
    ---          -----
    iol.co.za    Jiso87Gydh332H!

To get only the field value:

    vault kv get -field iol.co.za secret/google-adwords
    Jiso87Gydh332H!

Can also use [jq](https://stedolan.github.io/jq/):

    $ vault kv get -format=json secret/google-adwords | jq -r .data
    {
        "data": {
            "iol.co.za": "Jiso87Gydh332H!"
        },
        "metadata": {
            "created_time": "2019-08-16T08:57:21.938583Z",
            "deletion_time": "",
            "destroyed": false,
            "version": 1
        }
    }

### Delete a Secret

Format is:

    vault kv delete secret/google-adwords

Example:

    $ vault kv delete secret/google-adwords
    Success! Data deleted (if it existed) at: secret/google-adwords

## Secret Engines

All request path's started with `secret/`:

If we try without `secret/` it fails:

    vault write foo/bar a=b

    Error writing data to foo/bar: Error making API request.

    URL: PUT http://127.0.0.1:8200/v1/foo/bar
    Code: 404. Errors:

    * no handler for route 'foo/bar'

> The path prefix tells Vault which secrets engine to which it should route traffic

> By default, Vault enables a secrets engine called kv at the path `secret/`

Vault supports many other secrets engines besides kv, and this feature makes Vault flexible and unique. For example, the aws secrets engine generates AWS IAM access keys on demand. The database secrets engine generates on-demand, time-limited database credentials

### Enable a secrets engine

> Each path is completely isolated and cannot talk to other paths

    $ vault secrets enable -path=kv kv
    Success! Enabled the kv secrets engine at: kv/

`kv` has 2 versions. To enable versioned `kv` secrets enable `kv-v2`

### View secrets engines

    $ vault secrets list
    Path          Type         Accessor              Description
    ----          ----         --------              -----------
    cubbyhole/    cubbyhole    cubbyhole_d44b4637    per-token private secret storage
    identity/     identity     identity_5a7fd29f     identity store
    kv/           kv           kv_4fbfcf52           n/a
    secret/       kv           kv_65c55db4           key/value secret storage
    sys/          system       system_037ee5dd       system endpoints used for control, policy and debugging

Add some secrets:

    vault write kv/my-secret value="s3c(eT"
    vault write kv/hello target=world
    vault write kv/airplane type=boeing class=787

View the secrets in an engine:

    vault list kv
    
    Keys
    ----
    airplane
    hello
    my-secret

### Disable a secrets engine

> When a secrets engine is disabled, all secrets are revoked and the corresponding Vault data and configuration is removed

    vault secrets disable kv/
    Success! Disabled the secrets engine (if it existed) at: kv/

### The power of the secrets engine

It is an abstraction of `read/write/delete/list operations` so vault does not interface directly to physical systems, db's etc.

## Dynamic Secrets

* Dynamic secrets are generated when they are accessed
* Dynamic secrets do not exist until they are read.
* Dynamic secrets can be revoked immediately after use.

### Enable the AWS secrets engine

Enable the AWS secrets engine:

    vault secrets enable -path=aws aws

AWS secrets engine generates dynamic, on-demand AWS access credentials

### Configure the AWS Secrets Engine

Use your root access and secret key

    vault write aws/config/root \
        access_key=AKIAI4SGLQPBX6CSENIQ \
        secret_key=z1Pdn06b3TnpG+9Gwj3ppPSOlAsu08Qw99PUW+eB \
        region=eu-west-2
    
    Success! Data written to: aws/config/root

> These credentials are now stored in this AWS secrets engine

There are special paths in AWS:

* `aws/config`

### Create a Role

A role in vault is a human-friendly identifier to an action (a symlink)

**Warning shit gets real here**

we create a role (map this policy document to a named role) with:

    vault write aws/roles/my-role \
            credential_type=iam_user \
            policy_document=-<<EOF
    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "Stmt1426528957000",
        "Effect": "Allow",
        "Action": [
            "ec2:*"
        ],
        "Resource": [
            "*"
        ]
        }
    ]
    }
    EOF
    
    Success! Data written to: aws/roles/my-role

### Generating the Secret

Ask vault to generate an access keypair

    vault read aws/creds/my-role

This gives you a new set of keys:

    Key                Value
    ---                -----
    lease_id           aws/creds/my-role/0bce0782-32aa-25ec-f61d-c026ff22106e
    lease_duration     768h
    lease_renewable    true
    access_key         AKIAJELUDIANQGRXCTZQ
    secret_key         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
    security_token     <nil>

This creates a role in `AWS IAM`

### Revoke the secret

As per the output, vault will revoke this credential in 768 hours.
Once revoked the keys will no longer be valid.

    vault lease revoke <lease_id>

eg.

    vault lease revoke aws/creds/my-role/0bce0782-32aa-25ec-f61d-c026ff22106
    Success! Revoked lease: aws/creds/my-role/0bce0782-32aa-25ec-f61d-c026ff22106e

## Getting Help

Get help with:

    vault path-help <path>

With the engine enabled do:

    vault path-help aws

> Remember get all paths with `vault secrets list`

You can then dive deeper into a different path:

    vault path-help aws/config/root

## Authentication

Assigning an identity to a Vault user

Authenticating to vault (not other systems)

> When starting the Vault server in dev mode, it automatically logs you in as the root user with admin permissions. In a non-dev setup, you would have had to authenticate first.

Similar to a website, there is a single session token - linked to a browser cookie.
In vault it is called a `Vault token`

### Tokens

> Token authentication is enabled by default in Vault and cannot be disabled

After starting a dev server, your root token is printed.

> The root token is the initial access token to configure Vault. It has root privileges, so it can perform any operation within Vault.

You can create more tokens:

    vault token create
    
    Key                  Value
    ---                  -----
    token                s.YkqvjPjBBrnXVQungkEfgPA8
    token_accessor       Qsc6pssQEpwoPk8ZC0mB41in
    token_duration       ∞
    token_renewable      false
    token_policies       ["root"]
    identity_policies    []
    policies             ["root"]

> By default, this will create a child token of your current token that inherits all the same policies

When a parent token is revoked, children are also revoked - so all tokens a user has created are removed as well.
Important: secrets they created are not removed

To authenticate with a token:

    vault login s.iyNUhq8Ov4hIAx6snw5mB2nL

Revoke a token:

    vault token revoke s.V6T0DxxIg5FbBSre61y1WLgm

> In practice, operators should not use the token create command to generate Vault tokens for users or machines. Instead, those users or machines should authenticate to Vault using any of Vault's configured auth methods such as GitHub, LDAP, AppRole

### Auth Methods

Enable the github auth method:

    vault auth enable -path=github github

> Unlike secrets engines which are enabled at the root router, auth methods are always prefixed with `auth/`. SO github would be accessible at: `auth/github`

> Each auth method has different configuration options

The minimal set of configuration is to map teams to policies

    vault write auth/github/config organization=hashicorp
    vault write auth/github/map/teams/my-team value=default,my-policy

The first command configures Vault to pull authentication data from the "hashicorp" organization on GitHub. The next command tells Vault to map any users who are members of the team "my-team" (in the hashicorp organization) to the policies "default" and "my-policy".

Getting help for an auth method:

    vault auth help github

Logging in with github:

    vault login -method=github

Revoke all tokens using github:

    vault token revoke -mode path auth/github

or disable the auth method:

    vault auth disable github

### LDAP

You can view [all the auth methods here](https://www.vaultproject.io/docs/auth/index.html), but we are looking for the [LDAP](https://www.vaultproject.io/docs/auth/ldap.html) auth method

Enable LDAP:

    vault auth enable ldap 

Configure that specific ldap:

    TODO...

## Authorization (Policies)

> There are some built-in policies that cannot be removed. For example, the root and default policies are required policies and cannot be deleted

Policies are authored in HCL - Hashicorp Config Language

Eg.

    path "secret/*" {
        capabilities = ["create"]
    }
        path "secret/foo" {
        capabilities = ["read"]
    }

With this policy: a user could write any secret to `secret/`, except to `secret/foo`, where only read access is allowed

Vault includes a command that will format the policy automatically according to specification

    vault policy fmt my-policy.hcl

**Everything in Vault must be accessed via the API**

Upload a policy:

    vault policy write my-policy my-policy.hcl

or directly in the terminal:

    vault policy write my-policy -<<EOF
    # Normal servers have version 1 of KV mounted by default, so will need these
    # paths:
    path "secret/*" {
        capabilities = ["create", "update"]
    }
    path "secret/foo" {
        capabilities = ["read"]
    }

    # Dev servers have version 2 of KV mounted by default, so will need these
    # paths:
    path "secret/data/*" {
        capabilities = ["create", "update"]
    }
    path "secret/data/foo" {
        capabilities = ["read"]
    }
    EOF

List policies:

    $ vault policy list
    default
    my-policy
    root

View a policy:

    vault policy read my-policy

Create a token and assign it a policy:

    vault token create -policy=my-policy

Login:

    vault login s.yQ7T7Ec5crX8saqi2xK7n4FM

Ensure you can only read from `secret/foo` but can write elsewhere:

    vault kv put secret/bar robot=beepboop
    
    Key              Value
    ---              -----
    created_time     2019-08-16T12:22:18.882232Z
    deletion_time    n/a
    destroyed        false
    version          1

    vault kv put secret/foo robot=beepboop
    
    Error writing data to secret/data/foo: Error making API request.

    URL: PUT http://127.0.0.1:8200/v1/secret/data/foo
    Code: 403. Errors:

    * 1 error occurred:
            * permission denied
    
> You also do not have access to `sys` according to the policy, so commands like `vault policy list` or `vault secrets list` will not work

### Mapping Policies to Auth Methods

Vault is a single-policy authority... you can't have multiple polcies.
Any enabled auth method must map identities to these core policies

Mapping is specific to each auth method

In github mapping is done per team:

    vault write auth/github/map/teams/default value=my-policy

## Deploying Vault

They want you to use `consul` as a storage backend...yet another hashicorp thing to learn.

Install consul and start it with:

    consul agent -dev

Then create the server config file:

    storage "consul" {
      address = "127.0.0.1:8500"
      path    = "vault/"
    }

    listener "tcp" {
      address     = "127.0.0.1:8200"
      tls_disable = 1
    }

Start the server:

    vault server -config=config.hcl

The vault server will start:

    ==> Vault server configuration:

                Api Address: http://127.0.0.1:8200
                        Cgo: disabled
            Cluster Address: https://127.0.0.1:8201
                Listener 1: tcp (addr: "127.0.0.1:8200", cluster address: "127.0.0.1:8201", max_request_duration: "1m30s", max_request_size: "33554432", tls: "disabled")
                Log Level: info
                    Mlock: supported: false, enabled: false
                    Storage: consul (HA available)
                    Version: Vault v1.1.3
                Version Sha: 9bc820f700f83a7c4bcab54c5323735a581b34eb

    ==> Vault server started! Log data will stream in below

The vault needs to be initialised once per cluster

    vault operator init

which gives:

    $ vault operator init
    Unseal Key 1: LpW6ZhghyvqCkTaX6GwUsjsnP216K7xcePNSGC+LIHjZ
    Unseal Key 2: 0BcUxMP7hxRdpG69XNpjF622RuQYdCRlkTJVucPAwJ66
    Unseal Key 3: M/H2/HpKavzVOSYucG99ua/qSZXAVnCdM2ECzqQE8iXc
    Unseal Key 4: ArwW1NgYpiv3ppD0jDsGsDnv8sL6prNgVHE3A9QDbXIa
    Unseal Key 5: 6+TT1ZlPf/8pYPBm3ThYVHNjmGfVBtgi7XkN9sGJiumf

    Initial Root Token: s.yEhk9w1zGQRaOK0z9E1l9HzK

> This is the only time the unseal keys should be this close together

### Seal / Unseal

> Every initialized Vault server starts in the sealed state

Vault can access the storage but does not know how to decrypt the data.
The process of teaching vault how to decrypt the data is called `unsealing`.

Unsealing has to happen every time vault starts.

It can be done via API or via Command line.

> To unseal the Vault, you must have the threshold number of unseal keys

Unseal the vault:

    vault operator unseal

It will ask for an unseal key:

    Unseal Key (will be hidden): 
    Key                Value
    ---                -----
    Seal Type          shamir
    Initialized        true
    Sealed             true
    Total Shares       5
    Threshold          3
    Unseal Progress    1/3
    Unseal Nonce       b8703efc-04d8-9efa-a178-10fa4f3140f2
    Version            1.1.3
    HA Enabled         true

It is still sealed but progress has been made.

> Multiple people with multiple keys are required to unseal the Vault,so it is good that the unseal process is stateful

> A single malicious operator does not have enough keys to be malicious

Run the unseal command 2 more times

It then becomes unsealed:

    Unseal Key (will be hidden): 
    Key                    Value
    ---                    -----
    Seal Type              shamir
    Initialized            true
    Sealed                 false
    Total Shares           5
    Threshold              3
    Version                1.1.3
    Cluster Name           vault-cluster-8e4c5106
    Cluster ID             be380232-0d5a-571c-b6bd-07b715feb1a9
    HA Enabled             true
    HA Cluster             n/a
    HA Mode                standby
    Active Node Address    <none>

Authenticate with the initial root token:

    vault login s.yEhk9w1zGQRaOK0z9E1l9HzK

As a root user you can reseal the vault with:

    vault operator seal

> A single operator is allowed to do this. This lets a single operator lock down the Vault in an emergency without consulting other operators.

> When the Vault is sealed again, it clears all of its state (including the encryption key) from memory. The Vault is secure and locked down from access.

## Using HTTP Apis

Validate the initialisation status:

    $ http :8200/v1/sys/init
    HTTP/1.1 200 OK
    Cache-Control: no-store
    Content-Length: 21
    Content-Type: application/json
    Date: Mon, 26 Aug 2019 08:06:21 GMT

    {
        "initialized": true
    }

...More stuff in the [docs on the HTTP Api](https://learn.hashicorp.com/vault/getting-started/apis)

## Using the Web UI

On the dev server you cna access the web ui at:

    http://127.0.0.1:8200/ui

You can use the intial dev token to sign in

On non-dev servers you must explicitly enable the `ui` with:

    ui = true

in the `config.hcl`

It runs on the same port as the vault listener






### Source

* [Hashicorp Vault Learn](https://learn.hashicorp.com/vault#getting-started)