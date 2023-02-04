### Zvi Knoll,
University of Haifa, Computer Science
Computer Graphics lab course

# IPC - Incremental Potential Contact

## Progress Report:
## Week 6-12/11:
Reading the paper introduction, (~2 Hr.)
Setting up the git repository, (~1 Hr.)
Initial review of the code, (~2 Hr.)

## Week 13-19/11:
Spending about 7 hours to install correctly SuiteSparse, contains BLAS, LAPACK.
Something is getting wrong. I have downloaded the files from https://icl.utk.edu/lapack-for-windows/lapack/index.html#build and build it by the manual. The cmake build lapacke and BLAS successfully.
Next step. CMAKE suiteSparse. not matter what I have done, the cmake can't find BLAS on the system.
Please help me to build IPC as well. (~7 Hr.)

## Week 18-24/12:
Talking with Roy about the project and present him the error I'm getting while initlizing SuiteSparse, Blas & Lapacke. (~1 Hr.)
Roy suggested to use VS Code with Ubuntu WSL.
Good advice! The installtion success. (~3 Hr.)
Now I got new Error, Hurray!!!
undefined reference to `IPC::IglUtils::

Also, spent time to enable editing through VSCode not as admin

## 26/12/22:
Annoucment!!! [100%] Built target IPC_bin (~4 Hr.)
Unbelieveable!!

## Week 01-07/01/23:
Start to play with IPC. Read the Readme file and start to understand what to do with this program. (~4 Hr.)

## Week 08-14/01:
Reading the Wiki file step by step in order to understand some of the parameters. (~2 Hr.)
Starting to debug the code. Line by line to reveal where my addition to IPC should be implement. (~2 Hr.)
According to the talk with Roy on 18/12 my project is to enable the simulation on object that consisting from identical pieces.
It should be in mesh.cpp.
Debuging main.cpp. Still hard to see where is the loop that run until the iteration number done.
Also, need to check what I should implement. Is it one big mesh and then all the mess triangle should act like one object, or the purpose is to implemnt it when to objects are nearby and the same force is up to both. (~4 Hr.)

## Week 15-21/01:
Unfortunately my wife's grandfather past away, I didn't worked on the project

## 22-28/01:
I learned to a Distributed Algorithms Exam. I didn't worked on the project.

## 29/01-04/02:
Check main cpp.
The suspect for now is: src\TimeStepper\Optimizer.cpp (~2Hr.)

main.cpp::main(): load all the files and build everything you need
At the end of main function in line 1427 call to main.cpp::preDrawFunc()
In this function, set the run mode and then call main.cpp::proceedOptimization()
In this function, the main loop, for each iteration from 0 to maxIter save PNG if needs and call Optimizer.cpp::solve() to solve 1 iteration.
After some validations call Optimizer.cpp::fullyImplicit_IP()
In this function, start the timer, call Optimizer.cpp::initX(), stop the timer, start again and then re-compute all the parameters.
My code should be somehow there
Add some debug lines to the code in purpose to ease the next time I dive into the code. (~4Hr.)
