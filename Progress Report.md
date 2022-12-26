### Zvi Knoll,
University of Haifa, Computer Science
Computer Graphics lab course

# IPC - Incremental Potential Contact

## Progress Report:
Week 6-12/11:
Reading the paper introduction, 2 hours
Setting up the git repository, ~1 hour
Initial review of the code, 2 hours

## Week 13-19/11:
Spending about 7 hours to install correctly SuiteSparse, contains BLAS, LAPACK.
Something is getting wrong. I have downloaded the files from https://icl.utk.edu/lapack-for-windows/lapack/index.html#build and build it by the manual. The cmake build lapacke and BLAS successfully.
Next step. CMAKE suiteSparse. not matter what I have done, the cmake can't find BLAS on the system.
Please help me to build IPC as well.

## Week 18-24/12
Talking with Roy about the project and present him the error I'm getting while initlizing SuiteSparse, Blas & Lapacke.
Roy suggested to use VS Code with Ubuntu WSL.
Good advice! The installtion success.
Now I got new Error, Hurray!!!
undefined reference to `IPC::IglUtils::

Also, spent time to enable editing through VSCode not as admin

## 26/12/22
Annoucment!!! [100%] Built target IPC_bin
Unbelieveable!!