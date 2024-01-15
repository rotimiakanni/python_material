from typing import Annotated

from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()


# Form request fields can be extracted as strings with Form and Annotated from fastapi
# Form fields are not part of the path, they are part of the request body and are sent as form data
# encoded in the body of the request as application/x-www-form-urlencoded.
@app.post("/login/")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    role: Annotated[str, Form()],
):
    print(username, password, role)
    return {"username": username}


# If a param is specified as type File. FastAPI will read the file for you and you will receive the contents as bytes.
# Have in mind that this means that the whole contents will be stored in memory. This will work well for small files.
# But there are several cases in which you might benefit from using UploadFile.
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


# It is recommended to use UploadFile instead of File. Here are some of the reasons:
#  - It uses a "spooled" file: A file stored in memory up to a maximum size limit,
#    and after passing this limit it will be stored in disk.
#  - This means that it will work well for large files like images, videos,
#    large binaries, etc. without consuming all the memory.
#  - You can get metadata from the uploaded file.
# - It exposes an actual Python SpooledTemporaryFile object that you can pass
#  directly to other libraries that expect a file-like object.
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    save_file_to_disk(file)
    return {"filename": file.filename}


def save_file_to_disk(uploaded_file: UploadFile):
    with open(uploaded_file.filename, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
