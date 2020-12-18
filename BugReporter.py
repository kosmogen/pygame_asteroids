from github import Github
from getpass import getpass
import sys

if __name__ == '__main__':
    print('You must have a Github account to report a bug. If you do not have one already, please make one now.')
    github_username = input('Github Username:')
    github_password = getpass('Github Password:')
    
    print('Ok, please tell me a little about what happened.')
    title = input('Give the bug report a title:')
    print('Ok, now please give me a brief summary of what happened. You can input multiple lines and press Ctrl+d when done.')
    body = sys.stdin.readlines()

    github_user = Github(github_username, github_password)
    repo = github_user.get_repo('/kosmogen/pygame_asteroids')
    new_issue = repo.create_issue(title, body)