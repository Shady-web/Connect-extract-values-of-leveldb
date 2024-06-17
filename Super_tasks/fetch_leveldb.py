import os
import shutil
import leveldb
import json

# Locate Chrome's local storage directory
def get_chrome_storage_dir():
    home = os.path.expanduser("~")
    chrome_data_path = os.path.join(home, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Local Storage", "leveldb")
    if not os.path.exists(chrome_data_path):
        raise Exception("Chrome local storage path not found.")
    return chrome_data_path

# Copy the LevelDB files to a temporary directory
def copy_leveldb_files(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_dir, dest_dir)

# Fetch a specific value from LevelDB
def fetch_value_from_leveldb(db_path, key):
    db = leveldb.LevelDB(db_path)
    raw_value = db.Get(key.encode('utf-8'))
    return raw_value

# Fetch all values from LevelDB
def fetch_all_values_from_leveldb(db_path):
    db = leveldb.LevelDB(db_path)
    all_values = {}
    for key, value in db.RangeIter():
        all_values[key.decode('utf-8')] = value.decode('utf-8')
    return all_values

# Main function to execute the script
def main():
    temp_dir = "C:\\temp\\chrome_leveldb"
    chrome_storage_dir = get_chrome_storage_dir()
    copy_leveldb_files(chrome_storage_dir, temp_dir)

    # Fetch a specific value
    key = "key"
    value = fetch_value_from_leveldb(temp_dir, key)
    print(f"Value for '{key}': {value.decode('utf-8')}")

    # Fetch and display all stored values
    all_values = fetch_all_values_from_leveldb(temp_dir)
    print("All stored values:")
    print(json.dumps(all_values, indent=2))

if __name__ == "__main__":
    main()
