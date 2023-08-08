# legacy-copy
Scripts to copy data from legacy media such as CDs, Floppy Disks, and Zip Drives. 

## Floppy Copy

The floppy disk workflow was created first in this project. Available in the repository is a Jupyter Notebook that you provide a box directory, and you can automatically create new boxes, disks, and copy images from the Windows Camera folder to the box and disk folders.

The Jupyter notebook uses IPyWidgets to give a small gui to manage creation of folders for boxes and disks, disk contents, and to rename and copy photos from the webcam to either box or disk folders to act as documentation. 

Boxes are collections of disks that were found together. A disk is an individual floppy disk. 

To copy the contents from the disk, you manually select all files and folders in the explorer, and either copypasta or drag and drop to the automatically created contents folder. 

## CD Copy

The CD's in the collection were proving to be more difficult to copy data from, so another approach was developed. 

At first, the floppy process was replicated, however there were many more errors than could be manually handled. So DDRescue was thought to be the solution, an Ubuntu 22.04 machine was set up to automatically run DDRescue on the CDs. 

This was unsatisfactory and took a long time with unclear results. Next I wrote a Python script, `cdxu.py` to copy the contents from the CD to a folder. 

Finally, brought together, I have bash scripts for Ubuntu to run `cdxu.py` and then DDRescue. This process still takes several hours per disk. A second DVD drive was found and the bash script was copied and configured such that `/dev/sr0` or `/dev/sr1` are specified as sources for DDRescue, and `cdxu.py` will look in `/etc/mtab` to find the `/media` mounts for each disk and keep `/dev/sr0` DDRescue with `/media/{sr0}` copy content. 

To help with disk documentation, a similar photo workflow was created for CDs. Take photos of the disks with a webcam, then copy the photos with a new name into the disk folder. 

## Zip Copy

Once we had located a USB based IOmega Zip drive (we had several D-Sub options), the floppy copy workflow was replicated, and the `cdxu.py`  process integrated. 

This process will create a folder for each disk (no boxes this time), copy photos from the Windows Camera app to the folder for each disk, and has a button to run a modified version of `cdxu.py` that is located within the Jupyter notebook. A new button was added to this notebook to automatically run the `cdxu.py` adaptation. 
