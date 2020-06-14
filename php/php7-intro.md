# PHP 7

What happened to 6? It was a faied project due to the ropsed ntroduction of `unicode`

## Most important feature

**Speed** More requests a second, less memory usage

## New features

### Type declarations

Weak typed - does not require declaration of data type.

PHP 5 you were limited to `class` and `array`. It would not allow scalar types.

in PHP 7 scalar types were allowed:

* int
* float
* string
* bool

It is `non-strict`. ie. If you pass a `string` into a function requiring a float the string will be converted as best it can. Eg. "1 week" becomes 1

`strict` types will throw a fatal error.

php 7 also allows return type declarations:

```
declare(strict_types=1);

function getTotal(float $a, float $b): int{
  return $a + $b;
}
```

In the above example a `fatal error` will be thrown. You have to cast to `int` first.

* `strict` mode is per file, not in `php.ini`
* Integers will be `widened` into floats by adding `.0`

### Error handling

Handling fatal errors would not invoke the error handler and would stop the script.
For production servers that causes `white screen of death`

### Operators

Spaceship operator: `<=>`

Checks each component individually...

```
2 < 1 reutrn -1
2 = 1 return 0
2 > 1 return 1
```

If set or, returns left operand if not null, else returns right.

```
$name = $firstName ?? "Guest";

//You can also stack - returns first not null

$name = $firstName ?? $MyName ?? "Guest";
```

### CString

Cryptographically secure sudo-random number generator - secure way of generating random data

Interface to operating systems random number generator

Usage passwords and password salts

`random_bytes` - return random bytes

`random_int(1, 20)` - return random integer

### Unicode Support

For `emoji` and international characters

## Removed Features

*
