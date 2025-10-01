# Creates a sample zip file to work on

cat <<- PLAINTEXT > file_to_zip
    This is some plaintext.
    It will be part of a zip file.
PLAINTEXT

zip -e "zipped_file.zip"  file_to_zip -P "this_is_the_pwd"
