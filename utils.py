import os
import zipfile
import shutil
import urllib.request
import gdown
import subprocess

BASE_DIR = os.getcwd()
rvc_models_dir = os.path.join(BASE_DIR, 'rvc_models')

voice_models = {"ariana-grande":"1XmsNoOP8vbT7icJ5r1q0spc-JtTwy19i"
,"the-weeknd":"1Xa6M83Vzmys3NL0cERGoouDAS12U3Pl6"
,"villager":"1Xop5JQwBYXPRX5Zc_HEe1wYK82kk-FgH"
,"trump":"1Y54pTA0TyKAc2_afIL1J1xwIeOZnb1Wm"
,"taylor-swift":"1XAGydwT5IZJ5z3x01ZnnMr2132CbSacG"
,"tate":"1JV_LT6AiLcxTshh_ITPqBU0tYAK0C9KG"
,"squidward":"1XujRA1g5QSmEzgAnh_sw-cMK1DP68TVE"
,"spongebob-squarepants":"1XokrEwcsNLLSx15n3pWP7EBq83b7FA2U"
,"siri":"1WsmXBRX9saFxTG2ymf_EkixHLv4inHum"
,"britney-spears":"1XFq_O3VpssFW1CWajXyMeROvudtKfWIZ"
,"pikachu":"1WmU6cJznw5en5Z2yxkrXpZfBwUDnwe8w"
,"obama":"1XJz825ywIl3OVL67oa5QB54niW8aneB_"
,"mrbeast":"1WcHOiJXrWzSgjWJ8AwNf2xPDiEmF-5Lg"
,"mj-raspy":"1WyGSPA4gsMpkDM2cuffYzp174LN1XlHC"
,"megatron":"1WrXWxTwoHepKEnJGJYEvdglp9zMTvAoL"
,"kanye":"1XM1NiWsp7T5idi36CqepMlNvDtmrYPJ5"
,"eminem":"1XWLv1AMF_y0KQC3zx94id8qS05z3Hzou"
,"elon-musk":"1YDKJf081FrEjA1mm74Skp8Vrl9sFA6k6"
,"drake":"1XbNY3Y_B0D9CZDWyz1HNpDtIAjnarz4H"
,"darthvader":"1WeDfGBIUork8vEyfW1LMIQWsPOujhXcp"
,"billie-eilish":"1XDQccGnGy9B39drbc_dw0BHKlSTZClvz"
,"biden":"1XHNWefqHUlrRI-qgRknuI6wS3lYRb3Pg"}

def extract_zip(extraction_folder, zip_name):
    os.makedirs(extraction_folder)
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(extraction_folder)
    os.remove(zip_name)

    index_filepath, model_filepath = None, None
    for root, dirs, files in os.walk(extraction_folder):
        for name in files:
            if name.endswith('.index') and os.stat(os.path.join(root, name)).st_size > 1024 * 100:
                index_filepath = os.path.join(root, name)

            if name.endswith('.pth') and os.stat(os.path.join(root, name)).st_size > 1024 * 1024 * 40:
                model_filepath = os.path.join(root, name)

    if not model_filepath:
        raise Exception(f'No .pth model file was found in the extracted zip. Please check {extraction_folder}.')

    # move model and index file to extraction folder
    os.rename(model_filepath, os.path.join(extraction_folder, os.path.basename(model_filepath)))
    if index_filepath:
        os.rename(index_filepath, os.path.join(extraction_folder, os.path.basename(index_filepath)))

    # remove any unnecessary nested folders
    for filepath in os.listdir(extraction_folder):
        if os.path.isdir(os.path.join(extraction_folder, filepath)):
            shutil.rmtree(os.path.join(extraction_folder, filepath))

