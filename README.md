# qt_toyapp

Toy application using Qt

## Installation

### User install from anaconda-navigator

Hereafter are the steps in order to install the application using
`anaconda-navigator`. First of all, you have to download the
[`environment.yml`](https://raw.githubusercontent.com/gVallverdu/qt_toyapp/main/environment.yml) 
file provided in this repository.

1. Open `anaconda-navigator`
2. On the left, go to the Environments tab
3. At the bottom, click on the import button and open the `environment.yml` file

When it is done, a new environment named `tapp` should appear in the list.
Click on the green triangle and select `Open Terminal`. There, enter the
following command to run the application

```
(tapp) C:\ toyapp
```

### User from command line

First create a new environment. For example, using conda:

```
$ > conda env create --name tapp python=3.9
```

where `tapp` is the name of the environnement. Then activate the 
environment and install toyapp.

```
$ > conda activate tapp
$ > pip install git+https://github.com/gVallverdu/qt_toyapp.git
```

You can now run the application from anywhere in the console
using the `toyapp` command:

```
$ > toyapp
```

If you prefer to do it in one shot, the following command may do the job

```
$ > conda env create -f environment.yml
```

### Developer installation

First, set up the environment. For example, using conda:

```
$ > conda env create --name tapp python=3.9
```

where `tapp` is the name of the environnement. Then clone the repository
containing the source files of the application and change to the
new directory `qt_toyapp`:

```
$ > git clone https://github.com/gVallverdu/qt_toyapp.git
$ > cd qt_toyapp
```

activate the environment and install dependencies

```
$ > conda activate tapp
$ > pip install -r requirements.txt
```

Alternatively, from the git folder of the application you can install
the application in developer. This will allow you to run the application
from anywhere, using the `toyapp` command. In the git root directory
(the one of this README file or the `setup.cfg` file) run:

```
$ > conda activate tapp
$ > pip install -e .
```

Finally you can run the application either from

```
$ > python src/toyapp/app.py
```

or directly using the `toyapp` command if you installed it

```
$ > toyapp
```