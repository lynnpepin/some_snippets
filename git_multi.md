Git repos on both GitHub and GitLab.

Instead of `git push`, you write `git push gh; git push gl` to push to each, respectively.

From a new project:

```sh
USER_NAME=lynnpepin
REPO_NAME=some_snippets

# first, instantiate your git repo. (or clone existing)
git init 
git add .
git commit -m "Initial commit"
git branch -M main

# if your repo is a clone from github/gitlab, remove the 'origin' remote
git remote remove origin

# then, add your origins
git remote add gh "git@github.com:$USER_NAME/$REPO_NAME.git"
git remote add gl "git@gitlab.com:$USER_NAME/$REPO_NAME.git"

# finally, push
git push gh
git push gl
```
