# Contribution Guide

You cannot directly commit to the main branch, because it's protected. So your flow will look like this.

1. **Create a Branch:** Use branches for short-lived periods, to complete a tasks or implement a feature.
2. **Commit to Branch:** Commit often, and write descriptive and concise commit messages.
3. **Open a Pull Request:** The pull request needs to be approved by 1 other contributor to be committed to main. 

# Workflows
Workflows are tests that run when opening a pull request, and they need to be passed in order to accept the pull request. 

The current workflow consists of a Super-Linter, which checks and validates the syntax of any source code.

In case of a failed check, click on the failed check and look for the <font color="#ff7b72">[ERROR]</font> tags, and they'll tell you more information to fix the issue.