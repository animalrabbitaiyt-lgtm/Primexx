css_code = """
/* =========================================================================
   WORK PAGE SERVICES GRID (RawEditt Style)
   ========================================================================= */

.raw-service-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
    gap: 32px;
    padding-top: 40px;
}

.raw-card {
    background: #0a0a0d;
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 30px 30px 0 30px;
    display: flex;
    flex-direction: column;
    min-height: 420px;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
    overflow: hidden;
    position: relative;
    text-decoration: none;
}

.raw-card:hover {
    transform: translateY(-8px);
    border-color: rgba(124, 58, 237, 0.4);
    box-shadow: 0 15px 40px rgba(124, 58, 237, 0.1);
}

.raw-card-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 24px;
}

.raw-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(124, 58, 237, 0.1);
    border-radius: 12px;
    color: var(--accent-color);
}

.raw-num {
    font-size: 4.5rem;
    font-weight: 800;
    font-family: var(--font-heading);
    color: transparent;
    -webkit-text-stroke: 1px rgba(255,255,255,0.1);
    line-height: 0.8;
    transition: all 0.4s ease;
    user-select: none;
}

.raw-card:hover .raw-num {
    -webkit-text-stroke: 1.5px var(--accent-color);
    text-shadow: 0 0 20px rgba(124, 58, 237, 0.4);
}

.raw-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 30px;
    line-height: 1.3;
}

.raw-img-container {
    margin-top: auto;
    width: 100%;
    margin-bottom: 30px;
    border-radius: 16px;
    overflow: hidden;
    aspect-ratio: 16/10;
    border: 1px solid rgba(255,255,255,0.05);
}

.raw-img-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}

.raw-card:hover .raw-img-container img {
    transform: scale(1.05);
}
"""

with open('d:\\CODING\\primex\\style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)
print("CSS injected successfully")
