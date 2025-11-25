Tim Littlefair's Python Package Template
========================================

This repository was cloned in November 2025 from:
https://github.com/microsoft/python-package-template
Most of the work on the upstream package appears to have been done by
a Microsoft employee called Daniel Ciborowski.

The upstream repository has not been updated since 2023 and may be abandoned.
In this clone, I integrated all outstanding dependabot pull requests up to
November 2025.

I plan to use this as a template for one or more Python packages I am
considering submitting to or updating at PyPi.

As well as updating dependencies, I have also disabled three of the GitHub
actions configured in the outdated upstream template which use secret tokens
to automate to integration to with non-repository services (including GitHub
itself and PyPi).
For the time being I don't wish to automate these integrations but
will consider re-enabling them if and when I am ready to publish my
downstream changes.

> [WARNING]
>
> I have made this repository public on the basis that the integration
> of outstanding dependabot pull requests may be useful to some users.
>
> I am still evaluating whether this repository forms a useful basis for
> the work I am considering using it for.  If and when I do determine
> that it is useful to me I will add some 'how to use' notes of my
> own.  I reserve the right to abandon work and either leave the
> repository unmaintained, archive it, or delete it.

The README.md file for Daniel Ciborowski's 2023 version of this package has
been moved to upstream_README.md.

