# Microtubule_processing
- This script can rotate the particles of RELION star file to a certain degree.

- Please calculate the rotation angle and edit the script before executing the script. 
  - e.g. if 3D Classification generates two classes with the microtubule seams in different orientation, this script can be used to rotate the paritcles of one class to the same orientation of the other class, thus re-aligning the particles.
  - The default rotation angle is "194" (=360*7/13), meaning the microtubule seam will be rotated by 7 protofilament. Please change the number accordingly.
  
- python gm_changeRot_singlet.py --starfile input.star
