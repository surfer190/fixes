# Secrets module

New as of `python 3.6`

Provides handy tools for random numbers and tokens

        import secrets

Create cryptographically strong random numbers and tokens

The `random` module is not for security

        >>> secrets.randbelow(50)
        41
        >>> secrets.randbits(256)
        113059864457604198581771394989525038054929728339648942356502714572067503369732
        >>> secrets.token_hex(32)
        'fdbdc2d18367d56c29e6091609dbb5272cdba41b2bea5013106a1395efd198dd'
        >>> secrets.token_urlsafe(32)
        'EC-VNjKLI9q11snALRlAkXmJidgLGJ-2qhekEKj5KTA'

Some more [features of the `security` modul eare in the docs](https://docs.python.org/3.6/library/secrets.html#module-secrets)