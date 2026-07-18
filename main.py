import streamlit as st
import hashlib

def group_by_size(uploaded_files):
    dict_size = {}
    for file in uploaded_files:
        size_bytes = file.size
        dict_size.setdefault(size_bytes, []).append(file)
    return {size: files for size, files in dict_size.items() if len(files) > 1}


def get_file_hash(file):
    sha256_hash = hashlib.sha256()
    file.seek(0)
    for chunk in iter(lambda: file.read(4096), b""):
        sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def group_by_hash(candidate_files):
    dict_hash = {}
    for file in candidate_files:
        file_hash = get_file_hash(file)
        dict_hash.setdefault(file_hash, []).append(file)
    return {h: files for h, files in dict_hash.items() if len(files) > 1}


def find_duplicates(uploaded_files):
    size_groups = group_by_size(uploaded_files)
    candidates = []
    for files in size_groups.values():
        candidates.extend(files)
    return group_by_hash(candidates)



# ---------- Streamlit UI ----------
 
st.title("🔍 Duplicate File Finder")
st.write("Select a folder below and this will find any duplicate files inside it (including subfolders).")
 
uploaded_files = st.file_uploader("Choose a folder", accept_multiple_files="directory")
 
if st.button("Scan for Duplicates"):
    if not uploaded_files:
        st.warning("Please upload at least 2 files first.")
    elif len(uploaded_files) < 2:
        st.warning("Upload at least 2 files to check for duplicates.")
    else:
        duplicates = find_duplicates(uploaded_files)
 
        if not duplicates:
            st.success("No duplicates found. All files are unique.")
        else:
            total = sum(len(files) for files in duplicates.values())
            st.write(f"Found **{total}** duplicate files in **{len(duplicates)}** group(s):")
 
            for file_hash, files in duplicates.items():
                st.write(f"**Group ({file_hash[:10]}...)**")
                for file in files:
                    st.write(f"- {file.name} ({file.size} bytes)")