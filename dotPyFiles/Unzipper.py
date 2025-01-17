import os
import zipfile

data_folder = "/Users/vishnumr/My Files/Programs/Python/Deep Learning 100/data"

# print("Folders:", os.listdir(data_folder))
for folder_name in os.listdir(data_folder):
    if folder_name.endswith(".zip"):
        zip_path = os.path.join(data_folder, folder_name)

        try:
            print(f"Extracting the zip file...: {zip_path}")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(data_folder)
            
            os.remove(zip_path)
            print(f"Unzip Succesful and zip file {zip_path} is deteted!!!")
        except zipfile.BadZipFile:
            print(f"Zip file {zip_path} is curropted")
        except Exception as e:
            print(f"Error occured while porcessing {folder_name}\n Error:{e}")
else:
    print("No Zip files found!!!")