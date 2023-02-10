## How do I Contribute ?


**1. Fork the repository**
- Fork the [zero project](https://github.com/0xAckerMan/Zero) by clicking on the fork button on the top of the page.
![](https://i.imgur.com/HrRuOtQ.png)

- This will create a copy of this repository in your account.


**2. clone the repository**
- Now clone the repo to your machine
- Click on the clone button and then click the copy to clipboard icon.
- Open a terminal( bash on linux/mac, command prompt on windows) and run the following git command: ```git clone "url you just copied" ``` 


**3. Create a branch**
- Change to the repository directory on your computer (if you are not already there): ```cd Zero```
- Now create a branch using the ``git checkout`` or ``git branch`` command: 
```bash
git checkout -b branchname
```
or
```bash
git branch branchname
git checkout branchname
```
- For example: 
```bash
git checkout -b K0r3s
```
or 
```bash
git branch K0r3s
git checkout K0r3s
```
Read more on [git and GitHub](https://docs.github.com/en/get-started/quickstart/hello-world)


**4. Make necessary changes and commit those changes**
> Make sure to follow steps laid out on the [README](https://github.com/0xAckerMan/Zero/blob/main/README.md) file to setup the development environment on your machine
- You can now create/modify files in the code repository in reference to the issue you were assigned.
- Save the file.
- On executing the command ``git status``, you'll see there are changes.
- Add those changes to the branch you just created using the ``git add .`` command:
- ``git add <the file you created or ammended>``
- Now commit those changes using the ``git commit`` command:
- ``git commit -m "a description of the contribution made``


**5. Push changes to GitHub**
- Push your changes using the command ``git push``
```bash
git push origin branchname
```
- (replacing < branchname > with the name of the branch you created earlier.)

**6. Submit your changes for review**
- If you go to your repository on GitHub, you’ll see a Compare & pull request button. 
- Click on that button.
- click create pull request button
- Wait for reviews then resolve any issues
- You will get a notification email once the changes have been merged

**You did it! 👏👏👏**
