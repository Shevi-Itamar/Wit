import os
import shutil
from Version import Version
from Modul import Create_a_new_folder, copy_content_of_folder, replace_files_from_folder, delete_folder,initialize_current_folder,count_directories

class repository:
    def __init__(self):
        path = os.path.join(os.getcwd(), '.wit')
        if not os.path.exists(os.path.join(path, 'staging')):
            Create_a_new_folder(path, 'staging')
        if not os.path.exists(os.path.join(path, 'commiting')):
            Create_a_new_folder(path, 'commiting')
        if not os.path.exists(os.path.join(path, 'current version')):
             current_version=Version(path, 'current_version', 'first version')
        self.path_commiting=os.path.join(path,'commiting')
        self.path_staging=os.path.join(path, 'staging')
        self.path_current_version=os.path.join(path, 'current_version')
        initialize_current_folder(os.getcwd(),self.path_current_version)


    def add(self,file_name):
       path=os.path.join(os.getcwd(),file_name)
       if os.path.exists(path):
            if os.path.isfile(path):
                shutil.copy(path, self.path_staging)
                print('The file added successfully')
       else:
            print('This path is not file')


    def commit(self,message):
        if os.listdir(self.path_staging):
            count_commit=count_directories(self.path_commiting)
            name = str(count_commit+1)
            new_version=Version(self.path_commiting,name,message)
            copy_content_of_folder(self.path_current_version,new_version.dir_path)
            replace_files_from_folder(self.path_staging,new_version.dir_path)
            delete_folder(self.path_current_version)
            copy_content_of_folder(new_version.dir_path,self.path_current_version)
            print('The version commiting successfully')
        else:
            print('The staging is empty')


    def log(self):
        list_files=os.listdir(self.path_commiting)
        for commit_name in list_files:
            print("Commit name: "+commit_name)
            my_commit_path=os.path.join(self.path_commiting,commit_name)
            my_detail_path=os.path.join(my_commit_path,'details')
            with open(my_detail_path ,'r')as my_file:
                print("message: "+my_file.readline())


    def status(self):
        if os.listdir(self.path_staging):
            print('You can make commit')
        else:
            print('The staging is empty')



    def checkout(self,commit_id):
        my_path=os.path.join(self.path_commiting,commit_id)
        if os.path.exists(my_path):
            delete_folder(self.path_current_version)
            copy_content_of_folder(my_path,self.path_current_version)
            print('')
        else:
            print('The commit does not exists')

