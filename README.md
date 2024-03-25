# 3D reconstruction using Apple Spatial Video and spacetime stereo algorithm

object 3D reconstruation using spatial video sequince captuted by iphone 15 pro using 

# Description
Spacetime stereo is 3D reconstruction  technique that enables precise estimation of the 3D geometry of an object using two or more cameras and an uncalibrated projector. This approach utilizes temporal variation of scene illumination to establish accurate matching between different cameras. As a result, spacetime stereo is capable of generating highly precise 3D reconstructions of objects and scenes.

# Requirements
 - opencv
 - open3d
 - spacetimestereo

<!-- # starbuck cup dataset
captured images  
estimated disparity map  
point cloud   -->


# Usage

launch run_reconstruction.py 

```
python main_show_model.py
```

# References 
- [spacetime stereo python library](https://github.com/maximm8/spacetimestereo)
- [Spacetime Stereo: A Unifying Framework for Depth from Triangulation.](https://graphics.stanford.edu/papers/SpacetimeStereo/)  
   James Davis, Ravi Ramamoothi, Szymon Rusinkiewicz.  
Computer Vision and Pattern Recognition (CVPR), 2003  

