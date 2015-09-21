# pythonize
**Download, install, and configure Python in one line.**

### Quickstart
```
pythonize [--python-version VERSION] [--miniconda] [--packages PACKAGE [PACKAGE...]]
```
Fetch and run in one line:

`git clone https://github.com/princebot/pythonize.git && pythonize/pythonize`

### About

**pythonize** wraps the installation process for the
**[Anaconda Python distribution](https://store.continuum.io/cshop/anaconda/)** and its environment/package manager
**[conda](http://conda.pydata.org/docs/)**, providing you in a single command line with a ready-to-use Python
installation containing any additional packages you specify.

Many tools manage Python packages—but only
if you have Python already. **Pythonize** instead bootstraps Python *and* initializes it with packages.

Run without options, **pythonize** performs these default actions:

* downloads latest Anaconda Python,
* installs using Anaconda defaults,
* updates all Python packages via conda, and
* adds `~/anaconda/bin` or `~/miniconda/bin` to `$PATH`.

Anacond Python comes with 100+ useful Python packages. For a leaner installation (10x smaller) including only the
conda utilityand Python, install miniconda rather than Anaconda using the `--miniconda` option.

For more usage information, check out the man page via `pythonize --help`.

### Backstory

In unruly, wild-west server environments without configuration management, I wrote a lot
of scripts in shell rather than in Python because I couldn't guarantee what Python might exist on any given box.
Using shell was often simpler than dealing with Python compatability issues.

Look through the code of any popular Python open-source project and you'll see repeated hoop-jumping such as
using deprecated libraries, avoiding modern features, and rampant if-statements to catch 2.6 idiosyncracies—all
just to accommodate Python version skew.

Continuum solves this problem extremely well with Anaconda/Miniconda. I wrote **pythonize** to abstract conda away
and make it easy to guarantee Python scripts run anywhere with the same Python version and packages.

Enjoy!
