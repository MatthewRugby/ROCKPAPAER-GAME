import streamlit as st
import random
import string
import pyperclip

# Page configuration
st.set_page_config(
    page_title="🔐 Password Generator",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        padding: 2rem 1rem;
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    .password-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
        word-break: break-all;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 5px;
        color: #155724;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 5px;
        color: #0c5460;
        margin: 1rem 0;
    }
    h1 {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    h2 {
        color: #667eea;
        border-bottom: 2px solid #667eea;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generated_passwords' not in st.session_state:
    st.session_state.generated_passwords = []
if 'copied' not in st.session_state:
    st.session_state.copied = False

# Title and description
st.markdown("<h1>🔐 Password Generator</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: white; margin-bottom: 2rem;'>
    <p style='font-size: 1.1rem;'>Create strong, secure passwords instantly</p>
    <p style='font-size: 0.9rem; opacity: 0.9;'>Never reuse passwords again! 🛡️</p>
</div>
""", unsafe_allow_html=True)

# Main container with two columns
col1, col2 = st.columns([2, 1], gap="medium")

with col1:
    st.markdown("<h2>⚙️ Configure Your Password</h2>", unsafe_allow_html=True)
    
    # Password length slider
    password_length = st.slider(
        "📏 Password Length",
        min_value=4,
        max_value=128,
        value=16,
        step=1,
        help="Longer passwords are more secure"
    )
    
    # Character type selections
    st.markdown("### 🔤 Character Types")
    
    col_a, col_b = st.columns(2)
    with col_a:
        use_uppercase = st.checkbox(
            "Uppercase (A-Z)",
            value=True,
            help="Include uppercase letters"
        )
        use_digits = st.checkbox(
            "Digits (0-9)",
            value=True,
            help="Include numbers"
        )
    
    with col_b:
        use_lowercase = st.checkbox(
            "Lowercase (a-z)",
            value=True,
            help="Include lowercase letters"
        )
        use_special = st.checkbox(
            "Special (!@#$%)",
            value=True,
            help="Include special characters"
        )
    
    # Password count
    st.markdown("### 📦 Generate Multiple")
    num_passwords = st.slider(
        "Number of passwords to generate",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

with col2:
    st.markdown("<h2>💪 Password Strength</h2>", unsafe_allow_html=True)
    
    # Calculate password strength
    char_types = sum([use_uppercase, use_lowercase, use_digits, use_special])
    
    strength_score = (password_length / 20) + (char_types / 4)
    strength_score = min(strength_score, 2)
    
    if strength_score >= 1.5:
        strength = "🟢 Strong"
        strength_color = "#28a745"
    elif strength_score >= 1:
        strength = "🟡 Medium"
        strength_color = "#ffc107"
    else:
        strength = "🔴 Weak"
        strength_color = "#dc3545"
    
    st.markdown(f"""
    <div style='background-color: {strength_color}; color: white; padding: 1rem; border-radius: 5px; text-align: center; font-weight: bold; font-size: 1.2rem;'>
        {strength}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style='background-color: #e9ecef; padding: 0.8rem; border-radius: 5px; font-size: 0.9rem;'>
        <p><strong>Length:</strong> {password_length}</p>
        <p><strong>Character Types:</strong> {char_types}/4</p>
        <p><strong>Combinations:</strong> {('Very High' if strength_score >= 1.5 else ('High' if strength_score >= 1 else 'Low'))}</p>
    </div>
    """, unsafe_allow_html=True)

# Validation
if not any([use_uppercase, use_lowercase, use_digits, use_special]):
    st.warning("⚠️ Please select at least one character type!")
else:
    # Generate button
    col_gen1, col_gen2 = st.columns([2, 1])
    
    with col_gen1:
        if st.button("🚀 Generate Password(s)", use_container_width=True, key="generate_btn"):
            # Clear previous passwords
            st.session_state.generated_passwords = []
            
            # Build character set
            characters = ""
            if use_lowercase:
                characters += string.ascii_lowercase
            if use_uppercase:
                characters += string.ascii_uppercase
            if use_digits:
                characters += string.digits
            if use_special:
                characters += string.punctuation
            
            # Generate passwords
            for _ in range(num_passwords):
                password = ''.join(random.choice(characters) for _ in range(password_length))
                st.session_state.generated_passwords.append(password)
    
    # Display generated passwords
    if st.session_state.generated_passwords:
        st.markdown("<h2>✨ Generated Password(s)</h2>", unsafe_allow_html=True)
        
        if len(st.session_state.generated_passwords) == 1:
            # Single password - large display
            password = st.session_state.generated_passwords[0]
            st.markdown(f"""
            <div class='password-box'>
                <h3 style='margin: 0 0 1rem 0; color: #667eea;'>Your Password:</h3>
                <p style='font-size: 1.3rem; margin: 0; word-break: break-all;'>{password}</p>
            </div>
            """, unsafe_allow_html=True)
            
            col_copy1, col_copy2 = st.columns(2)
            with col_copy1:
                if st.button("📋 Copy to Clipboard", use_container_width=True):
                    try:
                        pyperclip.copy(password)
                        st.success("✅ Copied to clipboard!")
                    except:
                        st.info("📌 Copy manually: Right-click above and select Copy")
            
            with col_copy2:
                if st.button("🔄 Regenerate", use_container_width=True):
                    st.rerun()
        
        else:
            # Multiple passwords - list display
            st.markdown(f"<p style='color: #667eea; font-weight: bold;'>Generated {len(st.session_state.generated_passwords)} passwords:</p>", unsafe_allow_html=True)
            
            for i, password in enumerate(st.session_state.generated_passwords, 1):
                col_num, col_pass, col_copy = st.columns([0.5, 3, 1])
                
                with col_num:
                    st.markdown(f"<p style='margin: 0; font-weight: bold;'>{i}.</p>", unsafe_allow_html=True)
                
                with col_pass:
                    st.markdown(f"""
                    <div style='background-color: #f0f2f6; padding: 0.8rem; border-radius: 5px; font-family: monospace; word-break: break-all;'>
                        {password}
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_copy:
                    if st.button("📋", key=f"copy_{i}", help=f"Copy password {i}"):
                        try:
                            pyperclip.copy(password)
                            st.success(f"✅ Password {i} copied!")
                        except:
                            st.info("📌 Copy manually")
            
            if st.button("🔄 Regenerate All", use_container_width=True):
                st.rerun()

# Security tips section
st.markdown("<h2>🛡️ Security Tips</h2>", unsafe_allow_html=True)

tips_col1, tips_col2 = st.columns(2)

with tips_col1:
    st.markdown("""
    **✅ Do's:**
    - ✓ Use 12+ character passwords
    - ✓ Mix uppercase, lowercase, numbers & symbols
    - ✓ Use unique passwords for each account
    - ✓ Store in a password manager
    - ✓ Update passwords regularly
    """)

with tips_col2:
    st.markdown("""
    **❌ Don'ts:**
    - ✗ Don't use birthdays or names
    - ✗ Don't reuse passwords
    - ✗ Don't share passwords via email
    - ✗ Don't write passwords on sticky notes
    - ✗ Don't use common words
    """)

st.markdown("<div style='text-align: center; color: #667eea; margin-top: 2rem; padding: 1rem; border-top: 2px solid #667eea;'><p>🔒 Your passwords are generated locally and never stored or transmitted</p></div>", unsafe_allow_html=True)
