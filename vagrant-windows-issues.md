# Special Instructions for Windows Vagrant
@channel: People with windows computers are having issues with the vagrant image either 
a) not retaining state when they shut it down or 
b) reseting back to its initial image if they sync it.  

I don't have a Windows machine to check this one, but experimenting with Drew Smith and thinking about it, I think this might "work":
1. Once you have vagrant initially configured using `make vagrant`, exit the shell
2. issue the command `vagrant snapshot save augur <saved-name-of-file>`. 
	- This will be visible in your virtual box admin screen. 
2. Then get back into vagrant using `vagrant ssh` [SHELL A]
3. In a new shell [SHELL B], type `vagrant rsync-auto` This will look like its stalled, but that's how it looks ... this keeps files synced between your vagrant image and your local file browser. 
3. When you are ready to stop using vagrant, use the use `CTRL+c` to stop the process in [SHELL B] **FIRST**. **SECOND**, exit vagrant in [SHELL A]
4. Next, in [SHELL A], issue the command `vagrant suspend`
5. To restart vagrant the "next time" use the `vagrant resume augur` command
6. If you turn your computer off, it seems like it might be a safe move to issue another `vagrant snapshot save augur <saved-name-of-file-<date>>`, like `vagrant snapshot save augur <saved-name-of-file-20190419>`.
7. My *guess* is that you will need to use `vagrant up` after restarting your computer, but I don't know that. Experiment.   