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

## Week 22-28/01:
I learned to a Distributed Algorithms Exam. I didn't worked on the project.

## Week 29/01-04/02:
Check main cpp.
The suspect for now is: src\TimeStepper\Optimizer.cpp (~2 Hr.)

main.cpp::main(): load all the files and build everything you need
At the end of main function in line 1427 call to main.cpp::preDrawFunc()
In this function, set the run mode and then call main.cpp::proceedOptimization()
In this function, the main loop, for each iteration from 0 to maxIter save PNG if needs and call Optimizer.cpp::solve() to solve 1 iteration.
After some validations call Optimizer.cpp::fullyImplicit_IP()
In this function, start the timer, call Optimizer.cpp::initX(), stop the timer, start again and then re-compute all the parameters.
My code should be somehow there
Add some debug lines to the code in purpose to ease the next time I dive into the code. (~4 Hr.)

## Week 19-25/02:
Roy gave me model to simulate. He gave me .stl file. Occurs many probelm - the program know to deal with .msh/.ele/.obj/.seg/.pt so first move is to convert it from stl to obj. Both of the files, the source and the converted are in input directory.
So, I ran it but i got a msg "Segmentation fault" - the error comes from IGL - Segmentation Function.
Looking on example to check how to load Obj files.
Temp conclusion: IPC simulation work in this pattern. Given some Object (Geometric) to set the area, simulate the mesh object when they have contact each other.
I used vectary software to create mesh like the object Roy gave me. Unfortunately, just after I finish to copy the object I realized that this software know to export just to geometric object.
In order to solve this, I downloaded gmsh program, I tried to use it but it really uncomfortable. I sent message to Roy to ask him which program I should use. (~3 Hr.)

## Week 14-20/05:
Meeting with Roy about the Project progress. He noticed me how to continue and how the work should be. (~1 Hr.)
Some google about how to convert stl file to msh. (~2 Hr.)
Ask Chat GPT what is the best way to convert from .stl to .msh, the answer I got is to use GMSH program. 
After using it, I got new Error, "corrupted size vs. prev_size in fastbins", It is mean that the file is corrupted ot something.
The error is from line 1099 in main.cpp. when the code try to append the allocation memory according to the msh file. Still nee to check why it is uppening on mesh that created from stl using GMSH program. (~2 Hr.)

## Week 28/05-01/06:
Taking a tutorial on Blender in order to realize how to split and merge the object (~5 Hr.)

## Jun - Jul:
I took a break. I moved my apartment and then the exams 

## Week 30/07-03/08:
Split the provided .stl into two separate Z objects and then merge them back into a single element, 
ensuring that they cannot be split again (~4 Hr.)
Export the merged object as a .msh file. The initial attempt failed, but the subsequent attempt was successful (~1 Hr.)

## Week 06-12/08:
I discovered that there are two types of .msh files. The one exported from Blender is not compatible with the IPC code. After conducting some research, I came across a Python script in the IPC repository itself that can update the .msh file, making it compatible with IPC.
My next steps involve getting this script to run successfully.
I don't know what I'm doing wrong, I tried to install PyMesh by this document: https://pymesh.readthedocs.io/en/latest/installation.html but at the end, the module not installed as needed (~2 Hr.)

## Week 27/08-01/09:
Trying different tests, it seems the problem is with the mesh I make. When I made an .msh file using pymesh, the functions worked like they should. (~1 Hr.)
Found documentation that describe the diffrences between GMSH to msh. In order to create GMSH need to do the following: 
Use Blender to merge the 2 stl's elements -> Export the merged element as obj -> use gmsh lib to generete the gmsh mesh file. (~3 Hr.)

## Week 03-08/09:
I thought other solution. Use both software, Blender and GMSH UI. With Blender Merge the object Then, open it with GMSH and save as msh file.
The first try failed with the error "Invalid Size". First thought that the object is too complex. Probably, it not just it. In the example objects there are many object way more complex like the armadilo219K.  So, I used Blender to reduce the complexity of the object. Then re-format using GMSH.
The second try failed with the error "Segmentation fault"
I think that the only solution is to clone this object using Gmsh. It is not going to be fun at all. (~3 Hr.)
