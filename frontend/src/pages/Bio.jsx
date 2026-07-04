import Badge from '../components/Badge';
import Seal from '../components/Seal';

function Bio() {
  return (
    <div>
      {/* HERO */}
      <div style={{
        background: 'radial-gradient(120% 140% at 15% 0%, #1C3B29 0%, var(--ink) 45%, var(--ink-deep) 100%)',
        color: 'var(--paper)',
        padding: '90px 48px',
      }}>
        <div style={{
          maxWidth: '1100px',
          margin: '0 auto',
          display: 'grid',
          gridTemplateColumns: '1fr auto',
          gap: '40px',
          alignItems: 'center',
        }}>
          <div>
            <span style={{
              fontFamily: "'IBM Plex Mono', monospace",
              fontSize: '12px',
              letterSpacing: '0.14em',
              color: 'var(--gold-bright)',
            }}>SRI LANKA · ALL ISLAND</span>

            <h1 style={{ fontSize: 'clamp(40px,6vw,60px)', lineHeight: 1, marginTop: '18px' }}>
              Malith<br />Senanayake
            </h1>

            <p style={{ fontSize: '18px', marginTop: '18px', maxWidth: '480px', color: 'rgba(243,236,217,0.85)' }}>
              Licensed National Tour Guide, leading journeys across Sri Lanka in English and French for over fifteen years.
            </p>

            <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', marginTop: '30px' }}>
              <Badge>SLTDA Licensed Guide</Badge>
              <Badge>DELF C1 — Français</Badge>
              <Badge>15+ Years Experience</Badge>
              <Badge>All Island Coverage</Badge>
            </div>

            <div style={{ display: 'flex', gap: '14px', marginTop: '32px', flexWrap: 'wrap' }}>
              <a href="https://wa.me/94770188707" target="_blank" rel="noopener noreferrer" style={{
                background: 'var(--gold)', color: 'var(--ink-deep)', padding: '13px 22px',
                fontFamily: "'IBM Plex Mono', monospace", fontSize: '13px', borderRadius: '2px',
                textDecoration: 'none', fontWeight: 500,
              }}>Message on WhatsApp</a>
              <a href="mailto:senanayake.malith@gmail.com" style={{
                border: '1px solid rgba(243,236,217,0.4)', color: 'var(--paper)', padding: '13px 22px',
                fontFamily: "'IBM Plex Mono', monospace", fontSize: '13px', borderRadius: '2px',
                textDecoration: 'none',
              }}>Send an Email</a>
            </div>
          </div>

          <Seal />
        </div>
      </div>

      {/* ABOUT */}
      <div style={{ maxWidth: '700px', margin: '0 auto', padding: '80px 40px' }}>
        <span style={{
          fontFamily: "'IBM Plex Mono', monospace", fontSize: '12px',
          letterSpacing: '0.1em', color: 'var(--rust)',
        }}>ABOUT</span>
        <h2 style={{ fontSize: 'clamp(28px,4vw,38px)', marginTop: '14px' }}>
          Fifteen years on the road, in two languages
        </h2>
        <p style={{ fontSize: '18px', marginTop: '24px' }}>
          I've spent over fifteen years walking Sri Lanka's ancient cities, tea hills, and
          wildlife plains with travelers from around the world. Licensed by the Sri Lanka
          Tourism Development Authority as a National Tourist Guide, I lead tours in both
          English and French, holding a DELF C1 certification in French. My work is built on
          patience, real local knowledge, and a genuine love of sharing this island's history
          and nature.
        </p>

        <h2 style={{ fontSize: '26px', marginTop: '48px' }}>The Wasgamuwa Farm</h2>
        <p style={{ fontSize: '17px', marginTop: '12px' }}>
          On a half-acre of land bordering Wasgamuwa National Park, I grow coconut, pepper,
          jackfruit, and pineapple — a working farm that reflects rural life in this part of
          the island.
        </p>
      </div>
    </div>
  );
}

export default Bio;