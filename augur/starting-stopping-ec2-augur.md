# Making an augur environment on EC2 
1. Check which version of python is default: `which python`
2. Check python version. `python --version` 
3. If needed, install python3 which was not the default. Also installed virtualenv
3. `virtualenv --python=python3 augur` from $HOME
4. `pip install -e .`
4. Check `augur.config.json` For tests I used my `augur.config.json` as a shortcut. 
5. All that seemed to make `make install-dev` work
6. Started augur with `nohup make dev-start &`, which runs it in the background and survives terminal session close
7. You can stop augur then with a regular `make dev-stop`

# To connect and work with augur: 
1. `source augur/bin/activate`
2. cd augur-se, or whatever your directory for augur is.

# To update augur from github repo: 
1. `git status` to see if you have locally changed files that matter.
2. Often, these files are changed by augur when it starts: 
    -   modified:   frontend/public/app.css
    -   modified:   frontend/public/app.css.map
    -   modified:   frontend/public/app.js
    -   modified:   frontend/public/app.js.map
    -   modified:   frontend/public/vendor.js
    -   modified:   frontend/public/vendor.js.map
3. If those are the only files modified, then you should do a `git stash`
4. Next, `make dev-stop` to stop your instance if you followed the instructions above. 
5. Then do a `git pull` to get the updates from your github repository. 
6. If you modified any backend files or routes, or just to be safe, its best to do a `make install-dev`, then
7. You can start augur up again using previous notes. `nohup make dev-start &`


