import codecs

with codecs.open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

clean_lines = lines[:896]

new_css = """
/* --- MOBILE MENU FIX --- */
@media (max-width: 767px) {
    .nav-controls.active {
        display: flex !important;
        flex-direction: column;
        position: absolute;
        top: 85px;
        left: 0;
        width: 100%;
        background: var(--white);
        padding: 32px 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        z-index: 1000;
        border-top: 1px solid #f1f5f9;
    }
    .nav-controls.active .nav-tabs {
        flex-direction: column;
        width: 100%;
        text-align: center;
        gap: 32px;
    }
    .nav-controls.active .btn {
        width: 100%;
        margin-top: 16px;
    }
}

.menu-toggle {
    font-size: 32px;
    padding: 5px;
}

/* --- CONTACT FORM STYLES & RECTANGULAR DESIGN --- */
.form-step {
    display: none;
}
.form-step.active {
    display: block;
    animation: fadeIn 0.4s ease forwards;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.rectangular-form {
    border-radius: 0 !important;
    border: 2px solid var(--dark-navy) !important;
    box-shadow: 8px 8px 0px rgba(30, 41, 59, 0.1) !important;
}

.rectangular-form .btn {
    border-radius: 0;
}

.rectangular-form input, .rectangular-form select, .rectangular-form textarea {
    border-radius: 0 !important;
    border: 1px solid #ccc !important;
}

.rectangular-form input:focus {
    border-color: var(--primary-blue) !important;
    outline: none;
}

.radio-card {
    border-radius: 0;
    border: 1px solid #ccc;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
    background: #fff;
}

.radio-card:hover {
    border-color: var(--primary-blue);
    background: rgba(59, 130, 246, 0.05);
}

.radio-grid {
    display: grid;
    gap: 16px;
    grid-template-columns: 1fr 1fr;
}

.radio-grid.vertical {
    grid-template-columns: 1fr;
}

.form-progress {
    height: 6px;
    background: #eee;
    margin-bottom: 24px;
    position: relative;
    border-radius: 0;
}

.progress-bar {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    background: var(--primary-blue);
    transition: width 0.3s ease;
}
"""

with codecs.open('style.css', 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)
    f.write(new_css)

print("Repaired style.css completely and safely.")
