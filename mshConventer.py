import subprocess
import gmsh
# Define the input and output file paths
input_geo_file = "input/singleElement.stl"
output_msh_file = input_geo_file+".msh"

# Generate the mesh using Gmsh
subprocess.run(["gmsh", input_geo_file, "-2", "-o", output_msh_file])

