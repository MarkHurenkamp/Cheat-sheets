# Git commands overview

Overview of some useful commands to get projects up and running quickly.<br>
For a complete overview including explaination, see [git-scm](https://git-scm.com/doc).

## First time setup:

### Global config:
```
$ git config --global user.name "first_name last_name"
$ git config --global user.email "email@domain.com"
```
Verify settings:
> $ git config --list

### Set up SSH:
Gitlab: follow steps at [User settings > SSH Keys](https://gitlab.com/-/profile/keys)<br>
Github: follow steps at [Settings > SSH & GPG Keys](https://github.com/settings/keys)

## Projects:

Start project:
> \$ git init

Set & check remote URL:
> \$ git remote set-url origin git@github.com:MarkHurenkamp/TDDBook.git
> \$ git config --get remote.origin.url

Download project from URL:
> \$ git clone git@github.com:MarkHurenkamp/TDDBook.git<br>

Basic usage:
> \$ git status<br>
> \$ git diff<br>
> \$ git add .<br>
> \$ git commit -m "My commit message"<br>

Review historic commits:
> \$ git log --pretty="%C(Yellow)%h %C(reset)%ad %C(Cyan)%an: %C(reset)%s" --date=iso860

Show all branches:
> \$ git branch

Create new branch:
> \$ git checkout 