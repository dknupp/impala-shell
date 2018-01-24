# Impala Interactive Shell

## TL;DR

```
$ virtualenv ~/path/to/my_virtualenv   # <-- This is a path of your choosing.
$ source ~/path/to/my_virtualenv/bin/activate
(my_virtualenv) $ pip install git+git://github.com/dknupp/impala-shell.git
(my_virtualenv) $ impala-shell -i my_impalad.foo.com
```

## System preparation

### On barebones Redhat 7.3 and CentOS 6.8 systems:

```
sudo yum install yum-utils
sudo easy_install pip
sudo pip install virtualenv
sudo yum install git
sudo yum install gcc-c++
sudo yum install python-devel
sudo yum install cyrus-sasl-devel.x86_64
```

### On barebones Ubuntu 14.04 systems:

```
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install virtualenv
sudo apt-get install git
sudo apt-get install gcc-c++
sudo apt-get install build-essential
sudo apt-get install python-dev
sudo apt-get install libsasl2-dev
```

### On barebones OSX systems (this list maye be incomplete):

```
brew install git
```

## To set up a virtualenv

```
$ virtualenv ~/path/to/my_virtualenv   # <-- This is a path of your choosing.
```

This will create a directory that holds the virtual environment, and will put a
copy of the python executable there, with it's own isolated directory for
additional python libs, and some utility scripts.

Activate the virtualenv by invoking

```
$ source ~/path/to/my_virtualenv/bin/activate
```

Your prompt will be by prepending the name of your virtualenv, so you can
always tell which environment you're working in.


## Installing from githhub

(If you decided NOT to create a virtualenv, and instead install into your
system python environment, you'll probably have to sudo the following command.)

```
(my_virtualenv) $ pip install git+git://github.com/dknupp/impala-shell.git
```


## Launching the shell

At this point, you can launch impala-shell as always. If you don't have a real
cluster, you can connect to the mini-cluster on your dev machine.

```
(my_virtualenv) $ impala-shell -i my_impalad.foo.com
Starting Impala Shell without Kerberos authentication
Connected to my_impalad.foo.com:21000
Server version: impalad version 2.9.0-SNAPSHOT RELEASE (build 2cd110014da78d3497529cdd32025b781935cc43)
***********************************************************************************
Welcome to the Impala shell.
(build version not available)

You can run a single query from the command line using the '-q' option.
***********************************************************************************
[my_impalad.foo.com:21000] >
```

Note that if you install this on your dev machine (which why would you? since
you ostensibly already have the Impala repo checked out -- but still) I don't
know whether the ```impala-shell``` command installed by pip will interfere with
```impala-shell``` command that was installed when you last built Impala, so
just a word of warning -- I didn't test this.

If you've done all this in a ```virtualenv```, you can deactivate it by invoking:

```
$ deactivate
```
