# install virtualenv

**This insulates you against the many different configuration issues we are seeing on different ec2 servers.  The command may be `yum` instead of `apt` if you are on the Amazon Linux AMI. **

1. `sudo apt install virtualenv`
2. `cd` takes you to your home directory
3. `virtualenv --python=python3 augur` : This creates an augur virtual environment for python 3 that you activate each time you login by : 
4. `cd` takes you to your home directory ... make sure you are there
5. `source augur/bin/activate` will "activate" the virtual environment. 
6. If anyone ever does a `make install-dev` as `sudo make install-dev` then you will have to issue the following command against that directory: `sudo chown -R ubuntu (or ec2-user) augur.egg.info`, for example.  That is the most common.  You can tell if this happened by doing an `ls -l` on your directory at the root of augur and see if any of the directories are owned by root. 


# Do you have ghost images of augur running? 

1. First `ps -ef | grep augur`will tell you
2. try `make dev-stop` from $AUGUR_HOME
3. 

