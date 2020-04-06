import os

WorkingDir = os.getcwd()
WatchedFolder = f'{WorkingDir}/Watched Folder - Demo'
print(WatchedFolder)
DirectoryPath = True


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


def FolderCheck(DirNames):  # Checks Folder total and sets proper version of the word folder.
    if len(DirNames) == 1:
        FolderPlural = 'folder'
    else:
        FolderPlural = 'folders'
    return FolderPlural


def FirstRunCheck(DirPath, DirNames):
    if DirectoryPath:
        print(f'The watched directory is located in {DirPath}.')
    elif len(DirNames) > 0:
        print(f'The directory contains {len(Folders)} {FolderCheck(Folders)} named {ListToCommas(Folders)}.')
        print(f'The {FolderCheck(DirNames)} {ListToCommas(DirNames)}')


# Uses os.walk to check each directory, folder and file in a watched folder.
for Directory, Folders, Files in os.walk(WatchedFolder):
    FirstRunCheck(Directory, Folders)
    if len(Folders) == 0:
        pass
    else:
        print(f'The {FolderCheck(Folders)} contains {ListToCommas(Files)}.\n')
    DirectoryPath = False
