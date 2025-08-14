import streamlit as st
import math

# ---------------- Page Config ----------------
st.set_page_config(page_title="Protein Structure Toolkit", layout="wide", initial_sidebar_state="auto")

# ---------------- Dark Theme CSS ----------------
st.markdown("""
<style>
.stApp { background-color: #003333; color: #e0f7f7; }
section[data-testid="stSidebar"] { background-color: #004d4d; color: #e0f7f7; }
input, textarea, select {
    background-color: #003f3f !important;
    color: #d0f0f0 !important;
    border: 1px solid #00b2b2 !important;
    border-radius: 6px !important;
}
::placeholder { color: #a0d6d6 !important; opacity: 1 !important; }
.stButton>button, .stDownloadButton>button {
    background-color: #007a7a !important;
    color: #e0f7f7 !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}
.stButton>button:hover, .stDownloadButton>button:hover { background-color: #00cccc !important; }
section[data-testid="stSidebar"] * { color: #e0f7f7 !important; }
h1, h2, h3, h4, h5, h6 { color: #b2f0f0 !important; font-weight: 700 !important; }
p, span, div, label { color: #ccf9f9 !important; }
</style>
""", unsafe_allow_html=True)

# ---------------- Helper Functions ----------------
def decode_bytes(bytes_obj):
    return bytes_obj.decode("utf-8", errors="ignore")

def parse_lines_from_bytes(bytes_obj):
    return decode_bytes(bytes_obj).splitlines()

def get_chains_from_lines(lines):
    return sorted({ln[21] for ln in lines if ln.startswith(("ATOM", "HETATM"))})

def get_hetero_from_lines(lines):
    return sorted({ln[17:20].strip() for ln in lines if ln.startswith("HETATM") and ln[17:20].strip() not in ("HOH", "H2O")})

def ensure_file_loaded():
    uploaded = st.file_uploader("Upload PDB file", type=["pdb"], key=f"uploader_{st.session_state.page}")
    if uploaded:
        st.session_state.pdb_bytes = uploaded.getvalue()
        st.session_state.pdb_name = uploaded.name
        st.success(f"Loaded: {uploaded.name}")
    if st.session_state.get("pdb_bytes") is None:
        st.warning("Please upload a PDB file to continue.")
        return False
    return True

# ---------------- Session Defaults ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "pdb_bytes" not in st.session_state:
    st.session_state.pdb_bytes = None
if "pdb_name" not in st.session_state:
    st.session_state.pdb_name = ""

# ---------------- Navigation ----------------
def back_home():
    st.session_state.page = "home"

# ---------------- Pages ----------------
def home_page():
    st.title("Protein Structure Toolkit")
    col_upload, col_clear = st.columns([4, 1])
    with col_upload:
        uploaded = st.file_uploader("Upload PDB file", type=["pdb"], key="home_upload")
    with col_clear:
        if st.session_state.get("pdb_bytes") and st.button("❌ Clear"):
            st.session_state.pdb_bytes = None
            st.session_state.pdb_name = ""
            st.session_state.home_upload = None
            st.experimental_rerun()
    if uploaded:
        st.session_state.pdb_bytes = uploaded.getvalue()
        st.session_state.pdb_name = uploaded.name
        st.success(f"Loaded: {uploaded.name}")
    st.write("Choose a tool:")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔗 Chain Extractor"): st.session_state.page = "chain"
    with col2:
        if st.button("💧 Water Remover"): st.session_state.page = "water"
    with col3:
        if st.button("💊 Ligand Isolator"): st.session_state.page = "ligand"
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("🧪 Protein Extractor"): st.session_state.page = "protein"
    with col5:
        if st.button("📏 Distance Calculator"): st.session_state.page = "distance"
    with col6:
        if st.button("🎯 Residues Within Cutoff"): st.session_state.page = "cutoff"
    if st.session_state.get("pdb_bytes"):
        st.info(f"Current PDB loaded: **{st.session_state.pdb_name}**")

def chain_extractor_page():
    st.header("Chain Extractor 🧬")
    if not ensure_file_loaded(): return
    lines = parse_lines_from_bytes(st.session_state.pdb_bytes)
    chain = st.selectbox("Select chain", get_chains_from_lines(lines))
    if st.button("Extract chain"):
        extracted = [ln for ln in lines if ln.startswith(("ATOM", "HETATM")) and ln[21] == chain]
        st.success(f"Chain {chain} extracted. File ready for download.")
        st.download_button("Download PDB", "\n".join(extracted), file_name=f"chain_{chain}.pdb", mime="chemical/x-pdb")
    st.button("⬅ Back to Home", on_click=back_home)

