For this example, we'll be taking the name of the redunda object as `redunda`.

**Uploading and Downloading files specified while constructing the `Redunda` object**

If one has already specified the files one wants to sync with Redunda while constructing the Redunda object, one can upload the files using

    redunda.uploadFiles()

and download them using 

    redunda.downloadFiles()

and the library will download and save them to the location which was specified while uploading them.

**Uploading and Downloading files singlehandedly**

If one wants to upload or download a file which was not specified while constructing the Redunda object, one can do so manually.

To upload a file, use

    redunda.uploadFile("<insert name here>", ispickle=<insert bool here>, at_home=<insert bool here>)

The first argument is the name of the file, and can also be a path to the file.

The second argument, `ispickle`, is an optional argument which is set to `False` by default. One can set it to `True` if the file to be uploaded is a pickle.

The third argument, `at_home`, is also an optional argument set to `False` by default. One can set it to `True` if the file to be uploaded is at the home directory.

To download a file, use

    redunda.downloadFile("<insert name here>", ispickle=<insert bool here>, at_home=<insert bool here>)

The arguments one has to specify are the same as when one is uploading a file.

Unless one have to upload or download a file once, it'll be much easier to upload and download files if one specifies the files while constructing the Redunda object.

