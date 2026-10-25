import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Data Terminal", page_icon="🖥️", layout="centered")

# ==========================================
# ESTILIZAÇÃO VISUAL (GREEN CRT TERMINAL)
# ==========================================
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1a19;
        font-family: 'Courier New', Courier, monospace;
        color: #10ffb0;
    }
    .network-header {
        background-color: #00bf86;
        color: #05100e;
        font-weight: bold;
        font-size: 24px;
        padding: 6px 16px;
        display: inline-block;
        border-radius: 4px;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }
    .header-line {
        border-bottom: 2px solid #00bf86;
        margin-bottom: 25px;
    }
    .stRadio label {
        color: #10ffb0 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 18px !important;
    }
    .stTextInput input {
        background-color: #05100e !important;
        color: #10ffb0 !important;
        border: 1px solid #00bf86 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    .stButton button {
        background-color: #00bf86 !important;
        color: #05100e !important;
        font-weight: bold !important;
        border: none !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# STATUS DA REDE (ALTERE MANUALMENTE NO CÓDIGO)
# ==========================================
REDE_ONLINE = False  # Mude para True quando quiser simular que eles conectaram a rede!

# ==========================================
# BASE DE DADOS DE USUÁRIOS E CHAVES DE ACESSO
# ==========================================
USUARIOS = {
    "NPC-Richard": {
        "key": "SincR",
        "senha": "Bravo2021",
        "nome": "Captain Sinclair",
        "nivel": 4,
        "cargo": "Expedition Leader & Survival Specialist"
    },
    "NPC-Vera": {
        "key": "SousV",
        "senha": "belostomatidae",
        "nome": "Dr. Sousa",
        "nivel": 3,
        "cargo": "Biologist & Camp Doctor"
    },
    "NPC-Archie": {
        "key": "SdorA",
        "senha": "Sverige",
        "nome": "Sdöreman",
        "nivel": 2,
        "cargo": "Geologist & Resources"
    },
    "NPC-Nolan": {
        "key": "CollN",
        "senha": "01191993",
        "nome": "Collins",
        "nivel": 5,
        "cargo": "Data & communication engineer"
    }
}

# ==========================================
# INICIALIZAÇÃO DE SESSÃO
# ==========================================
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if "usuario_atual" not in st.session_state:
    st.session_state.usuario_atual = None

if "carregando" not in st.session_state:
    st.session_state.carregando = False

if "chat_mensagens" not in st.session_state:
    st.session_state.chat_mensagens = [
        {"autor": "AGT. COLLINS", "texto": "Channel established. All transmissions are encrypted."},
        {"autor": "SYSTEM", "texto": "Welcome to the secure peer-to-peer network."},
        {"autor": "AGT. COLLINS", "texto": "Archie, please. Let me know if you receive this. The team is talking about aborting the mission, so you need to show up asap. They don't care if someone gets left behind."},
        {"autor": "AGT. COLLINS", "texto": "I knew that something was off. I'm sorry."},
        {"autor": "AGT. COLLINS", "texto": "I'l tryna hold'em up, but idk how much time you have. In that case i'll leave food and water for u in the old deposit."},
        {"autor": "AGT. COLLINS", "texto": "Archie, are u there?"},
        {"autor": "AGT. COLLINS", "texto": "Were leaving through north, i'll wait for u there."}
    ]

# ==========================================
# TELA 1: AUTENTICAÇÃO
# ==========================================
if not st.session_state.autenticado and not st.session_state.carregando:
    st.markdown('<div class="network-header">NETWORK LOGIN</div>', unsafe_allow_html=True)
    st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)
    
    st.write("EXTRA-DIMENSIONAL RECONNAISSANCE DIVISION - PRIVATE DATA AND COMMUNICATION TERMINAL")
    st.write("RESTRICTED ACCESS SYSTEM BY CREDENTIAL LEVEL")
    st.write("")

    with st.form("form_login"):
        admin_key = st.text_input("ADMIN KEY:", type="default")
        senha = st.text_input("ACCESS PASSWORD:", type="password")
        botao_entrar = st.form_submit_button("AUTHENTICATE")

        if botao_entrar:
            login_sucesso = False
            user_encontrado = None

            for user_id, dados in USUARIOS.items():
                if admin_key == dados["key"] and senha == dados["senha"]:
                    login_sucesso = True
                    user_encontrado = dados
                    break
            
            if login_sucesso:
                st.session_state.usuario_atual = user_encontrado
                st.session_state.carregando = True
                st.rerun()
            else:
                st.error("ACCESS DENIED: INVALID KEY OR PASSWORD")

