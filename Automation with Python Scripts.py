import os
import shutil

def organize_images(source_folder, destination_folder):

    if not os.path.exists(source_folder):
        print(f"Error: The source folder '{source_folder}' does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    count = 0

    try:
        for filename in os.listdir(source_folder):
            if filename.lower().endswith(('.jpg', '.jpeg')):
                source_path = os.path.join(source_folder, filename)
                destination_path = os.path.join(destination_folder, filename)

                try:
                    shutil.move(source_path, destination_path)
                    print(f"Successfully moved: {filename}")
                    count += 1
                except Exception as e:
                    print(f"Could not move {filename}: {e}")
    except Exception as e:
        print(f"An error occurred while accessing the folder: {e}")

    print(f"\n--- Automation Summary ---")
    print(f"Total .jpg files moved: {count}")
    print(f"Files are now located in: {destination_folder}")

if __name__ == "__main__":

    src_path = r'C:\Users\mhpak\Downloads' 
    
    dest_path = r'C:\Users\mhpak\Pictures\Organized_JPEGs'

    organize_images(src_path, dest_path)