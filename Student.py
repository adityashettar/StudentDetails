import sys
          # Check if correct number of argument
if len(sys.argy) == 3:
  script_name = sys.argy[0]
  name = sys.argy[1]
  rollno = sys.argy[2]
  print("User provided input values:")
else:
  script_name =sys.argy[0]
  name = "Deepa"
  rollno = "101"
  print("No input given - using default values:")

print ("Script Name:",script_name)
print ("Student Name:", name)
print ("Roll number:",rollno)
