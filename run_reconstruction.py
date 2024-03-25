import cv2
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
import os

import spacetimestereo as sts


dataset_folder  = f'data/'
result_folder   = f'results/'

dataset_name    = 'starbucks_cup'

data_folder     = f'{dataset_folder}/{dataset_name}/'
output_folder   = f'{result_folder}/{dataset_name}/'

# data_folder = 'data/2024-03-20 15-09-49_rect'
# output_folder = 'results/2024-03-20 15-09-49_rect'


shadow_th           = 100
black_white_ind     = (0, 1)
disp_range          = (30, 80)
device              = 'cuda'# or 'cpu' 
batches             = 8 # try 10 if out of memory
filter_size         = 3 # spatial smoothing window size

ss  = sts.SpacetimeStereo()

# load data
print('load data')
ss.load_params(data_folder)
imgs1, imgs2 = ss.load_images(data_folder)
texture_img  = imgs1[0]
imgs1.pop(0), imgs2.pop(0)

# calculate disparity map using spacetime stereo
print('calculate disparity map')
disparity_map = ss.calc_disparity(imgs1, imgs2, disp_range, filter_size, device, batches)
shadow_map, _, _ = ss.calc_shadow_map_from_array(imgs1, shadow_th)

#clean edges
print('clean disparity map')
disparity_map *= shadow_map
disparity_map[:,0:disp_range[1]] = 0
disparity_map[:,disparity_map.shape[1]-(disp_range[1]-disp_range[0]):disparity_map.shape[1]] = 0

pcd = ss.disparity_to_point_cloud(-disparity_map, texture_img, z_lim=[00, 600])

# postprocessing point cloud using open3D
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
pcd, ind = pcd.remove_radius_outlier(nb_points=20, radius=1)

print('show results')
# show disparity map
plt.imshow(disparity_map), plt.show()
# show point cloud
o3d.visualization.draw_geometries([pcd])

# save results
print('save results')
if not os.path.exists(output_folder): os.mkdir(output_folder)
disparity_map_color =  sts.disparity_map_to_color(disparity_map)
cv2.imwrite(f'{output_folder}/disparity.png', disparity_map_color)
o3d.io.write_point_cloud(f'{output_folder}/point_cloud.ply', pcd)
np.save(f'{output_folder}/disparity.npy', disparity_map)