### Zvi Knoll,
University of Haifa, Computer Science
Computer Graphics lab course

# IPC - Incremental Potential Contact
[GitHub repository](https://github.com/ZviKnoll/IPC---Incremental-Potential-Contact.git)
## Progress Report:
## Week 6-12/11:
Reading the paper introduction, (~2 Hr.)
Setting up the git repository, (~1 Hr.)
Initial review of the code, (~2 Hr.)

## Week 13-19/11:
Spending about 7 hours to install correctly SuiteSparse, contains `BLAS`, `LAPACK`.
Something is getting wrong. I have downloaded the files from https://icl.utk.edu/lapack-for-windows/lapack/index.html#build and build it by the manual. The cmake build `lapacke` and `BLAS` successfully.
Next step. CMAKE suiteSparse. not matter what I have done, the cmake can't find `BLAS` on the system.
Please help me to build IPC as well. (~7 Hr.)

## Week 18-24/12:
Talking with Roy about the project and present him the error I'm getting while initlizing SuiteSparse, `Blas` & `Lapacke`. (~1 Hr.)
Roy suggested to use VS Code with Ubuntu WSL.
Good advice! The installtion success. (~3 Hr.)
Now I got new Error, Hurray!!!
undefined reference to `IPC::IglUtils::`

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
It should be in `mesh.cpp`.
Debuging `main.cpp`. Still hard to see where is the loop that run until the iteration number done.
Also, need to check what I should implement. Is it one big mesh and then all the mesh triangle should act like one object, or the purpose is to implemnt it when to objects are nearby and the same force is up to both. (~4 Hr.)

## Week 15-21/01:
Unfortunately my wife's grandfather past away, I didn't worked on the project

## Week 22-28/01:
I learned to a Distributed Algorithms Exam. I didn't worked on the project.

## Week 29/01-04/02:
Check main cpp.
The suspect for now is: `src\TimeStepper\Optimizer.cpp` (~2 Hr.)

main.cpp::main(): load all the files and build everything you need
At the end of main function in line 1427 call to main.cpp::preDrawFunc()
In this function, set the run mode and then call main.cpp::proceedOptimization()
In this function, the main loop, for each iteration from 0 to maxIter save PNG if needs and call Optimizer.cpp::solve() to solve 1 iteration.
After some validations call `Optimizer.cpp::fullyImplicit_IP()`
In this function, start the timer, call `Optimizer.cpp::initX()`, stop the timer, start again and then re-compute all the parameters.
My code should be somehow there
Add some debug lines to the code in purpose to ease the next time I dive into the code. (~4 Hr.)

## Week 19-25/02:
Roy gave me model to simulate. He gave me .stl file. Occurs many probelm - the program know to deal with .msh/.ele/.obj/.seg/.pt so first move is to convert it from stl to obj. Both of the files, the source and the converted are in input directory.
So, I ran it but i got a msg `"Segmentation fault"` - the error comes from `IGL - Segmentation` Function.
Looking on example to check how to load Obj files.
Temp conclusion: IPC simulation work in this pattern. Given some Object (Geometric) to set the area, simulate the mesh object when they have contact each other.
I used vectary software to create mesh like the object Roy gave me. Unfortunately, just after I finish to copy the object I realized that this software know to export just to geometric object.
In order to solve this, I downloaded `gmsh` program, I tried to use it but it really uncomfortable. I sent message to Roy to ask him which program I should use. (~3 Hr.)

## Week 14-20/05:
Meeting with Roy about the Project progress. He noticed me how to continue and how the work should be. (~1 Hr.)
Some google about how to convert stl file to msh. (~2 Hr.)
Ask ChatGPT what is the best way to convert from .stl to .msh, the answer I got is to use GMSH program. 
After using it, I got new Error, `"corrupted size vs. prev_size in fastbins"`, It is mean that the file is corrupted ot something.
The error is from line 1099 in main.cpp. when the code try to append the allocation memory according to the msh file. Still need to check why it is uppening on mesh that created from stl using GMSH program. (~2 Hr.)

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
The first try failed with the error `"Invalid Size"`. First thought that the object is too complex. Probably, it not just it. In the example objects there are many object way more complex like the armadilo219K.  So, I used Blender to reduce the complexity of the object. Then re-format using GMSH.
The second try failed with the error `"Segmentation fault"`
I think that the only solution is to clone this object using Gmsh. It is not going to be fun at all. (~3 Hr.)

Writing the conclusion (~2 Hr.)

# Conclusion:

IPC Project has 3 parts:
**Understanding IPC repository**
This part took me about three months and approximately 38 work hours.

First, I read research papers and watched videos. IPC is a simulator built by students from the University of Pennsylvania, Adobe Research, and New York University. The purpose of this tool is to simulate the effects of contact between various types of items. This tool enables high-rate time stepping, regardless of the degree of compression and contact.

Second, I forked the Git repository and cloned it to my workspace. A significant amount of time was spent on this step, mainly due to my computer's operating system. This project runs smoothly on Linux. The instructions on how to build it on Windows are very brief and, in the end, may not be possible. After consulting with Roy, he suggested running this project on Ubuntu WSL, which turned out to be a `smart idea`. After a few more hours, I installed and built every library needed for this project, and the IPC simulator built successfully.

Third, I played around with this simulator - it's really cool!

Fourth, I began to understand the code and thought about where I should add my piece of code.

_Partial Summary_
IPC simulator is a highly useful tool for calculating the effects of contact on various items. The code consists of more than 2000 lines, making it quite challenging to comprehend every aspect of it without prior knowledge of IGL, physics, and graphics. Each simulation loads a text file that describes every component of the simulation, including the objects (with paths to mesh files), the obstacles (with paths to STL or OBJ files), and additional instructions such as gravity, speed, object placement, object textures, and density.

![IPC Screenshot1](Report%20assets/Screenshot%202023-09-04%20204820.png)
![IPC Screenshot2](Report%20assets/Screenshot%202023-09-04%20210210.png)
![IPC Screenshot3](Report%20assets/Screenshot%202023-09-04%20210327.png)
![IPC Screenshot4](Report%20assets/Screenshot%202023-09-04%20210332.png)


Roy's task is to investigate how the simulator behaves when an object with multiple identical parts interacts with another object upon contact. After running some tests, I noticed that this functionality might already be implemented. I loaded two objects, a large bar and a cube. When the cube fell onto the bar, as depicted in the picture above, the bar began to twist and was no longer straight. 


**Simulate Roy Object using IPC Simulator**
This part took me about seven months (with long breaks) and approximately 27 work hours.

I had a conversation with Roy, and he assigned me an object to simulate.
![Roy Object](Report%20assets/SingleElement.png)
At this point, I began to realize that IPC is not as user-friendly as I initially thought. While it's a wonderful tool when using predefined example inputs, it becomes more challenging when you want to insert your own elements.

As mentioned earlier, there are two types of objects in this simulator: objects and obstacles. The simulator affects the objects, while the obstacles determine the area and remain unaffected by the simulator. The objects should ideally be mesh files, but the file Roy provided was in STL format.

My next step was to convert this STL file into an MSH file. However, despite my efforts, extensive documentation research, and Google searches, I couldn't find a magic tool that could perform this conversion with a single click.
I told Roy about this situation and he suggest me to use blender. Also, he so that the object has to parts and for good results I should merged it to one.
So, with the fact that I don't know Blender at all I took some tutorials to learn how to use.
After investing some time and effort, I was able to successfully merge the objects and export them as mesh files.
However, my joy was short-lived as I discovered that there are two types of MSH files: standard mesh and Gmsh. The IPC simulator specifically requires Gmsh files. To convert from STL to Gmsh format, I resorted to using the Gmsh software. Unfortunately, this process proved to be far from user-friendly, and to make matters worse, the output Gmsh file wasn't compatible with our simulator.

I believe the most viable approach to create a Gmsh file that is compatible with the IPC simulator is to build it from scratch using the Gmsh library, preferably in Python. This way, you can ensure that the output file is in pure Gmsh format and reduce the risk of encountering issues when running the simulation.

**Check the Simulation on identical pieces**
Unfortunately, I don't succeed to reach this part.

As I describe before, I think that the simulator is fit to Roy needs. With lot of effort it should  be able to create the object that fit to IPC simulator.

Based on your observations and experiments, it seems that when the simulator runs a collision between one object and Roy's object, the latter will twist but not break. Additionally, as demonstrated by Roy's example, if this object were to be used as the sole of a shoe, the person wearing it would not feel any obstacles due to the object's twisting ability.

In the end, I'm grateful for the opportunity this project provided to learn about computer graphics and even some physics. I also feel a sense of regret that it didn't turn out as expected.

Throughout this experience, I gained valuable insights. I learned that when faced with a challenging task, it's important to persevere even when it appears to be a dead-end. Moreover, I recognized the significance of time management in ensuring that tasks are completed on schedule.

I really appreciate the opportunity I was given, and I'm especially grateful for the extension that allowed me to continue even though the project was already past its deadline. This experience has been a valuable learning journey, and I'm thankful for the support and understanding throughout the project.