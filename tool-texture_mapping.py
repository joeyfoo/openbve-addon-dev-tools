# This tool helps with generating SetTextureCoordinate commands for CSV objects. 
# Video explanation: https://www.youtube.com/watch?v=6a2mEnoN530
# Last updated: 21 March 2016 / Targets Python 3

axes = ["X", "Y", "Z"]
axisReference = {"X": 0, "Y": 1, "Z": 2}

def get_input_axis(prompt):
    while(True):
        axis = input(prompt)
        if(axis.upper() in axes):
            return(axis.upper())
        else:
            print("Invalid axis.")

def get_float_input(prompt):
    while(True):
        n = input(prompt)
        return(float(n))

if __name__ == "__main__":
    print("Joey's Projection Mapping script for openBVE development!")
    print()
    axis1 = get_input_axis("The object axis that corresponds to the image's horizontal axis: ")
    axis1Min = get_float_input("Position on the object's " + axis1 + " axis that corresponds to the image's LEFT edge: ")
    axis1Max = get_float_input("Position on the object's " + axis1 + " axis that corresponds to the image's RIGHT edge: ")
    print()
    axis2 = get_input_axis("The object axis that corresponds to the image's vertical axis: ")
    axis2Min = get_float_input("Position on the object's " + axis2 + " axis that corresponds to the image's TOP edge: ")
    axis2Max = get_float_input("Position on the object's " + axis2 + " axis that corresponds to the image's BOTTOM edge: ")
    
    print()
    print("Paste the CreateMeshBuilder section (or just all AddVertex commands) below: ")
    
    vertices = []
    
    while(True):
        line = input()
        if(line == "END"): 
            print()
            print()
            print("The generated SetTextureCoordinates commands are below:")
            print("-------------------------------------------------------")
            break
        elif(line == ""):
            print("Type END to end")
        elements = line.split(",")
        for i in elements:
            i = i.strip()
        if(elements[0].lower() == "addvertex"):
            vertices.append((float(elements[1]), float(elements[2]), float(elements[3])))
            #debug print(" -> Vertex added at " + str(vertices[-1]))
        #else:
            #debug print(" -> Command ignored.")
    
    for (i, v) in enumerate(vertices):
        line = "SetTextureCoordinates, "
        line += str(i)
        line += ", "
        #line += axisReference[axis1]
        line += str((v[axisReference[axis1]] - axis1Min)/(axis1Max - axis1Min))
        line += ", "
        line += str((v[axisReference[axis2]] - axis2Min)/(axis2Max - axis2Min))
        print(line)
    
    print("-------------------------------------------------------")
