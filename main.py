import os
import shutil

dir_dict = {'Documents': ['.DOC', '.DOCX', '.HTML', '.HTM', '.ODT',
                          '.PDF', '.XLS', '.XLSX', '.ODS', '.PPT', '.PPTX', '.TXT', '.MD'],
            'Pictures': ['.JPEG', '.JPG', '.GIF', '.TIFF', '.PSD', '.EPS', '.AI', '.INDD',
                         '.RAW', '.PNG', '.BMP', '.XCF'],
            'Video': ['.MP4', '.MOV', '.WMV', '.AVI', '.AVCHD', '.FLV', '.F4V', '.SWF',
                      '.MKV', '.WEBM', '.HTML5', '.OGG'],
            'Music': ['.M4A', '.FLAC', '.MP3', '.WAV', '.WMA', '.AAC']}

common_str = '/home/'+os.getlogin()+'/'
cwd = os.getcwd()


def get_extension(filename):

    split_filename = os.path.splitext(filename)

    return split_filename[1].upper()


# get files in working directory
files = os.listdir()
for file in files:

    extension = get_extension(file)
    file_name = cwd+'/'+file
    if extension in dir_dict['Documents']:
        mv_str = 'Documents'
        file_str = common_str+'Documents/'+file
    elif extension in dir_dict['Pictures']:
        mv_str = 'Pictures'
        file_str = common_str+'Pictures/'+file
    elif extension in dir_dict['Video']:
        mv_str = 'Videos'
        file_str = common_str+'Videos/'+file
    elif extension in dir_dict['Music']:
        mv_str = 'Music'
        file_str = common_str+'Music/'+file

    shutil.move(file_name, file_str)
    print('moved '+file+' to '+mv_str)

print('--------------')
print('Done Scrubbing')
print('--------------')
