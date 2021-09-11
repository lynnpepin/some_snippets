Git-multi

I keep having issues setting up repos on GitHub and GitLab because I keep forgetting how to do it.

So, let me note my steps :)

1. `git init; git add .; git commit -m "blahblah"`: Initialize your repo and add a commit as normal.
2. Make a blank repo on GitHub and GitLab
3. `git remote add origin git@gitlab.com:lynnpepin/REPONAMEHERE.git`
4. `git push --set-upstream origin master`
5. `git remote set-url origin --push --add git@github.com:lynnpepin/REPONAMEHERE.git`
6. `git push` as normal. No need to manage this anymore... I think :)
