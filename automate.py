import os

# Define the folder structure
folders = [
    "Collections",
    "Donors",
    "Events",
    "Organization",
    "Users"
]

entity = [
    "collections",
    "donors",
    "events",
    "organization",
    "users"
]

# Define the base directory and subdirectories
base_dir = ""
controllers_dir = os.path.join(base_dir, "app", "Controllers", "API")
models_dir = os.path.join(base_dir, "app", "Models")

# Create folders and files for Controllers
for folder in folders:
    # Create folder inside Controllers/API
    folder_path = os.path.join(controllers_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print(f"📁 {folder} already exists.")
    
    # Create PHP file inside folder
    file_name = folder + "Controller.php"
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            # Write some content to the PHP file
            file.write("<?php\n")
            file.write(f"namespace App\Controllers\API\{folder};")
            file.write("\n")
            file.write(f"use App\Controllers\BaseController;")
            file.write("\n\n")
            file.write(f"class {folder}Controller extends BaseController\n")
            file.write("{\n")
            file.write("}\n")
    else:
        print(f"    📄 {file_name} already exists.")

# Create folders and files for Models
for folder in folders:
    index = folders.index(folder)
    # Create folder inside Models
    folder_path = os.path.join(models_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print(f"📁 {folder} already exists.")

    # Create PHP model file inside folder
    file_name = folder + "Model.php"
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            # Write some content to the PHP model file
            file.write("<?php\n")
            file.write(f"namespace App\Models\{folder}; \n")
            file.write(f"use CodeIgniter\Model; \n\n")
            file.write(f"class {folder}Model extends Model\n")
            file.write("{\n")
            file.write(f"    protected $table = '{entity[index]}';\n")
            file.write(f"    protected $primaryKey = 'id';\n\n")
            file.write(f"    protected $allowedFields = [];\n\n")
            file.write("}\n")
    else:
        print(f"    📄 {file_name} already exists.")

print("Folders and files created successfully.")
