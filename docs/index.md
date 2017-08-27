Once one has pyRedunda installed in their computer, one can import it using

    import pyRedunda

To start using pyRedunda, one needs to create a `Redunda` object first.

    redunda = pyRedunda.Redunda("<insert instance key here>", [{<insert file sync dictionary here>}], "<insert the version of your bot here>")

The first argument to the constructor is one's instance key; one can get a key for their bot from [Redunda](https://redunda.sobotics.org/). This instance key can only be accessed by owners and collaborators of the bot; make sure you give the instance key for your instance!

The _third_ argument is the version of one's bot. This is usually the commit hash of the git repo, or the version (like 0.1.3) of one's bot. This should be of type `str`.

The second argument is a list of files one wants to sync. This should be an empty list (`[]`) if one does not want to sync files with Redunda (Note, one can still upload and download files without specifying the files over here; but, specifying the files over here will make uploading and downloading easier).

Every file should be specified in a dictionary in the following format:

    {"name": "<filename>", "ispickle": <Whether the file is a pickle>, "at_home": <Should be True if the file is at the home directory>}

The `name` specifies the name of the file; this can also be a path to a file. The name is supposed to be of type `str`.

The `ispickle` argument is a `bool`. It should be `False` if the file is not a pickle, but should be `True` if the file is a pickle.

The `at_home` argument is also a `bool`. It should be `True` if the file is at the home directory, but should be `False` otherwise. This argument is necessary as the path to the home directory differs from system to system, thus, if the files have to be synced between two different types of systems and be placed at the home directory, this argument is a must.

Once one has done this, the setup of pyRedunda is done. 

Check out the other pages of the wiki to use pyRedunda.
