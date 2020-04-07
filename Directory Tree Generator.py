import os

WorkingDir = os.getcwd()
WatchedFolder = rf'{WorkingDir}\Demo Watched Folder'


def ListToCommas(List):
    for item in List:
        if len(List) == 1:
            CommaSep = ", ".join(List)
        elif len(List) == 2:
            CommaSep = " and ".join(List)
        else:
            List.insert(-1, 'and')
            CommaSep = ", ".join(List)
        return CommaSep


def FolderCountCheck(DirNames):  # Checks Folder total and sets proper version of the word folder.
    if len(DirNames) == 1:
        FolderPlural = 'folder'
    else:
        FolderPlural = 'folders'
    return FolderPlural


DirectoryPath = True

# Uses os.walk to check each directory, folder and file in a watched folder.
for Directory, Folders, Files in os.walk(WatchedFolder):
    if DirectoryPath:
        print(f'The watched directory is located in {Directory}.')
    DirectoryPath = False

# Folder Check

    if len(Folders) == 0:
        pass
    else:
        print(f'The {FolderCountCheck(Folders)} contained in {os.path.basename(WatchedFolder)} are {ListToCommas(Folders)}.')

# Files Check
    if len(Files) == 0:
        pass
    else:
        print(f'The {FolderCountCheck(Folders)} contained are {ListToCommas(Files)}.')

# todo add voice readout of directory info.

print(os.path.dirname(WatchedFolder))
print(os.path.basename(WatchedFolder))