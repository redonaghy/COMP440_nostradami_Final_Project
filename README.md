# COMP440_nostradami_Final_Project

## Project goal

## To use this project, you'll need:

a working `python3` installation, `jupyterlab`, `ipython`

jupyter and ipython can be installed with pip. 

If you're having trouble running pip executibles, check out the second response
of [this stack overflow thread](https://stackoverflow.com/questions/35898734/pip-installs-packages-successfully-but-executables-not-found-from-command-line).

## Environment setup:

Place `kaggle.json` in '~/.kaggle' directory, optionally adjust the permissions 
of the file with 

```bash
chmod 600 ~/.kaggle/kaggle.json
```

In the project directory, create a virtual environment with 

```bash
python -m venv venv
```

Then activate the virtual environment with 

```bash
source venv/bin/activate
```

Finally, sync project requirements with 

```bash
pip install -r requirements.txt
```

Now that our virtual environment is configured, we can create a kernel for 
jupyter to use with ipython. That can be done with 

```bash
ipython kernel install --user --name=venv
```

At this point you should now be able to select the venv as a jupyter runtime 
environment and you're good to go!