# ==========================================
# TELA DE CARREGAMENTO ISOLADA
# ==========================================
elif st.session_state.carregando:
    user = st.session_state.usuario_atual
    
    if user is not None:
        st.markdown('<div class="network-header">SYSTEM INITIALIZATION</div>', unsafe_allow_html=True)
        st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)
        
        st.write(f"### WELCOME AGENT {user['nome'].upper()}")
        st.write("INITIALIZING TERMINAL SESSION...")
        st.write("")

        progress_bar = st.progress(0)
        status_text = st.empty()

        for percent in range(0, 101, 10):
            time.sleep(0.35)
            progress_bar.progress(percent)
            status_text.text(f"LOADING SYSTEM MODULES... {percent}%")

        st.session_state.carregando = False
        st.session_state.autenticado = True
        st.rerun()

# ==========================================
# TELA 2: MENU PRINCIPAL (DINÂMICO POR NÍVEL)
# ==========================================
elif st.session_state.autenticado and st.session_state.usuario_atual is not None:
    user = st.session_state.usuario_atual
    
    st.markdown('<div class="network-header">NETWORK LOGIN</div>', unsafe_allow_html=True)
    st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)
    
    # 1. Cria duas colunas: a da esquerda (larga) para o usuário e a da direita (curta) para o status
    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(f"CONNECTED OPERATOR: **{user['nome']}** | ROLE: **{user['cargo']}**")
        st.write(f"CREDENTIAL LEVEL: **{user['nivel']}**")

    with col2:
        # Indicador discreto alinhado no canto direito
        if REDE_ONLINE:
            st.markdown("<p style='text-align: right; color: #10ffb0; font-size: 13px;'>🔴 <b>ONLINE</b></p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='text-align: right; color: #ff5555; font-size: 13px;'>🔴 <b>OFFLINE</b></p>", unsafe_allow_html=True)

    st.write("---")

    opcoes_disponiveis = []
    
    if user["nivel"] >= 1:
        opcoes_disponiveis.append("-> Electronic Mail")
        opcoes_disponiveis.append("-> Data Transfers")
    if user["nivel"] == 2 or user["nivel"] == 5:
        opcoes_disponiveis.append("-> Private Chat")
    if user["nivel"] >= 3:
        opcoes_disponiveis.append("-> Staff Services")
    if user["nivel"] >= 4:
        opcoes_disponiveis.append("-> Remote Terminal Access")

    opcoes_disponiveis.sort()
        
    opcoes_disponiveis.append("-> Log Out")

    opcao = st.radio(label="", options=opcoes_disponiveis)
    st.write("---")

    if opcao == "-> Staff Services":
        st.subheader("> STAFF SERVICES [RESTRICTED LEVEL III+]")
        st.write("PERSONNEL BIOMETRIC RECORD CONSULTATION")
        
        agente_select = st.selectbox(
            "SELECT AGENT RECORD:",
            ["AGT. SINCLAIR-2026-01", "AGT. SOUSA-2026-02", "AGT. SDOREMAN-2026-03", "AGT. COLLINS- 2026-04"]
        )
        
        if "2026-01" in agente_select:
            st.code("""
[ CONFIDENTIAL PERSONNEL RECORD ]
FILE: AGT. SINCLAIR-2026-01 | STATUS: ACTIVE
ROLE: Field Leader & Survival Specialist
PSI (Psychic Stability Index): 92/100
AUTHORIZED PERSONAL ITEM: Mechanical Pocket Compass and [REDACTED]
NOTES: Military rescue training. High resistance to anomalous stress. 
Excessive rigidity in protocols and insensitivity regarding personal matters.
            """, language="yaml")
        elif "2026-02" in agente_select:
            st.code("""
[ CONFIDENTIAL PERSONNEL RECORD ]
FILE: AGT. SOUSA-2026-02 | STATUS: ACTIVE
ROLE: Biologist and Field Doctor
PSI (Psychic Stability Index): 82/100
AUTHORIZED PERSONAL ITEM: 
NOTES: Specialist in zoology of hostile environments.
            """, language="yaml")
        elif "2026-03" in agente_select:
            st.code("""
[ CONFIDENTIAL PERSONNEL RECORD ]
FILE: AGT. SDÖREMAN-2026-03 | STATUS: ACTIVE
ROLE: Geologist & Cartography/Resources Specialist
PSI (Psychic Stability Index): 52/100
AUTHORIZED PERSONAL ITEM: Precision Geological Sampler
NOTES: Displayed PSI fluctuations after analysis of local waters. 
Social isolation may be needed.
            """, language="yaml")
        elif "2026-04" in agente_select:
            st.code("""
[ CONFIDENTIAL PERSONNEL RECORD ]
FILE: AGT. COLLINS-2026-03 | STATUS: ACTIVE
ROLE: Data Engineer and Communication
PSI (Psychic Stability Index): 78/100
AUTHORIZED PERSONAL ITEM: A tactile stress-relief metallic Rubik's cube
NOTES: Data specialist and reserved. 
It doesn't go out if not the dormitories or the central comns. 
            """, language="yaml")

    elif opcao == "-> Remote Terminal Access":
        st.subheader("> REMOTE TERMINAL ACCESS [EXCLUSIVE LEVEL IV]")
        st.write("DIRECT CONNECTION TO EXPEDITION CENTRAL NODE")
        st.code("""
[ P.A.N.A.C.E.A. PROTOCOL ACTIVE ]
NODE STATUS: ONLINE
EXTRA-DIMENSIONAL NAVIGATION SYSTEM: CONNECTED
TACTICAL ALERT: Spatial anomaly detected in sector 46.
DOOR REINITIALIZATION OPTION AVAILABLE.
        """, language="bash")

    elif opcao == "-> Electronic Mail":
        st.subheader("> ELECTRONIC MAIL")
        st.write("OPERATOR INBOX: LOCAL")
        st.write("---")
        
        with st.expander("• [GENERAL NOTICE] Tape logs reminder"):
            st.write("**FROM:** AGT. SINCLAIR")
            st.write("**BODY:** Reminder: Keep your tape logs and your reports updated at all times.")

        if user["nivel"] == 2:
            with st.expander("[FROM: AGT. SINCLAIR] Unofficial call"):
                st.write("**BODY:** Sr. Söderman, i'm requesting your geologists services for an expediction by the level 1 area. Report to me as soon as possible.")
            with st.expander("[FROM: AGT. SOUSA] Mission requirement"):
                st.write("Agt. Sdöreman, i need your help in a expediction by the pool area. I suspect that our visitor may have come form there. I need to take a better look and i can't do it without you.")
            with st.expander("[FROM: AGT. SINCLAIR] Unofficial call"):
                st.write("**BODY:** Sr. Söderman, it was discovered a unnatural water source and i need you run some tests in the area. Report to me as soon as possible.")
            with st.expander("[FROM: AGT. COLLINS] AdminKey Changes"):
                st.write("**BODY:** I made an upgrade in your AdminKey. You thanks me later.")
            with st.expander("[FROM: AGT. SOUSA] Presence requirement"):
                st.write("Archie, i fear that you might be contaminated due our last expecditions. So, i'm running some checkups with the team and you included. Talk to me in the medbay when you finish your work, please.")

        if user["nivel"] == 3:
            with st.expander("[FROM: AGT. SDÖREMAN] Apology"):
                st.write("**BODY:** I am sorry for yesterday, Dr. Sousa, if we could talk in private later i would be glad. I promisse that it won't happen again.")
            with st.expander("[FROM: AGT. COLLINS] Concern about health"):
                st.write("**BODY:** Dr., i am worried about agt. Sdöreman. Can you check him, please? I know that he's having trouble remembering about things and often feeling sick. I shoudn't be telling you this, so if you could be discreet i will be happy.")

        if user["nivel"] >= 4:
            with st.expander("⚠️ [PRIVATE - LEVEL IV] Containment protocol"):
                st.write("**FROM:** E.R.D. CENTRAL COMMAND")
                st.write("**SUBJECT:** Containment protocol and evacuation plan.")
                st.write("**MESSAGE:** If the group's psychic stability (PSI) falls below 40%, the remote node must be isolated immediately.")
                st.write("In that case, the emergency protocol must be followed.")

            with st.expander("• [REPLY TO: CENTRAL COMMAND] Personal Records Status"):
                st.write("**FROM:** AGT. SINCLAIR")
                st.write("**BODY:** Dr. Sousa has already updated our personal records. There is nothing to worry about. The mission must proceed.")

    elif opcao == "-> Data Transfers":
        if user["nivel"] == 2:
            st.subheader("> DATA TRANSFERS")
            st.write("REPORTS DOWNLOAD")
            st.write("1. `Cartography_Log_03.dat` (Sent sucessfully)")
            st.write("2. `Geological_Sample_PNC.csv` (Sent sucessfully)")
            st.write("3. `Level_0.8_Report_Update.pdf` (Sent sucessfully)" )
            st.write("4. `Cartography_Log_04.dat` (Sent sucessfully)")
        elif user["nivel"] == 3:
            st.subheader("> DATA TRANSFERS")
            st.write("REPORTS DOWNLOAD")
            st.write("1. `Full_Biometric_Files.pdf` (Sent sucessfully)")
            st.write("2. `Identification_Report_Day15.csv` (Sent sucessfully)")
        elif user["nivel"] == 4:
            st.subheader("> DATA TRANSFERS")
            st.write("REPORTS DOWNLOAD")
            st.write("1. `Mission_Reports_Files.pdf` (Sent sucessfully)")
            st.write("2. `Armory_Report_Check.pdf` (Sent sucessfully)")


    elif opcao == "-> Private Chat":
        st.subheader("> PRIVATE CHAT [SECURE P2P NODE]")
        
        # Exibe status específico da conexão do Chat
        if REDE_ONLINE:
            st.caption("🟢 CONNECTION ESTABLISHED WITH EXTERNAL NODES")
        else:
            st.caption("🔴 OFFLINE NODE — SHOWING LOCAL CACHED TRANSMISSIONS ONLY")
            
        st.write(f"ACTIVE AGENT: {user['nome'].upper()}")
        st.write("---")

        # Exibe as mensagens padrão do histórico
        for msg in st.session_state.chat_mensagens:
            if msg["autor"] == "SYSTEM":
                st.caption(f"🤖 **[SYSTEM]:** {msg['texto']}")
            elif msg["autor"] == user["nome"].upper():
                st.markdown(f"> **YOU ({msg['autor']}):** {msg['texto']}")
            else:
                st.markdown(f"**[{msg['autor']}]:** {msg['texto']}")

        # NOVAS MENSAGENS TRANSMITIDAS SÓ QUANDO CONECTAREM A REDE:
        if REDE_ONLINE:
            st.write("---")
            st.warning("⚠️ NEW INCOMING TRANSMISSION RECEIVED")
            st.markdown("**[AGT. ARCHIE]:** *Guys, do you copy? The signal is restored!*")
            st.markdown("**[SYSTEM]:** *Incoming external data packet detected.*")

        st.write("---")

    elif opcao == "-> Log Out":
        st.session_state.autenticado = False
        st.session_state.usuario_atual = None
        st.session_state.carregando = False
        st.rerun()