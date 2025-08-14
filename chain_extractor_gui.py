import streamlit as st
def get_chains(pdb_path):
    chains = set()
    with open(pdb_path, "r") as pdb_file:
        for line in pdb_file:
            if line.startswith("ATOM"):
                chains.add(line[21])
    return sorted(chains)
def extract_chain(pdb_path, chain_id):
    extracted_lines = []
    with open(pdb_path, "r") as pdb_file:
        for line in pdb_file:
            if line.startswith("ATOM") and line[21] == chain_id:
                extracted_lines.append(line)
    return extracted_lines
st.title("Protein Chain Extractor")
uploaded_file = st.file_uploader("Upload a PDB file", type=["pdb"])
if uploaded_file is not None:
    with open("temp.pdb", "wb") as f:
        f.write(uploaded_file.getbuffer())
    chains = get_chains("temp.pdb")
    if chains:
        chain_id = st.selectbox("Select Chain ID", chains)
        extracted = extract_chain("temp.pdb", chain_id)
        if extracted:
            st.success(f"Extracted {len(extracted)} lines for chain {chain_id}")
            st.text_area("Extracted Chain Content", value="".join(extracted), height=300)
            output_file = f"extracted_chain_{chain_id}.pdb"
            with open(output_file, "w") as out_f:
                out_f.writelines(extracted)
            with open(output_file, "rb") as file:
                st.download_button(
                    label="Download Extracted Chain File",
                    data=file,
                    file_name=output_file,
                    mime="text/plain"
                )
        else:
            st.error(f"No data found for chain {chain_id}")
    else:
        st.error("No chains found in this file.")