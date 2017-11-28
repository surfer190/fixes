# Encryption vs Cryptographic Hash

What is the difference between encryption and a cryptographic hash

## Encryption

Create a secret message to send to someone and they do the opposite to decrypt it.
Encryption can always be **reversed** if you know the process or have the correct key.

## Hashing

Hashing is a process that **cannot be undone**. It always changes the same input into the same output.

Cryptographic hasing adds random data, a `salt`, that makes the input data more different and unique.

### Example Using Bcrypt

Install bcrypt

        pip install flask-bcrypt

Import

        from flask_bcrypt import generate_password_hash

Generate the hash

        >>> generate_password_hash('secret')

Output

        b'$2b$12$w/x0Q9FnFydn/vZX26iz7eSNhJUavlm93SI.Kuv4uMATe031dKcpG'

* `b`means `byte-string`
* `$2b` tells you it is `bcrypt`
* `$12` is the number of rounds
* rest is the hash

If you set the rounds really high, it takes longer:

        >>> generate_password_hash('secret', 15)

When a password attempt fails, it is good practise to increase the rounds so it takeslonger to check the hash.Slowing down crackers.

#### Checking password

How do you heck it though...

        >>> hashed_pw = generate_password_hash('secret', 12)
        >>> hashed_pw
        b'$2b$12$tE/SrlIDeO3Efs5lI77ZxeY3hzoAd1on2Lbx0SZnxBEARuSwBvEri'
        >>> hashed_pw == generate_password_hash('secret', 12)
        False

The above does not work.
Youhave to check it with `check_password_hash`

        from flask_bcrypt import check_password_hash

then test it:

        >>> check_password_hash(hashed_pw, 'secret')

