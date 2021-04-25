from src.cropping.crop_single import crop_single_mammogram
from src.optimal_centers.get_optimal_center_single import get_optimal_center_single
from src.heatmaps.run_producer_single import produce_heatmaps
from src.modeling.run_model_single import run

UPLOAD_FOLDER = 'sample_single_input/'
filename = 'mammogram.png'

def crop_mammogram(selected_view):
    print('Cropping in process...')
    resp = crop_single_mammogram(
        mammogram_path=UPLOAD_FOLDER+filename, 
        view=selected_view, 
        cropped_mammogram_path=UPLOAD_FOLDER+filename,
        metadata_path='sample_single_output/cropped_metadata.pkl',
        horizontal_flip='NO',
        num_iterations=100,
        buffer_size=50
    )
    print('Completed.')
    if resp:
        print(resp)
        return resp

def calc_optimal_centers():
    print('Extracting centers...')
    get_optimal_center_single(
        cropped_mammogram_path=UPLOAD_FOLDER+filename,
        metadata_path='sample_single_output/cropped_metadata.pkl'
    )
    print('Completed.')

def generate_heatmap():
    print('Generating heatmaps...')
    produce_heatmaps(dict(
        device_type='cpu',
        gpu_number=0,

        patch_size=256,

        stride_fixed=70,
        more_patches=5,
        minibatch_size=100,
        seed=0,

        initial_parameters='models/sample_patch_model.p',
        input_channels=3,
        number_of_classes=4,

        cropped_mammogram_path=UPLOAD_FOLDER+filename,
        metadata_path='sample_single_output/cropped_metadata.pkl',
        heatmap_path_malignant='sample_single_output/malignant_heatmap.hdf5',
        heatmap_path_benign='sample_single_output/benign_heatmap.hdf5',

        heatmap_type=[0, 1],  # 0: malignant 1: benign 0: nothing

        use_hdf5=True
    ))
    print('Completed...')

def classify_mammogram(selected_view):
    print('Running Classifier...')
    resp = run({
        "view": selected_view,
        "model_path": 'models/ImageHeatmaps__ModeImage_weights.p',
        "cropped_mammogram_path": UPLOAD_FOLDER+filename,
        "metadata_path": 'sample_single_output/cropped_metadata.pkl',
        "device_type": 'cpu',
        "gpu_number": 0,
        "max_crop_noise": (100, 100),
        "max_crop_size_noise": 100,
        "batch_size": 1,
        "seed": 0,
        "augmentation": True,
        "num_epochs": 10,
        "use_heatmaps": True,
        "heatmap_path_benign": 'sample_single_output/benign_heatmap.hdf5',
        "heatmap_path_malignant": 'sample_single_output/malignant_heatmap.hdf5',
        "use_hdf5": True,
    })
    print('All completed.')
    return resp
