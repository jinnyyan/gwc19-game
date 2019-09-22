# M1: Get started with git & run a Python game
[23 SEP 2019]

## References:
* What is git? https://docs.microsoft.com/en-us/azure/devops/learn/git/what-is-git 
* Is git a programming language? Spoiler: NO -- it's a repository https://www.quora.com/What-is-Git-and-GitHub-Is-it-a-programming-language-a-IDE-What-does-it-do 
* What's GitHub vs. GitLab? 3:53 video: https://youtu.be/s8DCpG1PeaU & https://about.gitlab.com/devops-tools/github-vs-gitlab.html

## Setting up your git information:

1. **Open up the command line:**
    1. Left-click the Windows button (bottom left of the screen; has Windows icon). Don't click on anything else!
    1. Using the keyboard, type `cmd`.
    1.  You should see a 'Command Prompt' option; left-click the black terminal screen icon.
1. **Configure git:** If you've never used git before on a computer (or you have and you want to change your user info), do the following two instructions once:
    1. `git config --global user.name 'yourname'`
    1. `git config --global user.email 'youremail@domain.extension'`

## Make a local copy of the game repository:

1. **Determine a storage location:**
    1. Left-click the Windows button (bottom left of the screen; has Windows icon); a menu of options will appear but don't click anything.
    1. Using the keyboard, type `file`.
    1. You should see a 'File Explorer' option; left-click the yellow folder icon.
    1. On the left-hand side of the file explorer, you should see a quick access icon for Desktop (with a blue screen icon). Click on this icon.
    1. Within this location, right-click into a blank area and select the 'New' option in the menu of choices that pops up. Select 'Folder' from the second tier of choices. Name the folder `GWC`. If your folder created with the 'New Folder' name, select it, press the F2 key on the keyboard, type in `GWC` and hit the Enter key. Left-click twice to navigate into this folder. 
    1. At the top of the file explorer window, locate the series of locations that starts with 'This PC' and ends with 'GWC'. Position your mouse over the white space to the right of these names (not one of the names!) and left-click. Press CTRL+c (hold the CTRL key while you simultaneously press 'c' on the keyboard) to copy this address path.
    1. In your command prompt window, type the following ('cd' for change directory with a space following it): `cd ` and then press CTRL+v to paste the address path. Hit enter.
1. **Clone the repository:** While still within the command prompt, type the following: `git clone https://github.com/alystaK/GWC2019game.git`

## Run the game:

1. **Check out the files:** Select the file explorer window and left-click twice into the folder named 'GWC2019game' (this is what you just cloned locally onto the computer you are currently working on!).
    1. There are 2 python files, basicGame2019.py and functionGame2019.py
    1. There are 5 picture files, all with the .jpg file type 
    1. There is 1 PDF file that is a Core 4 reference sheet; this correlates to the icons.
    1. There is 1 PowerPoint file that has the player and icons in an editable format.
    1. There is 1 README.md file that shows information about the repository when viewed from the web interface or opened in a text editor
    1. There is 1 license file that does not have a file extension but may be opened in any text editor.
1. **Run the Python game:**
    1. Right-click the 'basicGame2019.py' file and select 'Edit with IDLE'
    1. For now, don't make any changes to the code (you will soon!).
    1. Hit the F5 button on your keyboard to load the code into a shell.
    1. Because of the way it is coded, this will automatically start the game; move the game window and the Python shell window around on your screen so you can see both of them at the same time.
    1. Use the arrow keys on the keyboard or the 'a','s','d', and 'w' keys to move the player on the board and collect the Core 4!

## Create your own repository (intermediate):

1. **Login to GitHub:** In a web browser, navigate to https://github.com and login. If you don't have an account yet and are under 13, you will need to set up an account with your parent/guardian.
1. **Create a new repository:**
    1. Click on your user icon in the top right of the page and select 'Your repositories'.
    1. Find the green 'New' button towards the right side of the page.
    1. Give your new repository a name that does not include spaces (you may use dashes '-' or underscores '_' if you want visual separation).
    1. Add a comment: `New repository based on https://github.com/alystaK/GWC2019game`
    1. Select Public for your repository's visibility.
    1. Click the box to initialize the repository with a README.
1. **Clone your repository locally:**
    1. Find the 'Clone or download' green button on the right side of your repository's page. If (and only if!) it says 'Clone with SSH', click on the 'Use HTTPS' link. Otherwise click the copy clipboard icon for the HTTPS address.
    1. In your command prompt window, ensure your working directory is still within the GWC folder you created inside your Desktop. Type `git clone ` and paste the address of your new repository with CTRL+v
1. **Add files to your repository:**
    1. Inside file explorer, open the File menu in the top left of the window and select 'Open new window'.
    1. Inside of the new window, click on the up arrow to the left of your location to go up one folder. Next, left-click twice to open the folder that corresponds with your new repository.
    1. In the original file explorer window, copy the basicGame2019.py file and the five jpg files; paste them into your new file explorer window to put them in your new repository.
1. **Commit your changes to your new repository in GitHub's cloud:**
    1. In the command prompt window, type `cd ` and the name of your new repository to enter the git repository directory.
    1. Add your new files to the repository with the command `git add -A`
    1. Check to ensure you have something to commit: `git status`
    1. Add a commit message to your code that identifies what you changed: `git commit -m "added basic game files"`
    1. Push your code to the remote repository: `git push origin master`
    1. When the GitHub login screen appears, enter your username and password. 
    1. You should now be able to see your commit on the webpage when you refresh it!
1. **Additional commits:**
For further changes to your repository, use the following set of commands:
  ```
  git add -A
  git commit -m "description of what you changed"
  git status
  git push
  ```

## Remove your git info from a shared computer:
1. If you're on a shared computer, remove your info at the end of your session:
    1. `git config --global --unset-all user.name`
    1. `git config --global --unset-all user.email`
1. Check to see if it is gone using `git config --list`
1. For further information on git configuration, check out the documentation at https://git-scm.com/docs/git-config/2.1.0