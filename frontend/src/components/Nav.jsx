import { Link } from 'react-router-dom';

function Nav() {
  return (
    <nav style={{
      display: 'flex',
      gap: '24px',
      padding: '20px 40px',
      borderBottom: '1px solid #ddd',
      fontFamily: 'sans-serif'
    }}>
      <Link to="/">Bio</Link>
      <Link to="/expertise">Expertise</Link>
      <Link to="/gallery">Gallery</Link>
    </nav>
  );
}

export default Nav;