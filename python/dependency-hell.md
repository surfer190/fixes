# Dependency Hell

1. Breaking changes in a minor release

If a user uses version pinning, then required dependencies requiring a different version will break.

    dependency_a==1.2.1

So we use narrow ranges (downside is package gets outdated):

    dependency_a>=1.3.0,<1.4.0

A broad range means too many versions to support:

    dependency_a>1.2.0,<1.9.0

## Use Semantic Versioning

[Semver.org](https://semver.org/)

    1.2.0
    Major.Minor.Path

* Major - Breaking / incompatible API change (reset other digits)
* Minor - Add functionality in a backwards compatible way. Bump minor version and reset patch.
* Patch - Security or bug fix that doesn't break the API

## Avoid API Churn

You don't want to force user's of your API to change the way they use it

* Removing an API
* Renaming an API
* Changing the parmameters of an API

## Setting your Requirements correctly

Ensure your `install_requires` uses a range and does not pin versions.

Eg. `six>=1.11` is better than `six==1.11.*`

If six uses semver, you could have done `six>1.11,<2`

## Test supported versions

Test your library with every supported python version and with earliest versions of all packages you depend on.

_By default pip installs the latest versions of your dependencies_

## Example

    apache-beam: httplib2>=0.8,<=0.11.3
    google-api-python-client: httplib2>=0.9.2, <1

With:

    pip install apache-beam google-api-python-client

In this case the installation is successful and version that is installed is the upper bound of the overlapping range.
It will install `0.11.3`

With:

    pip install google-api-python-client apache-beam

Gives an error about incompatibilities

> Pip resolves dependencies on a first come first serve basis

> The order your dependencies are installed if you use requirements.txt are arbitrary

## Summary

Help your users:

* Use semantic versioning
* Avoid API churn
* Support as large a version range as possible
* Support the latest version of your dependencies




## Source

* [Dependency hell: a library author’s guide](https://www.youtube.com/watch?v=OaBhcueqNqw)