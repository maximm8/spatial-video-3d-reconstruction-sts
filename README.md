# 3D reconstruction using Apple Spatial Video and spacetime stereo algorithm

object 3D reconstruction using spacetime stereo approach and Apple spatial video sequence captured by iphone 15 pro

# Requirements
 - opencv
 - open3d
 - spacetimestereo

# Starbucks cup dataset
### input 
<img src="docs/starbucks_cup_laser.gif" alt="captured sequence" style="width:800px;"/>
 <!-- <video src="docs/starbucks_cup_laser.mp4" controls="controls" style="width: 800px;"> </video> -->
 
 ### or
<img src="docs/starbucks_cup_projector.gif" alt="captured sequence" style="width:800px;"/>

### point cloud
<img src="docs/starbucks_cup_pc_anim.gif" alt="point cloud" style="width:800px;"/>
 <!-- <video src="docs/starbucks_cup_animation.mp4" controls="controls" style="width: 800px;"> </video> -->

### disparity map
 <img src="docs/starbucks_cup_disparity.png" alt="disparity map" style="width:800px;"/>


# Usage

```
python run_reconstruction.py
```

# References 
- [spacetime stereo python library](https://github.com/maximm8/spacetimestereo)
- [Spacetime Stereo: A Unifying Framework for Depth from Triangulation.](https://graphics.stanford.edu/papers/SpacetimeStereo/)  
   James Davis, Ravi Ramamoothi, Szymon Rusinkiewicz.  
Computer Vision and Pattern Recognition (CVPR), 2003  

