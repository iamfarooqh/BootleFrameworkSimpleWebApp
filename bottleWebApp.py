#!/usr/local/bin/python3.6
import os
from bottle import route, request, run, redirect

@route('/pdd')
def upload():
    return '''
        <center><h1 style="color: blue;">File Converter</h1><hr style="width: 900px;"><br><br>

        <form action="/upload" method="post" enctype="multipart/form-data">
            <b>Enter Directory Name:</b> &nbsp;&nbsp; <input style="width: 300px; border: 1px solid powderblue; height: 30px;"type="text" name="category" placeholder="No spaces/special characters allowed" required/><br><br>
            <b>Select Excel file:</b> &nbsp;&nbsp; <input style="border: 1px solid powderblue;"type="file" name="upload" required/><br><br>
            <input style="width: 200px; border: 1px solid powderblue;"type="submit" value="Convert" /> &nbsp;&nbsp;
            <input style="width: 200px; border: 1px solid powderblue;"type="reset" value="Reset" />
        </form></center>
    '''

@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.xlsx', '.xls'):
        return "Please upload only files with .xlsx or .xls extention. Click back button from your browser now and retry!"

    do_upload.save_path = "/tmp/CONV_FILES/{category}".format(category=category)
    if not os.path.exists(do_upload.save_path):
        os.makedirs(do_upload.save_path)

    do_upload.file_path = "{path}/{file}".format(path=do_upload.save_path, file=upload.filename)
    upload.save(do_upload.file_path)
    os.system("python3.6 convertFile.py %s" %do_upload.file_path)
    print (do_upload.save_path)
    os.system("mv %s* %s" %(name,do_upload.save_path))
    #return "File successfully saved to '{0}'.".format(save_path)
    return redirect("/list_files")

@route('/list_files')
def do_list():
    return '''
       <center><br><br><br><h3> Conversion is completed. To access the converted files: <a href="http://mydomainname:port/">Click Here</a></h3> <center>
    '''

run(host='0.0.0.0', port=8080, debug=True)
