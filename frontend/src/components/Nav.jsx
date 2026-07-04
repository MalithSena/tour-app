import { Link } from 'react-router-dom';

function Nav() {
  const linkStyle = {
    fontFamily: "'IBM Plex Mono', monospace",
    fontSize: '13px',
    letterSpacing: '0.06em',
    textTransform: 'uppercase',
    color: 'var(--paper)',
  };

  return (
    <nav style={{
      display: 'flex',
      gap: '32px',
      padding: '24px 48px',
      background: 'var(--ink)',
      borderBottom: '1px solid rgba(201,154,59,0.25)',
    }}>
      <Link to="/" style={linkStyle}>Bio</Link>
      <Link to="/expertise" style={linkStyle}>Expertise</Link>
      <Link to="/gallery" style={linkStyle}>Gallery</Link>
    </nav>
  );
}

export default Nav;