def water_remover_page():
    st.header("Water Remover 💧")
    if not ensure_file_loaded(): return
    lines = parse_lines_from_bytes(st.session_state.pdb_bytes)
    if st.button("Remove HOH"):
        out_lines = [ln for ln in lines if not (ln.startswith("HETATM") and ln[17:20].strip() == "HOH")]
        st.success("Water molecules removed. File ready for download.")
        st.download_button("Download PDB", "\n".join(out_lines), file_name="without_HOH.pdb", mime="chemical/x-pdb")
    st.button("⬅ Back to Home", on_click=back_home)

def ligand_isolator_page():
    st.header("Ligand Isolator 💊")
    if not ensure_file_loaded(): return
    lines = parse_lines_from_bytes(st.session_state.pdb_bytes)
    ligand = st.selectbox("Select ligand (3-letter code)", get_hetero_from_lines(lines))
    if st.button("Isolate ligand"):
        extracted = [ln for ln in lines if ln.startswith("HETATM") and ln[17:20].strip() == ligand]
        st.success(f"Ligand {ligand} ready for download.")
        st.download_button("Download PDB", "\n".join(extracted), file_name=f"ligand_{ligand}.pdb", mime="chemical/x-pdb")
    st.button("⬅ Back to Home", on_click=back_home)

def protein_extractor_page():
    st.header("Protein Extractor 🧪")
    if not ensure_file_loaded(): return
    if st.button("Extract protein"):
        lines = parse_lines_from_bytes(st.session_state.pdb_bytes)
        extracted = [ln for ln in lines if ln.startswith("ATOM")]
        st.success("Protein extracted. File ready for download.")
        st.download_button("Download PDB", "\n".join(extracted), file_name="extracted_protein.pdb", mime="chemical/x-pdb")
    st.button("⬅ Back to Home", on_click=back_home)

def distance_calculator_page():
    st.header("Distance Calculator 📏")
    if not ensure_file_loaded(): return
    lines = parse_lines_from_bytes(st.session_state.pdb_bytes)
    chain = st.selectbox("Select chain", get_chains_from_lines(lines))
    res1 = st.text_input("Residue 1")
    res2 = st.text_input("Residue 2")
    if st.button("Calculate distance"):
        ca_atoms = {ln[22:26].strip(): (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))
                    for ln in lines if ln.startswith("ATOM") and ln[21] == chain and ln[12:16].strip() == "CA"}
        if res1 in ca_atoms and res2 in ca_atoms:
            st.success(f"Distance between {chain}{res1} and {chain}{res2}: {math.dist(ca_atoms[res1], ca_atoms[res2]):.2f} Å")
        else:
            st.error("One or both residues not found.")
    st.button("⬅ Back to Home", on_click=back_home)

def cutoff_page():
    st.header("Residues Within Cutoff 🎯")
    if not ensure_file_loaded(): return
    lines = parse_lines_from_bytes(st.session_state.pdb_bytes)
    chain = st.selectbox("Select chain", get_chains_from_lines(lines))
    ref_res = st.text_input("Reference residue")
    cutoff = st.number_input("Cutoff distance (Å)", min_value=0.1, value=5.0, step=0.1)
    if st.button("Find residues"):
        ca_atoms = {ln[22:26].strip(): (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))
                    for ln in lines if ln.startswith("ATOM") and ln[21] == chain and ln[12:16].strip() == "CA"}
        if ref_res not in ca_atoms:
            st.error("Reference residue not found.")
        else:
            ref_coord = ca_atoms[ref_res]
            results = [f"{rn}\t{math.dist(ref_coord, coord):.2f} Å"
                       for rn, coord in ca_atoms.items() if rn != ref_res and math.dist(ref_coord, coord) <= cutoff]
            if results:
                st.text_area("Residues within cutoff", value="\n".join(results), height=300)
            else:
                st.info("No residues within cutoff.")
    st.button("⬅ Back to Home", on_click=back_home)

# ---------------- Router ----------------
page = st.session_state.page
if page == "home": home_page()
elif page == "chain": chain_extractor_page()
elif page == "water": water_remover_page()
elif page == "ligand": ligand_isolator_page()
elif page == "protein": protein_extractor_page()
elif page == "distance": distance_calculator_page()
elif page == "cutoff": cutoff_page()