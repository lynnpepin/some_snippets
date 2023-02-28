Git repos on both GitHub and GitLab.

Instead of `git push`, you write `git push gh; git push gl` to push to each, respectively.

From a new project:

```sh
USER_NAME=lynnpepin
REPO_NAME=some_snippets

# first, instantiate your git rep
git init 
git add .
git commit -m "Initial commit"
git branch -M main

# then, add your origins
git remote add gh "git@github.com/$USER_NAME/$REPO_NAME.git"
git remote add gl "git@gitlab.com/$USER_NAME/$REPO_NAME.git"

git push gh
git push gl
```

So, let me note my steps :)

1. `git init; git add .; git commit -m "blahblah"`: Initialize your repo and add a commit as normal.
2. Make a blank repo on GitHub and GitLab
3. `git remote add origin git@gitlab.com:lynnpepin/REPONAMEHERE.git`
4. `git push --set-upstream origin master`
5. `git remote set-url origin --push --add git@github.com:lynnpepin/REPONAMEHERE.git`
6. `git push` as normal.
7. `git remote set-url origin --push --add git@gitlab.com:lynnpepin/REPONAMEHERE.git`: I do this again for good measure...
