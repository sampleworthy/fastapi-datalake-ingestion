from azure.storage.filedatalake import DataLakeServiceClient
from app.config import AZURE_STORAGE_ACCOUNT_NAME, AZURE_STORAGE_ACCOUNT_KEY, AZURE_FILE_SYSTEM

def get_datalake_client():
    return DataLakeServiceClient(
        account_url=f"https://{AZURE_STORAGE_ACCOUNT_NAME}.dfs.core.windows.net",
        credential=AZURE_STORAGE_ACCOUNT_KEY
    )

def upload_json_data(path: str, content: str):
    client = get_datalake_client()
    fs_client = client.get_file_system_client(AZURE_FILE_SYSTEM)
    dir_client = fs_client.get_directory_client("incoming")
    file_client = dir_client.create_file(path)
    file_client.append_data(content, offset=0, length=len(content))
    file_client.flush_data(len(content))