def download_online_model(url, dir_name='custom'):
    try:
        print(f'[~] Downloading voice model with name {dir_name}...')
        zip_name = url.split('/')[-1]
        extraction_folder = os.path.join(rvc_models_dir, dir_name)
        if os.path.exists(extraction_folder):
            shutil.rmtree(extraction_folder)

        if 'pixeldrain.com' in url:
            url = f'https://pixeldrain.com/api/file/{zip_name}'

        urllib.request.urlretrieve(url, zip_name)

        print('[~] Extracting zip...')
        extract_zip(extraction_folder, zip_name)
        print(f'[+] {dir_name} Model successfully downloaded!')

    except Exception as e:
        raise Exception(str(e))


def download_gdrive_model(voice):
    # Google Drive file URL (make sure it's shared and accessible)
    file_url = f"https://drive.google.com/uc?id={voice_models[voice]}"

    # Define the destination file name and path
    output_file = f"{voice}.zip"
    os.makedirs(f"rvc_models/{voice}",exist_ok=True)
    # Download the file
    gdown.download(file_url, output_file, quiet=False)

    # Unzip the downloaded file
    with zipfile.ZipFile(output_file, "r") as zip_ref:
        zip_ref.extractall(f"rvc_models/{voice}")

    os.remove(output_file)


def generate_ai_cover(SONG_INPUT,RVC_DIRNAME):
    PITCH_CHANGE = 0 
    PITCH_CHANGE_ALL = 0 
    INDEX_RATE = 0.5 
    FILTER_RADIUS = 3 
    PITCH_DETECTION_ALGO = "rmvpe" 
    CREPE_HOP_LENGTH = 128 
    PROTECT = 0.33 
    REMIX_MIX_RATE = 0.25  
    MAIN_VOL = 0 
    BACKUP_VOL = 0 
    INST_VOL = 0 
    REVERB_SIZE = 0.15 
    REVERB_WETNESS = 0.2 
    REVERB_DRYNESS = 0.8 
    REVERB_DAMPING = 0.7 
    OUTPUT_FORMAT = "mp3" 

    command = [
        "python",
        "src/main.py",
        "-i", SONG_INPUT,
        "-dir", RVC_DIRNAME,
        "-p", str(PITCH_CHANGE),
        "-k",
        "-ir", str(INDEX_RATE),
        "-fr", str(FILTER_RADIUS),
        "-rms", str(REMIX_MIX_RATE),
        "-palgo", PITCH_DETECTION_ALGO,
        "-hop", str(CREPE_HOP_LENGTH),
        "-pro", str(PROTECT),
        "-mv", str(MAIN_VOL),
        "-bv", str(BACKUP_VOL),
        "-iv", str(INST_VOL),
        "-pall", str(PITCH_CHANGE_ALL),
        "-rsize", str(REVERB_SIZE),
        "-rwet", str(REVERB_WETNESS),
        "-rdry", str(REVERB_DRYNESS),
        "-rdamp", str(REVERB_DAMPING),
        "-oformat", OUTPUT_FORMAT
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in process.stdout:
        print(line, end='')
    process.wait()



def move_model(destination_dir):
    file_extension = ".pt"
    # List files in the directory
    files = os.listdir(destination_dir)
    # Check if any file with the desired extension exists
    file_exists = any(file.endswith(file_extension) for file in files)

    if file_exists:
        print(f"A file with the {file_extension} extension exists in the directory.")
    else:
        all_items = os.listdir(destination_dir)
        # Filter for subdirectories (folders)
        subfolders = [item for item in all_items if os.path.isdir(os.path.join(destination_dir, item))]

        source_dir = os.path.join(destination_dir,subfolders[0])
        # Ensure that the destination directory exists
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # List files in the source directory
        files = os.listdir(source_dir)

        # Iterate through the files and move the ones ending with ".pth"
        for file in files:
            if file.endswith(".pth"):
                source_file = os.path.join(source_dir, file)
                destination_file = os.path.join(destination_dir, file)
                shutil.move(source_file, destination_file)
                print(f"Moved {file} to {destination_dir}")
        for file in files:
            if file.endswith(".index"):
                source_file = os.path.join(source_dir, file)
                destination_file = os.path.join(destination_dir, file)
                shutil.move(source_file, destination_file)
                print(f"Moved {file} to {destination_dir}")
