# Git commands overview

Overview of some useful commands to get projects up and running quickly.<br>
For a complete overview including explaination, see [git-scm](https://git-scm.com/doc).

## First time setup:

### Global config:
```
$ git config --global user.name "first_name last_name"
$ git config --global user.email "email@domain.com"
$ git config --global init.defaultBranch main
```
(Github uses 'main' as default branch, Gitlab uses 'master')

Verify settings:
> $ git config --list

### Set up SSH:
Gitlab: follow steps at [User settings > SSH Keys](https://gitlab.com/-/profile/keys)<br>
Github: follow steps at [Settings > SSH & GPG Keys](https://github.com/settings/keys)

## Projects:

Start project:
> \$ git init

Set & check remote URL:
> \$ git remote add origin git@github.com:MarkHurenkamp/Cheat-sheets.git
> \$ git remote set-url origin git@github.com:MarkHurenkamp/Cheat-sheets.git
> \$ git config --get remote.origin.url

Download project from URL:
> \$ git clone git@github.com:MarkHurenkamp/Cheat-sheets.git<br>

Basic usage:
> \$ git status<br>
> \$ git diff<br>
> \$ git add .<br>
> \$ git commit -m "My commit message"<br>
> \$ git push -u origin main <br>

Review historic commits:
> \$ git log --pretty="%C(Yellow)%h %C(reset)%ad %C(Cyan)%an: %C(reset)%s" --date=iso8601

Show all branches:
> \$ git branch

Create or switch to different branch:
> \$ git branch foo<br>
> \$ git checkout foo<br>

Commit and push to new (remote) branch:
> \$ git commit -a -m "Another commit message"<br>
> \$ git push origin foo<br>

Merge:
> \$ git checkout main<br>
> \$ git merge foo<br>
> \$ git push origin main<br>

Delete branch (local + remote):
> \$ git branch -d foo<br>
> \$ git push origin :foo<br>

Save local work and revert to earlier commit:
> \$ git stash<br>
> \$ git reset --hard \<index\>

See stashed work and reapply:
> \$ git stash list<br>
> \$ git stash pop 0

Open GUI:
> \$ gitk

Some tips on naming conventions on branches:<br>
[Stackoverflow](https://stackoverflow.com/questions/273695/what-are-some-examples-of-commonly-used-practices-for-naming-git-branches)

