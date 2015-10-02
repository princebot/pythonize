# pythonize
<h4>Download, install, and configure Python in one line.</h4>

![pythonize screenshot](http://i.imgur.com/29qmqXw.gif)


## Quickstart

```
pythonize [--python-version PYTHON-VERSION] [--miniconda]
          [--packages PYTHON-PACKAGE [PYTHON-PACKAGE...]]
          [--wrapper APPLICATION-NAME]
```

**Fetch and run in one line:**

```bash
git clone https://github.com/princebot/pythonize.git && pythonize/pythonize
```
When invoked without options, **pythonize** uses
Continuum's [Anaconda](https://www.continuum.io/why-anaconda/)
to install
[Python 2.7](https://docs.python.org/2/whatsnew/2.7.html),
[conda](http://conda.pydata.org/docs/),
[pip](https://pip.readthedocs.org/en/stable), and
[100+ popular Python packages]
(http://docs.continuum.io/anaconda/pkg-docs):

```bash
pythonize
```

**Install the latest version of Python 3:**

```bash
pythonize --python-version 3
```

**Install a specific Python release then add
[httpie](https://github.com/jkbrzt/httpie),
[nose](https://nose.readthedocs.org/en/latest/), and
[click](http://click.pocoo.org/5/):**

```bash
pythonize --python-version 3.3 --packages httpie nose click
```

## Overview
**pythonize** performs unattended download, installation, and configuration for
the **[Anaconda Python distribution](https://www.continuum.io/why-anaconda/)**
and its environment / package manager
**[conda](http://conda.pydata.org/docs/)**: In one command line, you get a
ready-to-use Python preloaded with the libraries you want.

By default, **pythonize** does this:

* downloads the latest Anaconda,
* installs Anaconda noninteractively,
* adds any additional Python packages you specify,
* sets this new installation as your default Python.

Anaconda Python gives you 100+ popular Python packages beyond the Python
standard library — but if you want a leaner installation (10x smaller)
including only Python and **conda**, you can install
**[Miniconda](http://conda.pydata.org/miniconda.html)**
instead by using the `--miniconda` option.

More than making Python set-up ridiculously easy, **pythonize** also
facilitates a novel approach to deploying Python applications on Linux and OS X
systems: With the `--wrapper` option,
**pythonize** *completely abstracts Python version and library dependencies
from the wrapped application's users.*

That means you can code for the Python environment *you* want. You don't need
to grind out kludges for ancient Pythons, add code-clutter
for [Python 2/3 compatability]
(http://python-future.org/quickstart.html#next-steps),
design complex
[egg](http://peak.telecommunity.com/DevCenter/PythonEggs) /
[wheel](https://pypi.python.org/pypi/wheel)
spec files, or leap down the bottomless rabbit hole of
[freezing](http://docs.python-guide.org/en/latest/shipping/freezing/) or
[cross-compiling](http://www.pyinstaller.org/)
your Python code: **Your application just works** — even if your users don't
have Python installed at all.


## Using Wrapper Mode

To see a Python application wrapped with **pythonize** in action, use this
pseudo–one-liner to fetch and run the demo:

```bash
git clone https://github.com/princebot/pythonize.git \
&& pythonize/example_package/example
```

### Invocation

When invoked with the `--wrapper` option, **pythonize** alters its behavior
as follows:
* It skips switching the user's default Python to Anaconda.
* It uses **conda** to satisfy Python version/library dependencies if **conda**
  is already installed rather then creating a fresh installation.
* It always use Miniconda instead of Anaconda.
* It fails rather than merely warns if any items listed with the `--packages`
  option can't be installed.

### Wrapping a Python Application

To make wrapping arbitrary Python programs with **pythonize** as easy as
possible, this repo contains an `example_package` directory with the files
you'll need, already in the recommended layout.

Just follow these steps to get going:

1. Clone this repo: `git clone https://github.com/princebot/pythonize.git`

2. Copy the `example_package` directory and rename it for your application.
   *(Note: For the rest of this section, all pathnames will be relative to this directory.)*

3. Rename the shell wrapper `example` as your main executable (for example,
   `nmapcli`).

4. Replace `.runtime/example.py` with your Python program.

5. Set your Python program's filename to match your main executable, but add a
   `.py` extension (for example, `nmapcli.py`).

6. Edit a couple of variables in `.runtime/wrapper.env` to set your Python
   dependencies:
   
   * `PY_VERSION=<version>`
     
   * `PY_PACKAGES=(<package_list>)`

That's it — you're done. Your Python app is now **pythonized**.

Users will run your application the same way they did before, but as an
implementation detail, the main executable is now a shell wrapper around your
Python program.

The shell wrapper checks that the current execution environment satisfies your
expressed dependencies and, if it doesn't, invokes **pythonize** to fetch the
required Python version and/or libraries before running your Python
app — and the end user doesn't have to do a damned thing.

## More

To read the full user documentation for **pythonize**, consult its manual page:

```bash
pythonize help
```

To discover implementation details (including how this can be
imported as a shell library and used by other utilities in an
[OOP](https://en.wikipedia.org/wiki/Object-oriented_programming)-like style),
browse the source: it's extensively commented for that purpose.

**pythonize** has been tremendously useful to me. I've used it as part of
bootstrapping cloud and local boxen when golden images were unavailable or
nonexistent. I've employed it to package Python apps for sharing
with other engineers at work and to run Python admin scripts in wild-west
server environments where sane configuration management remains a pipe
dream.

I made **pythonize** mainly to scratch my own itch — and now I'm
sharing it, on the off chance some other people may be itchy, too.
![smiley](http://i.imgur.com/SztTrtO.png)
