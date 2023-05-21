from util import mkdir


# directory to store the results
results_dir = './results/'
mkdir(results_dir)

# root to the testsets
dataroot = './dataset/test/'
# dataroot = 'F:\BaiduDownloads\CNN_synth_testset/'


# list of synthesis algorithms
vals = ['progan', 'stylegan', 'biggan', 'cyclegan', 'stargan', 'gaugan',
        'crn', 'imle', 'seeingdark', 'san', 'deepfake', 'stylegan2', 'whichfaceisreal']
# vals=['0_real','1_fake']

# indicates if corresponding testset has multiple classes
multiclass = [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]

# model
model_path = 'weights/blur_jpg_prob0.1.pth'
