import shutil
import os
import sys

DEBUG = False


class Settings:
    PROJECT_NAME = "1 - Iniciar ensaio.py"  # Name of the project in the MagicBox
    PROJECT_MAIN_FILE_NAME = "main.py"  # Name of the main file of the project

    PROJECT_SOURCES_PATH = f"src/"  # Path to the project sources

    @staticmethod
    def generate_paths() -> None:
        '''
        Get the path to the MagicBox from arguments
        '''
        if DEBUG:
            Settings.MAGICBOX_PATH = "dist"
        else:
            if len(sys.argv) < 2:  # Check if the path was provided
                print("No MagicBox path was provided, use: `python magicbox_uploader.py <magicbox root path>`")
                exit(1)

            Settings.MAGICBOX_PATH = sys.argv[1]  # Get the path from the arguments

        Settings.MAGICBOX_SCRIPT_FOLDER_NAME = "Script"  # Name of the MagicBox script folder

        # Path to the MagicBox script folder
        Settings.MAGICBOX_SCRIPT_PATH = f"{Settings.MAGICBOX_PATH}/{Settings.MAGICBOX_SCRIPT_FOLDER_NAME}"

        # Path to the MagicBox project main file
        Settings.MAGICBOX_PROJECT_MAIN_FILE = f"{Settings.MAGICBOX_SCRIPT_PATH}/{Settings.PROJECT_MAIN_FILE_NAME}"

    @staticmethod
    def setup() -> None:
        '''
        Setup the settings
        '''
        Settings.generate_paths()


class FileManager:
    @staticmethod
    def get_paths(path) -> list[str]:
        """
        Return the source files and folders in the path
        """
        return [os.path.join(path, file) for file in os.listdir(path)]

    @staticmethod
    def copy_paths(paths, destination) -> None:
        """
        Copy the paths to the destination
        """
        for path in paths:
            if os.path.isdir(path):
                shutil.copytree(path, f"{destination}/{path.split('/')[-1]}")
            else:
                shutil.copy(path, destination)

    @staticmethod
    def delete(paths) -> None:
        """
        Delete the paths
        """
        for path in paths:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)

    @staticmethod
    def rename(path, new_name) -> None:
        """
        Rename the path to the new name
        """
        os.rename(path, new_name)


class MagicBoxUploader:

    @staticmethod
    def clean() -> None:
        """
        Delete the files from the MagicBox
        """
        project_sources = FileManager.get_paths(Settings.MAGICBOX_SCRIPT_PATH)  # Get the project sources
        FileManager.delete(project_sources)  # Delete the project sources from the MagicBox

    @staticmethod
    def upload() -> None:
        """
        Upload the files to the MagicBox
        """
        print('Cleaning the MagicBox project sources...', end='')
        MagicBoxUploader.clean()  # Delete the project sources from the MagicBox
        print('Done!')

        print('Getting the project sources...')
        project_sources = FileManager.get_paths(Settings.PROJECT_SOURCES_PATH)  # Get the project sources
        print('Founded the following paths:')
        for path in project_sources:
            print(f'\t{path}')

        print('Uploading the project sources to the MagicBox...', end='')
        FileManager.copy_paths(project_sources, Settings.MAGICBOX_SCRIPT_PATH)  # Copy the project sources to the MagicBox
        print('Done!')

        print('Renaming the main file...', end='')
        FileManager.rename(Settings.MAGICBOX_PROJECT_MAIN_FILE,
                           f"{Settings.MAGICBOX_SCRIPT_PATH}/{Settings.PROJECT_NAME}.py")
        print('Done!')


if __name__ == "__main__":
    Settings.setup()  # Setup the settings
    MagicBoxUploader.upload()  # Upload the files to the MagicBox
